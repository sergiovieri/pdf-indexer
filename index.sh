#!/bin/bash
pdf=$1
mkdir tmp
for ((i=1; i<=200; i++)); do
  let n=$i # page offset
  pdftotext -f $i -l $i $pdf "tmp/$n.txt" 
done
python3 index.py > out.txt 2> ignored.txt
rm -rf tmp
