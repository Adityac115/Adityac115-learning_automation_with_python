#!/bin/bash
files=$(grep " jane " ../python/list.txt | cut -d' ' -f3)
for f in $files; do 
  if [ -e "$HOME$f" ]; then
    echo "$HOME$f" >> oldFiles.txt;
  fi
done