echo "Checking/making today's data folder"
RANDOM=2
DATA_FOLDER="./data/$RANDOM"
if [ -d ${DATA_FOLDER} ]; then
	echo "Data already exists, skipping download"
else	
	mkdir -p $DATA_FOLDER
	echo "Downloading data"
	# grab 50 arbitrary json files from json generator
	for i in {0..2}
	do
		echo "Downloading file number $i"
		curl -s https://next.json-generator.com/api/json/get/Vy7eluVOK -o "$DATA_FOLDER/data-${i}.json"
	done
fi