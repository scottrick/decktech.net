#!/usr/bin/env python3


import os
import frontmatter
from pprint import pprint
import re




def indexpage(filename, page_permalink, subpage_permalink, subpages, format_guide="Y/M/D", title=""):
  if title == "":
    title = "SW:CCG Decks"
  fh = open("../_decks_indexes/"+filename+".html", "w")
  fh.write("---\n")
  fh.write("layout: decks\n")
  fh.write("title: "+title+"\n")
  fh.write("permalink: "+page_permalink+"\n")
  fh.write("---\n")
  #fh.write("<h2>"+title+"</h2>\n")
  fh.write("<em>"+format_guide+"</em>\n")
  fh.write("<ul class='deck-index'>\n")
  for subpage in subpages:

    if type(subpage) == list:
      out = subpage_permalink + subpage
      out2 = out.replace("/starwarsccg/decks/", "")
      fh.write('<li><a href="' + out + '">' + out2 + "</a></li>\n")
    elif type(subpage) == dict:
      out = subpage_permalink + subpage["id"]
      fh.write('<li><a href="' + out + '">' + subpage["title"] + "</a></li>\n")
    elif type(subpage) == str:
      out = subpage_permalink + subpage
      out2 = out.replace("/starwarsccg/decks/", "").replace("articles/", "").replace("ratings/", "").replace("authors/", "").replace("sides/", "").replace("titles/", "").replace("handles/", "")
      fh.write('<li><a href="' + out + '">' + out2 + "</a></li>\n")
    else:
      print("UNKNOWN subpage TYPE: "+str(type(subpage)))
      print("  *",subpage)
      exit(1)

  fh.write("</ul>\n")

def frontmatter_parser(filename):
  fm = {}
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


fils = os.popen("find -type f").read()

