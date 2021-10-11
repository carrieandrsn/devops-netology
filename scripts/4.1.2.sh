while ((1==1))
do
	curl http://localhost:80
	if (($? != 0))
	then
		date > ecurl.log
	fi
done