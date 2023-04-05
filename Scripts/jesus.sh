#!/bin/bash

arr=()
input="/home/maciej/Dokumenty/Smieci/jesus.txt"
RANDOM=$$$(date +%s)

select_random() {
    printf "%s\0" "$@" | shuf -z -n1 | tr -d '\0'
}

while IFS= read -r line
do
  arr+=("${line}")
done < "$input"


selectedexpression=$(select_random "${arr[@]}")
echo "$selectedexpression" | tr -d '\n'
