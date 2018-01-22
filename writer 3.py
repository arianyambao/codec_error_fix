# -*- coding: utf8 -*-
import re
import string

with open("to_edit.txt", encoding="ISO-8859-1") as files:
    writer=open("edited.txt", "w")
    for line in files:
        line = line.strip()
        line = re.sub(r"[^\x00-\x7F\u00C0-\u00FF]+",'', str(line))
        writer.write(line+"\n")
        #print(line)
    writer.close()

