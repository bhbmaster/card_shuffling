#!/bin/bash

PY=python

function print_run_section() {
    echo "## $PY $1 ##"
    echo '```'
    $PY $1
    echo '```'
}

echo "# Example Output #"
echo
echo "output date: `date`"
echo
print_run_section "card.py"
echo
print_run_section "deck.py"
echo
print_run_section "analysis.py"