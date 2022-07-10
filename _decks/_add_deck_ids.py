#!/usr/bin/env python3


import os
import shutil

def frontmatter_updater(filename):
  fm = {}
  #f[11:].replace(".md", "")
  print("parsing frontmatter for: "+filename)
  shutil.copy(filename, filename+".old")
  fi = open(filename+".old", "r")
  fo = open(filename+"", "w")
  print("  * in.:",filename+".old")
  print("  * out:",filename+"")
  filename_without_path = f[11:] ## 2000-12-31-12619.md
  filename_without_path_s = filename_without_path.replace(".md", "").split("-") ## 2000, 12, 31, 12619
  deck_id = filename_without_path_s[3]
  print("  *",len(filename_without_path_s),filename_without_path_s)


  threelines = 0
  permalink_written = False
  for lin in fi:
    if lin.replace("\n", "") == "---":
      threelines = threelines + 1

    if threelines == 2:
      if not permalink_written:
        fo.write("id: "+deck_id+"\n")
        fo.write('permalink: "/starwarsccg/deck/'+str(deck_id)+'"'+"\n")
        permalink_written = True

    if threelines == 1:
      if lin.replace("\n", "").strip() != "":
        fo.write(lin)
    else:
      fo.write(lin)


exit(1)

fils = os.popen("find -type f -iname \*.md").read()
for f in fils.split("\n"):
  f = f.replace("./", "")
  if f != "":
    frontmatter_updater(f)



