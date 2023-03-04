#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import sqlite3


def init_data(path, station_file_path, cycling_file_path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute('''DELETE FROM station''')
    cur.execute('''DELETE FROM cycling''')
    with open(station_file_path) as f:
        reader = list(csv.reader(f))
        for row in reader[1:]:
            station_name, station_lat, station_lon, station_id, station_type = row
            cur.execute('''INSERT INTO station VALUES (?,?,?,?,?)''',
                        (station_id, station_name, station_lat, station_lon, station_type))
            con.commit()
    cycling_ids = []
    with open(cycling_file_path) as f:
        reader = list(csv.reader(f))
        for row in reader[1:]:
            cycling_id, start_time, end_time, duration, from_station_id, to_station_id, usertype, gender, birthyear = row
            if cycling_id in cycling_ids:
                continue
            cycling_ids.append(cycling_id)
            cur.execute('''INSERT INTO cycling VALUES (?,?,?,?,?,?,?,?,?)''',
                        (cycling_id, start_time, end_time, duration, from_station_id, to_station_id, usertype, gender,
                         birthyear))
            con.commit()


if __name__ == '__main__':
    init_data(os.path.join('db.sqlite3'), os.path.join('data', 'station.csv'),
              os.path.join('data', 'chicago_data.csv'))
