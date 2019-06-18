for i in $(find . -maxdepth 1 -type d) ; do 	
    if [ (find $i -type f | wc -l) == 1 ]
    then
    	 echo -n $i": " ;
    fi
done