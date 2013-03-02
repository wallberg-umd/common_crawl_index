#!/bin/bash -x

date=$(date +"%Y%m%d")

../bin/remote_read edu.umd. > ${date}-data.txt

./report.py < ${date}-data.txt > ${date}-report.txt

gzip --best ${date}-data.txt

