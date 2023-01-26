#!/bin/bash

for file in *html.txt.txt; do
    name=$(basename "$file" .html.txt.txt)
    mv "$file" "$name.txt"
done