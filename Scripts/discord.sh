#!/usr/bin/bash

discord & disown

PPPID=$(awk '{print $4}' "/proc/$PPID/stat")
kill $PPPID
