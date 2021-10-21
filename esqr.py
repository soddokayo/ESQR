# esqr.py

import qrcode, sys, os

PSIZE = 1000

if len(sys.argv)==2:
	fin = open(sys.argv[1], "r", encoding="utf-8")
	txt = fin.read()
	
	path = sys.argv[1] + ".result"
	try:
		os.mkdir(path)
	except:
		pass
		
	# slice into n-letter pieces
	for i in range(0, len(txt), PSIZE):
		img = qrcode.make(txt[i:i+PSIZE])
		type(img)
		foname = path + "/" + str(i) + "-" + str(i+PSIZE) + ".png"
		img.save(foname)
else:
	print("Usage: python esqr.py [INPUT_FILENAME]")
