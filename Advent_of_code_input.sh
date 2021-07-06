#!bin/bash

YEAR=$1
DAY=$2

curl --cookie session=$(cat $HOME/advent_of_code/aocse) "https://adventofcode.com/$YEAR/day/$DAY/input"
