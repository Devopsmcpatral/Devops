#!/bin/bash

x=20

check_variable() {
  local var="$1"
  local value="$2"
 
  if [[ -n "$value" ]]; then
    echo "La variable '$var' está configurada y no está vacía"
    
    if [[ "$value" -eq 20 ]]; then
      echo "La variable '$var' tiene el valor 20"
    else
      echo "La variable '$var' no tiene el valor 20"
    fi
  else
    echo "La variable '$var' no está configurada o está vacía"
  fi
}

check_variable "x" "$x"