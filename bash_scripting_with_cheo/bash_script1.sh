#!/bin/bash
if [ $# -ne 2 ]; then
  echo "Usage: $0 <parameter1> <parameter1>"
  exit 1
fi

name=$1
apellido=$2

echo "Hola $1, tu apellido es $2"
