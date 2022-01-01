#!/bin/bash

PY=python

echo "output date: `date`"
echo '# card.py'
echo '```'
$PY card.py
echo '```'
echo 
echo '# deck.py'
echo '```'
$PY deck.py
echo '```'
echo 
echo '# analysis.py'
echo '```'
$PY analysis.py
echo '```'
