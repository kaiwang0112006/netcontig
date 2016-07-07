# netcontig

Build a net of contig and find the shortest path. Please see the examples input and output format


script path on server
---------
/public/scripts/kw/netcontig/contigpath.py

Usage
---------

	$ python src/contigpath.py -h
	
	usage: contigpath.py [-h] --input INPUT --start START --end END [--out OUTPUT]
	
	python *.py [option]
	
	optional arguments:
	
	  -h, --help     show this help message and exit
	
	  --out OUTPUT   output file
	
	required arguments:
	
	  --input INPUT  input file to insert into DB,required
	
	  --start START  start nodes file
	
	  --end END      end nodes file


    $ python contigpath.py  --input=/public/share/hldu/R498_Final_Final_Ref/R498_Analysis/R498_Pacbio_Self/Graph/Start_End.txt --start=start.txt --end=end.txt
