#!/bin/sh

mkdir -p ./ranking
mkdir -p ./js

./rank.sh
./matrix.py > js/matrix.js
./color.py > js/color.js
