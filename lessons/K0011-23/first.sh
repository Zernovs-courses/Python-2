#!/bin/bash

# echo "Today is " `date`

# echo "\nenter th path to directory"
# read the_path

# echo -e "\n your path has the fillowing files and folders: "
# ls $the_path

# -------------------------------

# VARIABLES 

# country=Russia

# same_country=$country

# echo $country

# Examples:
# name
# count
# _var
# myVar
# MY_VAR

# -------------------------------

# INPUT AND OUTPUT

# read from terminal

# read the_path

# read from file

# while read line
# do
#     echo $line
# done < input.txt

# command line arguments

# передаются в скрипт под именами $1, $2, $3, ...

# echo "Hello, $1!"

# # output

# echo "Hello, world!"

# echo "this is some text" > output.txt # перезапись файла


# echo "this is some other text" >> output.txt # пишем в конец файла

# ls >> output.txt

# -------------------------------

# IF-ELSE

# if [[ condition ]];
# then
#     statement
# elif [[ condition ]]; then
#     statement
# else
#     statement
# fi

# echo "Please enter number: "
# read num

# if [ $num -gt 0 ]; then
#     echo "$num is positive"
# elif [ $num -lt 0 ]; then
#     echo "$num is negative"
# else
#     echo "$num is zero"
# fi

# and -a
# or -o

# -------------------------------

# LOOPS

# WHILE

# i=1
# while [ $i -le 10 ]; do
#     echo "$i"
#     i=$(( $i + 1 ))
# done

# FOR

# for i in 1 2 3 4 5
# do
#     echo "$i"
# done

# for i in {1..5}
# do
#     echo "$i"
# done

# for i in {0..10..2}
# do=0; i<=10; i
#     echo "$i"
# done

for (( i=0; i<=10; i++ ))
do
    echo $i
    if [ $i -eq 5 ]; then
        i = $(( 8 ))
    fi
done