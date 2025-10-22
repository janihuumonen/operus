#!/bin/sh
src=a${1}.py
trg=A${1}_T{1,2,3,4,5,6,7}.py
if [ $# -eq 0 ] || [ ! -e $src ]; then
	echo "No argument OR $src does not exist!"
	exit 1
fi
for i in $trg; do
	if [ ! -e $i ]; then
		echo cp $src $i;
		cp $src $i;
	fi
done
echo 'Editing with vi:'
echo ' ma to mark a, d`a to delete from mark a to current position'
echo ' :n(ext) to edit next file, :args to list files'
echo ' :q! to quit without saving'
read
vi $trg
