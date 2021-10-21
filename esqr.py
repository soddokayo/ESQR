# esqr.py

import sys, os
import qrcode
import hashlib

PSIZE = 900

if len(sys.argv)==2:
	FNAME = sys.argv[1].split('\\')[-1]
	print(sys.argv[1], FNAME)
	
	fin = open(sys.argv[1], "r", encoding="utf-8")
	txt = fin.read()
	
	path = FNAME + ".result"
	try:
		os.mkdir(path)
	except:
		pass
		
	# slice into PSIZE-letter pieces
	nn = int(len(txt)/PSIZE) + 1
	sha1_hasher = hashlib.sha1()
	sha1_hasher.update(txt.encode())
	f_hash = sha1_hasher.hexdigest()
	for i in range(0, len(txt), PSIZE):
		rr = int(i/PSIZE) + 1

		# header : text/binary, filename, psize, progress		
		header = "?st t " + FNAME + " " + str(PSIZE) + " "\
		+ str(rr) + "/" + str(nn) + "\n"
			
		# content : sliced PSIZE-letter data
		content = txt[i:i+PSIZE]
		
		# footer : sha1 hash of piece/file
		sha1_hasher = hashlib.sha1()
		sha1_hasher.update(content.encode())
		p_hash = sha1_hasher.hexdigest()
		footer = "\n" + "?ed p " + str(p_hash)

		if rr == nn:
			footer += "\n" + "?ed f " + str(f_hash)

		buf = header + content + footer
	
		print("\n===\n" + "processing " + str(rr) + "/" + str(nn))
		print("\n" + buf)
		
		enc_img = qrcode.make(buf)
		fo_name = path + "/" + str(i) + "-" + str(i+PSIZE) + ".png"
		enc_img.save(fo_name)
else:
	print("Usage: python esqr.py [INPUT_FILENAME]")
