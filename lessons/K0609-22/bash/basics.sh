#!/bin/bash

# echo "Today is " `date`
#
# echo -e "\nenter the path to directory"
# read the_path
#
# echo -e "\nyour path has the following files and folders: "
# ls $the_path

# echo $1 $2 $3

# ---------------------------------------------------------

# # VARIABLES
#
# country=Russia
# county_full="Russian Federation"
#
# same_country=$country
#
# echo $country, $county_full, $same_country, country

# ---------------------------------------------------------

# READ

# read var
# echo $var
#
#
# while read line
# do 
#   echo $line 
# done < input.txt

# ---------------------------------------------------------

# ECHO

echo this is some output

echo -e "column1\tcolumn2\ntext\tvalue"


echo "New line from echo" > output.txt #запись в файл с начала файла
echo "One more line from echo" >> output.txt #запись в конец файла

ls >> output.txt
