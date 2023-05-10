# Python SQLite RFID Tracking System

This is a Python-based system that tracks RFID tags using SQLite as the database. It allows users to track their cards with Auto RFID UUID Checking.

## Requirements

- Python 3.x
- SQLite 3.x
- Python SQLite3 module

## Installation

1. Clone or download the repository.
2. Install Python if it's not already installed on your system.
3. Install SQLite if it's not already installed on your system.
4. Install the Python SQLite3 module if it's not already installed on your system. You can install it using pip: `pip install pysqlite3`
5. Create a new SQLite database using the provided schema file `rfid_db_schema.sql`.
6. Modify the database configuration in the `config.py` file to match your database configuration.

## Usage

1. Run the `main.py` script to start the program.
2. Follow the on-screen instructions to perform CRUD operations on the database.
3. Use the `quit` command to exit the program.

## Database Schema

The database schema consists of two tables:

### rfid_tags

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | INTEGER | Unique identifier for the tag. |
| tag_uid | TEXT | Unique identifier for the tag. |
| name | TEXT | Name of the tag owner. |
| description | TEXT | Description of the tag. |
| created_at | TEXT | Timestamp of when the tag was created. |
| updated_at | TEXT | Timestamp of when the tag was last updated. |

### rfid_logs

| Column Name | Data Type | Description |
|-------------|----------|-------------|
| id | INTEGER | Unique identifier for the log entry. |
| tag_id | INTEGER | Foreign key referencing the `id` column of the `rfid_tags` table. |
| timestamp | TEXT | Timestamp of when the RFID tag was detected. |
| direction | TEXT | Direction of the RFID tag (in or out). |

## License

This system is released under the MIT License. See LICENSE file for details.
