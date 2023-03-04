#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from flask import Flask, render_template, make_response, request

app = Flask(__name__, template_folder='../templates', static_folder='../templates/static')


@app.route("/")
def home():
    """
    :return:
    """
    return render_template('home.html')


@app.route("/cycling/list")
def cycling_list():
    """
    :return:
    """
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    # 查询条件参数
    station_name = request.args.get('station_name', '')
    station_ids = None
    if station_name:
        with sqlite3.connect("db.sqlite3") as conn:
            cur = conn.cursor()
            cur.execute('''select id from station where station_name like '%{}%' '''.format(station_name))
            records = cur.fetchall()
            station_ids = [record[0] for record in records]

    if station_ids is not None:
        sql = "select * from cycling where from_station_id in ({0}) or to_station_id in ({0})".format(
            ','.join([str(station_id) for station_id in station_ids]))
    else:
        sql = "select * from cycling "
    sql += " limit {},{}".format(str((page - 1) * limit), str(limit))
    result = []
    with sqlite3.connect("db.sqlite3") as conn:
        cur = conn.cursor()
        cur.execute("select count(1) from cycling")
        total = cur.fetchone()[0]
        cur = conn.cursor()
        cur.execute(sql)
        records = list(cur.fetchall())
        for record in records:
            try:
                cur.execute("select station_name from station where id=?", (record[4],))
                from_station_name = cur.fetchone()[0]
            except Exception:
                from_station_name=""
            try:
                cur.execute("select station_name from station where id=?", (record[5],))
                to_station_name = cur.fetchone()[0]
            except Exception:
                to_station_name=""
            result.append({
                "id": record[0],
                "from_station_name": from_station_name,
                "to_station_name": to_station_name,
                "start_time": record[1],
                "end_time": record[2],
                "duration": record[3],
                "usertype": record[6],
                "gender": record[7],
                "birthyear": record[8]
            })

    return make_response({"code": 0, "data": result, "count": total})
