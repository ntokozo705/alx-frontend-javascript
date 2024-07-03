#!/bin/bash

# Function to generate Pascal's Triangle
pascal_triangle() {
    local n=$1
    if [ $n -le 0 ]; then
        echo "[]"
        return
    fi

    # Initialize the first row
    local triangle=()
    triangle[0]="1"

    # Generate each row
    for (( i=1; i<n; i++ )); do
        local row="1"
        for (( j=1; j<i; j++ )); do
            local val=$(( $(echo ${triangle[$((i-1))]} | cut -d' ' -f$j) + $(echo ${triangle[$((i-1))]} | cut -d' ' -f$((j+1))) ))
            row+=" $val"
        done
        row+=" 1"
        triangle[i]=$row
    done

    # Print the triangle
    for (( i=0; i<n; i++ )); do
        echo ${triangle[$i]}
    done
}
