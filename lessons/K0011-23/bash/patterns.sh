#!/bin/bash

# GLOB

#  * - любая строка, включая пустую строку
#  ? - любой единичный символ
#  [...] - любой символ из скобок 


# glob: */bin
# foo/bin + 
# /usr/foo/bin -

filename="some.jpg"
if [[ $filename = *.jpg || $filename = *.jpeg ]]; then
    echo "$filename is a jpeg"
fi

# EXTENDED GLOB

# ?(list) - 0 или 1 совпадание
# *(list) - 0 или больше совпадений
# +(list) - 1 или больше
# @(list) - один из данных паттерном
# !(list) - все, кроме указанных паттернов

# можем разделять список внутри скобок символом |

# REGULAR EXPRESSIONS (regex)

str="Hello, world"
r='*,'
if [[ $str =~ $r ]]; then
    echo match
else
    echo not match
fi

# .*[]^${}\+?|() - метасимволы

# якорные символы

^ - привязывает шаблон к началу строки

echo "welcome to sirius" | awk '/^sirius/{print $0}'
echo "sirius college" | awk '/^sirius/{print $0}'

$ - привязывает шаблон к концу строки

echo "welcome to sirius" | awk '/sirius$/{print $0}'
echo "sirius college" | awk '/sirius$/{print $0}'

awk '/^this is a test$/'

'^$' - поиск пустой строки

