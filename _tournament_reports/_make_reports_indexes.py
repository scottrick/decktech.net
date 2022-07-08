#!/usr/bin/env python3


import os
import frontmatter
from pprint import pprint
import re




def indexpage(filename, page_permalink, subpage_permalink, subpages, format_guide="Y/M/D", title=""):
  if title == "":
    title = "SW:CCG tournament reports"
  fh = open("../_tournament_reports_indexes/"+filename+".html", "w")
  fh.write("---\n")
  fh.write("layout: tournament_reports\n")
  fh.write("title: "+title+"\n")
  fh.write("permalink: "+page_permalink+"\n")
  fh.write("---\n")
  #fh.write("<h2>"+title+"</h2>\n")
  fh.write("<em>"+format_guide+"</em>\n")
  fh.write("<ul class='deck-index'>\n")
  for subpage in subpages:

    if type(subpage) == list:
      out = subpage_permalink + subpage
      out2 = out.replace("/starwarsccg/tournament-reports/", "")
      fh.write('<li><a href="' + out + '">' + out2 + "</a></li>\n")
    elif type(subpage) == dict:
      out = subpage_permalink + subpage["id"]
      fh.write('<li><a href="' + out + '">' + subpage["title"] + "</a></li>\n")
    elif type(subpage) == str:
      out = subpage_permalink + subpage
      out2 = out.replace("/starwarsccg/tournament-reports/", "").replace("articles/", "").replace("ratings/", "").replace("authors/", "").replace("sides/", "").replace("titles/", "").replace("handles/", "")
      fh.write('<li><a href="' + out + '">' + out2 + "</a></li>\n")
    else:
      print("UNKNOWN subpage TYPE: "+str(type(subpage)))
      print("  *",subpage)
      exit(1)

  fh.write("</ul>\n")

def frontmatter_parser(filename):
  fm = {}
  #f[11:].replace(".md", "")
  print("parsing frontmatter for: "+filename)
  fh = open(filename, "r")
  threelines = 0
  for lin in fh:
    lin = lin.replace("\n", "")
    if lin == "---":
      threelines = threelines + 1
      print("\n")
    else:
      lina = lin.split(":")
      if len(lina) > 1:
        print('['+lin+']['+lina[0].strip()+']['+lina[1].strip().replace("! ", "")+']')
    if threelines >= 2:
      return


fils = os.popen("find -type f -iname \*.html").read()

