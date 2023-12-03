#!/bin/bash
# changeVolume

map_volume_to_hyphens() {
    local volume="$1"
    local max_hyphens=20

    # Calculate the number of hyphens based on the volume
    local num_hyphens=$(awk -v volume="$volume" -v max="$max_hyphens" 'BEGIN { print int(volume * max) }')

    # Generate the hyphen string
    local hyphen_string=""
    for ((i = 0; i < num_hyphens; i++)); do
        hyphen_string+="━"
    done

    # Print the hyphens
    echo "$hyphen_string"
}

get_volume_icon() {
    local volume="$1"
    local mute="$2"

    # Convert volume to integer (multiplying by 100 and then rounding)
    local volume_int=$(echo "$volume * 100" | bc -l | xargs printf "%.0f")

    if [ "$mute" = true ]; then
        echo "notification-audio-volume-muted"
    elif [ "$volume_int" -eq 0 ]; then
        echo "notification-audio-volume-off"
    elif [ "$volume_int" -le 33 ]; then
        echo "notification-audio-volume-low"
    elif [ "$volume_int" -le 67 ]; then
        echo "notification-audio-volume-medium"
    else
        echo "notification-audio-volume-high"
    fi
}

case $1 in
    --inc)
        wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 2%+
        shift
        ;;
    --dec)
        wpctl set-volume -l 1.0 @DEFAULT_AUDIO_SINK@ 2%-
        shift
        ;;
    --toggle)
        wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
        shift
        ;;
    *)
        echo "invalid argument: $1"
        exit 1
        ;;
esac

volume=$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -d " " -f 2)
muted=$([ "$(wpctl get-volume @DEFAULT_AUDIO_SINK@ | cut -d " " -f 3)" = "[MUTED]" ] && echo true || echo false)

dunstify -a changeVolume -i $(get_volume_icon "$volume" "$muted") -h string:x-dunst-stack-tag:changeVolume $(map_volume_to_hyphens "$volume")