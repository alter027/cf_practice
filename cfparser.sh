
# echo "Start!"

filename=cf_$1.txt
# echo $filename
mkdir $1
cat $filename | while read line 
do
    name=$(echo $line | sed 's/[ \r$]//g')
    # echo $name
    python3 cfparser.py $line > $1/$name
    # do something with $line here
done
