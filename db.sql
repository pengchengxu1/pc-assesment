
CREATE TABLE station(
   ID INT PRIMARY KEY     NOT NULL,
   station_name           TEXT    NOT NULL,
   station_lat            CHAR(50),
   station_lon        CHAR(50),
   station_type        CHAR(50)
);

CREATE TABLE cycling(
   ID INT PRIMARY KEY     NOT NULL,
   start_time          DATETIME,
   end_time            DATETIME,
   duration        INTEGER,
   from_station_id        INTEGER,
    to_station_id     INTEGER,
usertype  CHAR(50),
gender CHAR(50),
birthyear CHAR(50),
    FOREIGN KEY(from_station_id) REFERENCES station(id),
    FOREIGN KEY(to_station_id) REFERENCES station(id)
);