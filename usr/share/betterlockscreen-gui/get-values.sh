#!/bin/bash
USER_CONF="$HOME/.config/betterlockscreenrc"

# If there is no config file, create it
if [ ! -f $USER_CONF ]; then
    echo "# betterlockscreenrc\nblur_level=0\ndim_level=0" > $USER_CONF
fi 

while getopts "bd" opt; do
    case $opt in
        b) VAL="blur_level";;
        d) VAL="dim_level";;
        *) exit 1;;
    esac
done

# First try, check if variable exist at config
ORIGINAL_VALUE=$(cat $USER_CONF | grep $VAL)
[ $? -ne 0 ] && echo "$VAL=0" >> $USER_CONF
# Get config value
ORIGINAL_VALUE=$(cat $USER_CONF | grep $VAL | cut -d"=" -f2)

# Check if variable is empty
if [ "$ORIGINAL_VALUE" = "" ]; then
    sed -i 's|'"$VAL"'=.*|'"$VAL"'=0|g' $USER_CONF
fi

# Check if variable contents is really a number
number_regex="^[+-]?[0-9]+([.][0-9]+)?$"
echo $ORIGINAL_VALUE | grep -qP ${number_regex}
isnumber=$?

if [ ${isnumber} -ne 0 ]; then
    sed -i 's|'"$VAL"'=.*|'"$VAL"'=0|g' $USER_CONF; ORIGINAL_VALUE=0; 
fi

if [ $VAL = "blur_level" ]; then

# It doesn't make sense to have blur above 100%
# But if the user did the mistake of put the value in a <= 100 format, correct them

   if (( $(echo "$ORIGINAL_VALUE > 1.00" | bc -l) )); then
        if (( $(echo "$ORIGINAL_VALUE > 0 <= 100.00" | bc -l) )); then
            FILE_VALUE=$ORIGINAL_VALUE
            ORIGINAL_VALUE=$(echo "scale=2; $FILE_VALUE / 100" | bc -l | sed -e 's/^-\./-0./' -e 's/^\./0./')
            sed -i 's|'"$VAL"'='"$FILE_VALUE"'|'"$VAL"'='"$ORIGINAL_VALUE"'|g' $USER_CONF
            GUI_VALUE=$FILE_VALUE
        fi

    # If, for some reason, there is a negative number on config, revert to defaults
    elif (( $(echo "$ORIGINAL_VALUE < 0" | bc -l) )); then
            GUI_VALUE=0
            sed -i 's|'"$VAL"'='"$ORIGINAL_VALUE"'|'"$VAL"'=0|g' $USER_CONF
     
    else
        # GUI uses integer values, so we need to convert the float into integer.
        GUI_VALUE=$(echo ";$ORIGINAL_VALUE * 100" | bc -l | cut -d"." -f1)
    fi

elif [ $VAL = "dim_level" ]; then
    GUI_VALUE=$ORIGINAL_VALUE

# Dim at 100% is black, so it doesn't make sense a value above that.
    if (( $(echo "$GUI_VALUE > 100" | bc -l) )); then
        GUI_VALUE=100
        sed -i 's|'"$VAL"'='"$ORIGINAL_VALUE"'|'"$VAL"'='"$GUI_VALUE"'|g' $USER_CONF
    elif (( $(echo "$GUI_VALUE < 0" | bc -l) )); then
        GUI_VALUE=0
        sed -i 's|'"$VAL"'='"$ORIGINAL_VALUE"'|'"$VAL"'=0|g' $USER_CONF
    fi

else
    echo "Invalid option"
fi

echo $GUI_VALUE
