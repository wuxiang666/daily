#!/bin/bash

hive -e "show tables;" > tables.txt

sleep 2

	cat tables.txt |while read eachline
	do
	hive -e "show create table $eachline" >>tablesDDL22.txt
	done
