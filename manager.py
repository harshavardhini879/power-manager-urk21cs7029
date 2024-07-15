# src/database_manager.py
import sqlite3
import os

class DatabaseManager:
    def _init_(self, db_path='../data/power_manager_telemetry.db'):
        db_dir = os.path.dirname(os.path.abspath(db_path))
        os.makedirs(db_dir, exist_ok=True)
        self.conn = sqlite3.connect(os.path.abspath(db_path))
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS telemetry_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            cpu_usage REAL NOT NULL,
            memory_usage REAL NOT NULL,
            disk_usage REAL NOT NULL,
            nic_usage REAL NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_telemetry_data(self, data):
        query = '''
        INSERT INTO telemetry_data (timestamp, cpu_usage, memory_usage, disk_usage, nic_usage)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (data['timestamp'], data['cpu_usage'], data['memory_usage'], data['disk_usage'], data['nic_usage']))
        self.conn.commit()

    def get_all_data(self):
        query = 'SELECT * FROM telemetry_data'
        cursor = self.conn.execute(query)
        rows = cursor.fetchall()
        return rows