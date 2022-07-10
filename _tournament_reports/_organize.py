#!/usr/bin/env python3

import os
import shutil

for p in os.scandir(path='.'):
  if p.is_file():
    n = p.name
    # 2000-08-09-9272.md
    ns = n.split("-")
    if len(ns) > 1:
      y = ns[0]
      m = ns[1]
      d = ns[2]
      ym = y+"/"+m
      ymd = y+"/"+m+"/"+d
      print("["+y+"]["+m+"]["+d+"]: "+n)
      if not os.path.isdir(y):
        os.mkdir(y)
      if not os.path.isdir(ym):
        os.mkdir(ym)
      if not os.path.isdir(ymd):
        os.mkdir(ymd)
      shutil.move(n, ymd+"/"+n)

    #else:
    #  print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
    #  print(str(len(ns)),n)
    #  print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    #  exit(1)
