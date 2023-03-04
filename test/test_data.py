#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import os
import requests
import unittest
from init_data import init_data


class Test_Init_Data(unittest.TestCase):
    def test_init_cycling(self):
        init_data(os.path.abspath('../db.sqlite3'), os.path.abspath('../data/station.csv'),
                  os.path.abspath('../data/chicago_data.csv'))
        con = sqlite3.connect(os.path.abspath('../db.sqlite3'))
        cur = con.cursor()
        cur.execute('select count(1) from cycling')

        self.assertEqual(cur.fetchone()[0], 6317)

    def test_init_station(self):
        init_data(os.path.abspath('../db.sqlite3'), os.path.abspath('../data/station.csv'),
                  os.path.abspath('../data/chicago_data.csv'))
        con = sqlite3.connect(os.path.abspath('../db.sqlite3'))
        cur = con.cursor()
        cur.execute('select count(1) from station')
        self.assertEqual(cur.fetchone()[0], 595)


class Test_Interface(unittest.TestCase):
    def test_home(self):
        url = 'http://127.0.0.1:5000/'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

    def test_list(self):
        url = 'http://127.0.0.1:5000/cycling/list?page=1&limit=10'
        res = requests.get(url)
        data = res.json()
        self.assertEqual(data, {'code': 0, 'count': 6317, 'data': [
            {'birthyear': '1994', 'duration': 990, 'end_time': '2019/7/24 23:15',
             'from_station_name': 'Lincoln Ave & Belle Plaine Ave', 'gender': 'Male', 'id': 23946925,
             'start_time': '2019/7/24 22:58', 'to_station_name': 'Clark St & Winnemac Ave', 'usertype': 'Subscriber'},
            {'birthyear': '1988', 'duration': 488, 'end_time': '2019/7/24 23:06',
             'from_station_name': 'Pine Grove Ave & Waveland Ave', 'gender': 'Male', 'id': 23946926,
             'start_time': '2019/7/24 22:58', 'to_station_name': 'Wilton Ave & Belmont Ave', 'usertype': 'Subscriber'},
            {'birthyear': '', 'duration': 1037, 'end_time': '2019/7/24 23:15',
             'from_station_name': 'Lincoln Ave & Belle Plaine Ave', 'gender': 'Male', 'id': 23946927,
             'start_time': '2019/7/24 22:58', 'to_station_name': 'Racine Ave & Fullerton Ave',
             'usertype': 'Subscriber'}, {'birthyear': '', 'duration': 3544, 'end_time': '2019/7/24 23:57',
                                         'from_station_name': 'Green St & Madison St', 'gender': '', 'id': 23946928,
                                         'start_time': '2019/7/24 22:58', 'to_station_name': 'Kingsbury St & Kinzie St',
                                         'usertype': 'Customer'},
            {'birthyear': '1995', 'duration': 964, 'end_time': '2019/7/24 23:14',
             'from_station_name': 'Lincoln Ave & Belle Plaine Ave', 'gender': 'Female', 'id': 23946930,
             'start_time': '2019/7/24 22:58', 'to_station_name': 'Clark St & Winnemac Ave', 'usertype': 'Subscriber'},
            {'birthyear': '', 'duration': 1224, 'end_time': '2019/7/24 23:19', 'from_station_name': 'Wells St & Elm St',
             'gender': '', 'id': 23946931, 'start_time': '2019/7/24 22:59', 'to_station_name': '',
             'usertype': 'Customer'}, {'birthyear': '', 'duration': 1301, 'end_time': '2019/7/24 23:20',
                                       'from_station_name': 'Wells St & Concord Ln', 'gender': 'Male', 'id': 23946932,
                                       'start_time': '2019/7/24 22:59',
                                       'to_station_name': 'Winchester Ave & Elston Ave', 'usertype': 'Customer'},
            {'birthyear': '1983', 'duration': 431, 'end_time': '2019/7/24 23:06',
             'from_station_name': 'State St & 19th St', 'gender': 'Male', 'id': 23946933,
             'start_time': '2019/7/24 22:59', 'to_station_name': 'Calumet Ave & 21st St', 'usertype': 'Subscriber'},
            {'birthyear': '1992', 'duration': 431, 'end_time': '2019/7/24 23:06',
             'from_station_name': 'Dearborn Pkwy & Delaware Pl', 'gender': 'Male', 'id': 23946934,
             'start_time': '2019/7/24 22:59', 'to_station_name': 'Clybourn Ave & Division St',
             'usertype': 'Subscriber'}, {'birthyear': '', 'duration': 1116, 'end_time': '2019/7/24 23:18',
                                         'from_station_name': 'Clark St & Schiller St', 'gender': 'Male',
                                         'id': 23946935, 'start_time': '2019/7/24 22:59',
                                         'to_station_name': 'Greenview Ave & Fullerton Ave',
                                         'usertype': 'Subscriber'}]})


if __name__ == '__main__':
    unittest.main()
