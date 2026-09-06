# Urides_project

# U-Rides Data Streaming Project

This project contains the data engineering implementation for the U-Rides
data streaming and ingestion pipeline.

## Project Structure

### `Data/`

Contains the JSON data and mapping files used by the project.

The folder includes:

- `bulk_rides.json`
- `map_cancellation_reasons.json`
- `map_payment_methods.json`
- `map_cities.json`
- `map_vehicle_types.json`
- `map_ride_statuses.json`
- `map_vehicle_makes.json`

### `Rides_Data_Streaming/`

Contains the main U-Rides streaming pipeline artifacts and source code
developed in Databricks.

### `U_rides_ingest/`

Contains supporting files from the original U-Rides ingestion development.

It includes:

- `exploration/` — sample and exploratory notebooks used during development
- `utilities/` — utility files used by the project
- `files_array.json` — list of JSON files used by the ingestion process
- Additional supporting project files and documentation

## Data Files Configuration

The `files_array.json` file contains the list of data files used by the
ingestion process.

The configured files are:

- `map_cancellation_reasons`
- `map_payment_methods`
- `map_cities`
- `map_vehicle_types`
- `map_ride_statuses`
- `map_vehicle_makes`
- `bulk_rides`

## Security

No secrets or credentials should be stored in this repository.

ADLS Gen2 secret keys were removed from the exploration code before
committing the project to GitHub.

Authentication credentials and connection information should be provided
through secure Databricks configuration or secret management mechanisms
rather than being hard-coded in source code.

## Development Environment

The project was developed using:

- Databricks
- Python
- PySpark
- Git/GitHub
