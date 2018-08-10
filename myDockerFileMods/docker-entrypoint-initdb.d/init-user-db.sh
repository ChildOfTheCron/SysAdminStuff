#!/bin/bash
set -e

#psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
#    CREATE USER docker;
#    CREATE DATABASE docker;
#    GRANT ALL PRIVILEGES ON DATABASE docker TO docker;
#EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
CREATE TABLE appIdTable (
	appid 	int PRIMARY KEY,
	productname 	varchar(250),
	discount	varchar(250)
);
CREATE GROUP restgroup;
CREATE USER restbot WITH PASSWORD 'resty';
ALTER ROLE restgroup LOGIN;
ALTER GROUP restgroup ADD USER restbot;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" postgres < /appidlist.sql 
