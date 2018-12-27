#! /bin/bash
#convert from GBK to UTF-8
#2014-09-24, by Ene
# update: 2018-12-27 - ene@xxiong.me

echo "Input Filename= "
read filename
iconv -f "gbk" -t "utf-8" < "$filename" > "$filename.tmp"
if [ $? -eq 0 ] 
then
mv "$filename" "$filename.backup"
mv "$filename.tmp" "$filename"
else
echo "Fail to convert."
fi
exit $?