alldates = {}
alltitles = { "0":[],"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
allauthors = {"3":[], "a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
allhandles = {"1":[],"2":[],"3":[],"4":[],"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}


for f in fils.split("\n"):
  f = f.replace("./", "")
  if f != "":
    fs = f.split("/")
    if len(fs) > 1:
      y = fs[0]
      m = fs[1]
      d = fs[2]

      filename_without_path = f[11:] ## 2000-12-31-12619.html
      filename_without_date = filename_without_path[11:].replace(".html", "")
      filename_without_path_s = filename_without_path.replace(".html", "").split("-") ## 2000, 12, 31, 12619
      report_id = filename_without_date[-5:]

      print(report_id,len(filename_without_path_s),filename_without_path_s)

      report_url = "/starwarsccg/tournament-report/" + y +"/" + m + "/" + d + "/" + report_id
      ym = y+"/"+m
      ymd = y+"/"+m+"/"+d
      print("["+y+"]["+m+"]["+d+"]["+filename_without_path+"]:"+f)


      ##
      ## Load post details
      ##
      post = frontmatter.load(f)

      title = post['title']
      title = str(title).replace("’", "'")
      author = post['author'].replace('""', '"')

      description = ""
      if 'description' in post:
        description = post['description']

      rating = ""
      if 'rating' in post:
        rating = post['rating']

      handle1 = list(re.findall('.*"(.*)".*', author))
      print("handle1:",author,handle1,type(handle1))
      #if len(handle1)
      print("handle1[0]:",handle1[0])
      handle = handle1[0].replace("_", "").replace("-", "").replace("$", "").replace("@", "").replace(".", "").replace(",", "").strip()
      author1 = re.findall('(.*)"(.*)"(.*)', author)[0]
      print("author1:",author,author1,type(author1[0]), len(author1[0]))
      author = ( str(author1[0]) + " " + str(author1[2]) ).replace("   ", " ").replace("  ", " ")

      print("title:",title)
      print("author:",author)
      print("handle:",handle)
      print("description:",description)
      print("rating:",rating)

      t = ( title.replace("'", "").replace("’", "").replace(" ", "").replace("(", "").replace("[", "").replace("-", "").replace("~", "") )[0:1].lower()
      a = (str(author))[0:1].lower()
      r = (str(rating)).split(".")[0]
      h = (str(handle))[0:1].lower()

      article = "<span class='deck-rating'>" + str(rating) + \
                "</span> <span class='deck-title'>" + title + \
                "</span> by <span class='deck-author'>" + author + \
                "</span> (<span class='deck-handle'>"+handle+ \
                "</span>)<br /><span class='deck-description'>" + str(description) + \
                "</span>"

      print(t, a, r, h)


      ##
      ## Index by alphabet
      ##
      alltitles[t].append({"id":report_id, "title":article})
      allauthors[a].append({"id":report_id, "title":article})
      if handle != "":
        allhandles[h].append({"id":report_id, "title":article})

      ##
      ## Index by Date
      ##
      if y not in alldates:
        alldates[y] = {}
      if m not in alldates[y]:
        alldates[y][m] = {}
      if d not in alldates[y][m]:
        alldates[y][m][d] = []
      alldates[y][m][d].append({"id":report_id, "title":article}) #filename_without_path)




#indexpage("dates", "/starwarsccg/tournament_reports/index", list(alldates.keys()), "Years" )
for y in alldates:
  print(y)
  indexpage(y, "/starwarsccg/tournament-reports/"+y+"/", "/starwarsccg/tournament-reports/"+y+"/", list(alldates[y].keys()), "Y/M", y+" SW:CCG tournament_reports" )
  for m in alldates[y]:
    print(".."+m)
    indexpage(y+"_"+m, "/starwarsccg/tournament-reports/"+y+"/"+m+"/", "/starwarsccg/tournament-reports/"+y+"/"+m+"/", list(alldates[y][m].keys()), "Y/M/D", y+"-"+m+" SW:CCG tournament_reports" )
    for d in alldates[y][m]:
      print("...."+d)
      indexpage(y+"_"+m+"_"+d, "/starwarsccg/tournament-reports/"+y+"/"+m+"/"+d+"/", "/starwarsccg/tournament-report/"+y+"/"+m+"/"+d+"/", alldates[y][m][d], "Y/M/D/id", y+"-"+m+"-"+d+" SW:CCG tournament_reports")




print("titles:", list(alltitles.keys()))
indexpage("titles", "/starwarsccg/tournament-reports/"+"titles/", "/starwarsccg/tournament-reports/"+"titles/", list(alltitles.keys()), "[0-9a-z]", "SW:CCG tournament_reports by Titles")
for t in alltitles:
  indexpage("titles_"+t, "/starwarsccg/tournament-reports/"+"titles/"+t, "/starwarsccg/tournament-report/", alltitles[t], "[0-9a-z]", "SW:CCG tournament_reports where Title starts with "+t)

print("authors:", list(allauthors.keys()))
indexpage("authors", "/starwarsccg/tournament-reports/"+"authors/", "/starwarsccg/tournament-reports/"+"authors/", list(allauthors.keys()), "[0-9a-z]", "SW:CCG tournament_reports by Authors")
for a in allauthors:
  indexpage("authors_"+a, "/starwarsccg/tournament-reports/"+"authors/"+a, "/starwarsccg/tournament-report/", allauthors[a], "[0-9a-z]", "SW:CCG tournament_reports where Author starts with "+a)

print("handles:", list(allhandles.keys()))
indexpage("handles", "/starwarsccg/tournament-reports/"+"handles/", "/starwarsccg/tournament-reports/"+"handles/", list(allhandles.keys()), "[0-9a-z]", "SW:CCG tournament_reports by Handles")
for a in allauthors:
  indexpage("handles_"+a, "/starwarsccg/tournament-reports/"+"handles/"+a, "/starwarsccg/tournament-report/", allhandles[a], "[0-9a-z]", "SW:CCG tournament_reports where Handles starts with "+a)





