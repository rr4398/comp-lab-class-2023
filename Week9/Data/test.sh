#!/bin/bash
for ((i=4; i<=10; i++)); do
    float_num=$(echo "scale=1; $i / 10" | bc)
    echo $float_num
done

