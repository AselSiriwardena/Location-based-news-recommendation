#!C:\Users\ASUS\Desktop\Location-based-news-reccomendation\Backend\venv\Scripts\python.exe
"""extract.py

     This file is part of libextractor.
     (C) 2002, 2003, 2004, 2005 Vidyut Samanta and Christian Grothoff

     libextractor is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published
     by the Free Software Foundation; either version 2, or (at your
     option) any later version.

     libextractor is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
     General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with libextractor; see the file COPYING.  If not, write to the
     Free Software Foundation, Inc., 59 Temple Place - Suite 330,
     Boston, MA 02111-1307, USA.

Little demo how to use the libextractor Python binding.

"""
import extractor
import sys

xtract = extractor.Extractor()
for arg in sys.argv[1:]:
    print "Keywords from %s:" % arg
    keys = xtract.extract(arg)
    for keyword_type, keyword in keys:
        print "%s - %s" % (keyword_type.encode('iso-8859-1'), keyword.encode('iso-8859-1'))
