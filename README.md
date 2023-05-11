# Readme

## Introduction

This application takes in a CSV file that was output from a UiPath RPA script, transforms and cleans the raw data, connects to a PostgreSQL database, creates database tables, and inserts the cleaned CSV data into the database.

## How It works

1. A Google Cloud cron job starts the VM once per day at a specific time
2. Windows job scheduler runs a powershell script that:
    - Opens a Google Chrome Instance
    - Opens a UiPath instance by calling a specific Uipath script
    - Starts a UiPath script that scrapes job data from indeed and saves it data to a csv file
3. The python code in this repo takes in the csv file as an input
4. The data is transformed and cleaned
5. Finally the data is inserted into a Postgresql database

## Contributing

Contributions to this project are welcome. Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This application is licensed under the MIT license. See the LICENSE file for more details.
