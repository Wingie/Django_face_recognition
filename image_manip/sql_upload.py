#!/usr/bin/env python
# -*- coding: utf-8 -*-


import MySQLdb as mdb
import sys
import glob
import os
import Image

def img(files):
    try:
        fileName, fileExtension = os.path.splitext(files)
        fin = open(files)
        img = fin.read()
    	fin.close()

    except IOError, e:

    	print "Error %d: %s" % (e.args[0],e.args[1])
    	sys.exit(1)

 
    try:
    	conn = mdb.connect(host='localhost',user='root',passwd='yanik88', db='dbname')
        cursor = conn.cursor()
    	cursor.execute("INSERT INTO image(image, image_name, extention) Values('%s', '%s', '%s')" % \
        	(mdb.escape_string(img), fileName, fileExtension))

    	conn.commit()
        print "Image Inserted:%s" % (files)
    	cursor.close()
    	conn.close()

    except mdb.Error, e:
  
    	print "Error %d: %s" % (e.args[0],e.args[1])
    	sys.exit(1)

os.chdir("img")
for files in glob.glob("*.*"):
    img(files)



