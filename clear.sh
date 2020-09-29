#!/bin/bash
THETAS=thetas.csv
HOUSES=houses.csv
VIRTUAL_ENV=virtual_env

if [ "$VIRTUAL_ENV" ] ; then
	rm -rf virtual_env && echo "\033[32;3mvirtual_env deleted ✅\033[0m"
else
	echo "\033[31;3mvirtual_env does not exist\033[0m"
fi

if [ -f "$THETAS" ] ; then
	rm $THETAS && echo "\033[32;3mthetas.csv deleted ✅\033[0m"
else
	echo "\033[31;3mthetas.csv does not exist ❌\033[0m"
fi

if [ -f "$HOUSES" ] ; then
	rm $HOUSES && echo "\033[32;3mhouses.csv deleted ✅\033[0m"
else
	echo "\033[31;3mhouses.csv does not exist ❌\033[0m"
fi
