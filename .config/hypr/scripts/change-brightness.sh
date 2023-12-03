#!/bin/bash

map_brightness_to_hyphens() {
    local brightness="$1"
    local max_hyphens=20

    # Calculate the number of hyphens based on the brightness
    local num_hyphens=$(awk -v brightness="$brightness" -v max="$max_hyphens" 'BEGIN { print int(brightness / 100 * max) }')

    # Generate the hyphen string
    local hyphen_string=""
    for ((i = 0; i < num_hyphens; i++)); do
        hyphen_string+="━"
    done

    # Print the hyphens
    echo "$hyphen_string"
}

get_brightness_icon() {
    local brightness="$1"
    local mute="$2"

    # Convert brightness to integer (multiplying by 100 and then rounding)
    local brightness_int=$(echo "$brightness" | bc -l | xargs printf "%.0f")

    if [ "$brightness_int" -eq 100 ]; then
        echo "notification-display-brightness-full"
    elif [ "$brightness_int" -le 33 ]; then
        echo "notification-display-brightness-low"
    elif [ "$brightness_int" -le 67 ]; then
        echo "notification-display-brightness-medium"
    else
        echo "notification-display-brightness-high"
    fi
}

case $1 in
    --inc) 
        brillo -A 2
        shift
        ;;
    --dec) 
        brillo -U 2
        shift
        ;;
    *) 
        echo "Invalid argument: $1"
        exit 1
        ;;
esac

brightness=$(brillo -G)
dunstify -a changebrightness -i $(get_brightness_icon "$brightness" "$muted") -h string:x-dunst-stack-tag:changebrightness $(map_brightness_to_hyphens "$brightness")
