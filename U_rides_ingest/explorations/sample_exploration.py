# Databricks notebook source
# MAGIC %md Ingest real time data from event hub

# COMMAND ----------


from pyspark.sql.functions import *
from pyspark.sql.types import *

# Event Hubs configuration
EH_NAMESPACE                    = "taxi-saida-eventhub"
EH_NAME                         = "uutopic"



# Retrieve connection string from Databricks Secrets
EH_CONN_STR = dbutils.secrets.get(scope="eventhub-secrets", key="connection-string")

KAFKA_OPTIONS = {
  "kafka.bootstrap.servers"  : f"{EH_NAMESPACE}.servicebus.windows.net:9093",
  "subscribe"                : EH_NAME,
  "kafka.sasl.mechanism"     : "PLAIN",
  "kafka.security.protocol"  : "SASL_SSL",
  "kafka.sasl.jaas.config"   : f"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username=\"$ConnectionString\" password=\"{EH_CONN_STR}\";",
  "kafka.request.timeout.ms" : 10000,
  "kafka.session.timeout.ms" : 10000,
  "maxOffsetsPerTrigger"     : 10000,
  "failOnDataLoss"           : 'true',
  "startingOffsets"          : 'earliest'
}

df = spark.readStream.format("kafka")\
    .options(**KAFKA_OPTIONS)\
    .load()

display(df, checkpointLocation = "/Volumes/u_catalog/bronze/my_volume/")

df = df.withColumn("ride", col("value").cast(StringType()))