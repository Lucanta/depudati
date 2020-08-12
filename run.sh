#!/bin/sh

### CREATE SQL DATABASE IF DOES NOT EXIST
SQL_FILE='sql_db/ItalianPolls.db'
SQL_CREATE='create_tables.sql'
x=333

if [ -f "$SQL_FILE" ]; then
    echo "$SQL_FILE exist."
    sqlite3 "$SQL_FILE" < "$SQL_CREATE"
    sqlite3 ".quit"
else
    echo "$SQL_FILE does not exist."
    sqlite3 $SQL_FILE 
    sqlite3 $SQK_FILE < $SQL_CREATE
fi
