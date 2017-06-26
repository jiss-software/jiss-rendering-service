#!/usr/bin/env bash

printf "\e[1mBUILDING jiss/rendering-service version ${1:-local}...\e[0m\n"

docker build -t jiss/rendering-service:${1:-local} . || {
    printf "\e[31mDOCKER IMAGE BUILD FAIL!\e[0m\n" 1>&2
    exit 1;
}

printf "\e[1mDOCKER IMAGE BUILD DONE.\e[0m\n"