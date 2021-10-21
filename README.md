# ESQR-EScaping-data-w-QR
escaping my shits with this fuckin QR code from a few meaningless annoying seperated networks

# Data Format
## Overview
Whole file will be sliced into several png(QRCode) files.
Each png piece contains about 2.8KB of data with following format.
> 1 Piece : header + content + footer
## Header
Header is for telling where the start point is, what content type is(t:text, b:binary), what file name is(FNAME), what size of piece is(PSIZE), which piece this piece is(rr:current state, nn:whole number of state).
> header example:
> ?st {t,b} FNAME PSIZE rr/nn
## Content
Content is content. if t mode its type is string. if b mode, it's binary.
## Footer
Footer is to tell where this piece ends, and also to tell sha1 hash of piece/whole file for error recognition.

# Requirements
only uses qrcode (& vanilla python)
> pip install qrcode

# Future Work
it could be used with any QRCode scanner like several apps in appstore,
but I prefer to make a specific reciever module to make easy to merge back files.
it might be contain auto scanning and error correcting functions if needed.

# Contact
email: soddokayo@gmail.com
