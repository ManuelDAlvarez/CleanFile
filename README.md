# CleanFile
This script finds all the first party URLs (or anything you want to look for) on a list of URLs. Input file is new-line separated

How to run it?
python CleanFile.py


What do you need to run it?

1. Update the line of code below and replace domain-x with the domain you are looking for. My use case is to find all the first party URLs but you can search for anything you want
  	if url_found.find("domain-x") != -1:

2. The script takes as an input a file, URLlist.txt, that must be placed on the same directory as the cript you are running. The list is comma separated. For example:

http://www.w3.org/2005/01/wai-rdf/GUIRoleTaxonomy

http://www.domain-x.com/

http://m-domain-x.com/

https://fonts.googleapis.com/css?family=XYZ


The ouptup is another file with a list of first party URLs
