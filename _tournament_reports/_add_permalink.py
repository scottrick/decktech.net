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
  filename_without_path = f[11:] ## 2000-12-31-12619.html
  filename_without_date = filename_without_path[11:].replace(".html", "")
  filename_without_path_s = filename_without_path.replace(".html", "").split("-") ## 2000, 12, 31, 12619
  y = filename_without_path_s[0]
  m = filename_without_path_s[1]
  d = filename_without_path_s[2]
  report_id = filename_without_date[-5:]
  permalink = "/starwarsccg/tournament-report/"+y+"/"+m+"/"+d+"/"+report_id
  print("  *",filename_without_path)
  print("  *",filename_without_date)
  print("  *",len(filename_without_path_s),filename_without_path_s)
  print("  *",permalink)
  print()

  threelines = 0
  permalink_written = False
  for lin in fi:
    if lin.replace("\n", "") == "---":
      threelines = threelines + 1

    if threelines == 2:
      if not permalink_written:
        fo.write("id: "+report_id+"\n")
        fo.write('permalink: "'+permalink+'"'+"\n")
        permalink_written = True

    if threelines == 1:
      if lin.replace("\n", "").strip() != "":
        fo.write(lin)
    else:
      fo.write(lin)


exit(1)

fils = os.popen("find -type f -iname \*.html").read()
for f in fils.split("\n"):
  f = f.replace("./", "")
  if f != "":
    print(f)
    frontmatter_updater(f)