alldates = {}
alltitles = { "1":[],"2":[],"3":[],"4":[],"6":[],"7":[],"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
allauthors = {"3":[], "a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
allhandles = {"1":[],"2":[],"3":[],"4":[],"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
allratings = {"0":[], "1":[],"2":[],"3":[],"4":[],"5":[]} #,"6":[],"7":[],"8":[],"9":[],"10":[]}
allsides = {"light":[], "dark":[]}

for f in fils.split("\n"):
  f = f.replace("./", "")
  if f != "":
    fs = f.split("/")
    if len(fs) > 1:
      y = fs[0]
      m = fs[1]
      d = fs[2]
      filename_without_path = f[11:] ## 2000-12-31-12619.md
      filename_without_path_s = filename_without_path.replace(".md", "").split("-") ## 2000, 12, 31, 12619
      print(len(filename_without_path_s),filename_without_path_s)
      if len(filename_without_path_s) < 3:
        print("!!!!!!!!!!!!!!!!!!!!")
        print("Filename shorter than expected")
        print("!!!!!!!!!!!!!!!!!!!!")
        print(y,m,d)
        print(f)
        print(fs)
        print(filename_without_path)
        print(filename_without_path_s)
        print("!!!!!!!!!!!!!!!!!!!!")
      else:
        deck_id = filename_without_path_s[3]
        deck_url = "/starwarsccg/deck/" + deck_id
        ym = y+"/"+m
        ymd = y+"/"+m+"/"+d
        print("["+y+"]["+m+"]["+d+"]["+filename_without_path+"]:"+f)


      ##
      ## Load post details
      ##
      post = frontmatter.load(f)

      if 'side' in post:
        s = post['side'].lower()
      else:
        print("\n\n!!!!!!!!!!!!!!!!!!!!!!!\n")
        print("side missing from frontmatter")
        print(f)
        print("\n\n!!!!!!!!!!!!!!!!!!!!!!!\n")
        pprint(post.metadata)
        print("\n!!!!!!!!!!!!!!!!!!!!!!!\n\n")
        exit(1)

      title = post['title']
      title = str(title).replace("’", "'")
      author = post['author'].replace('""', '"')

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
      print("description:",post['description'])
      print("rating:",post['rating'])
      print("side:",post['side'])

      t = ( title.replace("'", "").replace("’", "").replace(" ", "").replace("(", "").replace("[", "").replace("-", "").replace("~", "") )[0:1].lower()
      a = (str(author))[0:1].lower()
      r = (str(post['rating'])).split(".")[0]
      h = (str(handle))[0:1].lower()

      article = "<span class='deck-rating'>" + str(post['rating']) + \
                "</span> (<span class='deck-side'>" + str(post['side']) + \
                " Side</span>) <span class='deck-title'>" + title + \
                "</span> by <span class='deck-author'>" + author + \
                "</span> (<span class='deck-handle'>"+handle+ \
                "</span>)<br /><span class='deck-description'>" + str(post['description']) + \
                "</span>"

      print(t, a, r, s, h)


      ##
      ## Index by alphabet
      ##
      alltitles[t].append({"id":deck_id, "title":article})
      allauthors[a].append({"id":deck_id, "title":article})
      allratings[r].append({"id":deck_id, "title":article})
      allsides[s].append({"id":deck_id, "title":article})
      if handle != "":
        allhandles[h].append({"id":deck_id, "title":article})

      ##
      ## Index by Date
      ##
      if y not in alldates:
        alldates[y] = {}
      if m not in alldates[y]:
        alldates[y][m] = {}
      if d not in alldates[y][m]:
        alldates[y][m][d] = []
      alldates[y][m][d].append({"id":deck_id, "title":article}) #filename_without_path)




#indexpage("dates", "/starwarsccg/decks/index", list(alldates.keys()), "Years" )
for y in alldates:
  print(y)
  indexpage(y, "/starwarsccg/decks/"+y+"/", "/starwarsccg/decks/"+y+"/", list(alldates[y].keys()), "Y/M", y+" SW:CCG Decks" )
  for m in alldates[y]:
    print(".."+m)
    indexpage(y+"_"+m, "/starwarsccg/decks/"+y+"/"+m+"/", "/starwarsccg/decks/"+y+"/"+m+"/", list(alldates[y][m].keys()), "Y/M/D", y+"-"+m+" SW:CCG Decks" )
    for d in alldates[y][m]:
      print("...."+d)
      indexpage(y+"_"+m+"_"+d, "/starwarsccg/decks/"+y+"/"+m+"/"+d+"/", "/starwarsccg/decks/"+y+"/"+m+"/"+d+"/", alldates[y][m][d], "Y/M/D/id", y+"-"+m+"-"+d+" SW:CCG Decks")




print("titles:", list(alltitles.keys()))
indexpage("titles", "/starwarsccg/decks/"+"titles/", "/starwarsccg/decks/"+"titles/", list(alltitles.keys()), "[0-9a-z]", "SW:CCG Decks by Titles")
for t in alltitles:
  indexpage("titles_"+t, "/starwarsccg/decks/"+"titles/"+t, "/starwarsccg/deck/", alltitles[t], "[0-9a-z]", "SW:CCG Decks where Title starts with "+t)

print("authors:", list(allauthors.keys()))
indexpage("authors", "/starwarsccg/decks/"+"authors/", "/starwarsccg/decks/"+"authors/", list(allauthors.keys()), "[0-9a-z]", "SW:CCG Decks by Authors")
for a in allauthors:
  indexpage("authors_"+a, "/starwarsccg/decks/"+"authors/"+a, "/starwarsccg/deck/", allauthors[a], "[0-9a-z]", "SW:CCG Decks where Author starts with "+a)

print("ratings:", list(allratings.keys()))
indexpage("ratings", "/starwarsccg/decks/"+"ratings/", "/starwarsccg/decks/"+"ratings/", list(allratings.keys()), "[0-9a-z]", "SW:CCG Decks by Rating")
for r in allratings:
  indexpage("ratings_"+r, "/starwarsccg/decks/"+"ratings/"+r, "/starwarsccg/deck/", allratings[r], "[0-9a-z]", "SW:CCG Decks with Rating "+r)

print("sides:", list(allsides.keys()))
indexpage("sides", "/starwarsccg/decks/"+"sides/", "/starwarsccg/decks/"+"sides/", list(allsides.keys()), "[0-9a-z]", "SW:CCG Decks by Side of The Force")
for s in allsides:
  indexpage("sides_"+s, "/starwarsccg/decks/"+"sides/"+s, "/starwarsccg/deck/", allsides[s], "[0-9a-z]", "SW:CCG "+s+" Side of The Force Decks")

print("handles:", list(allhandles.keys()))
indexpage("handles", "/starwarsccg/decks/"+"handles/", "/starwarsccg/decks/"+"handles/", list(allhandles.keys()), "[0-9a-z]", "SW:CCG Decks by Handles")
for a in allauthors:
  indexpage("handles_"+a, "/starwarsccg/decks/"+"handles/"+a, "/starwarsccg/deck/", allhandles[a], "[0-9a-z]", "SW:CCG Decks where Handles starts with "+a)





