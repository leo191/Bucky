#!/bin/bash

pipexec=$(which pip)
pip3exec=$(which pip3)
$pipexec freeze | grep $1 > /dev/null 2>&1
if $( $pipexec freeze | grep $1 > /dev/null 2>&1 ) || $( $pip3exec freeze | grep $1 > /dev/null 2>&1 )
then
    exit 0
else
    exit 1
fi
