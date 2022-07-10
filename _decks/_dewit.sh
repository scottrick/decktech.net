find 1999 2000 2001 2002 -type f -exec sed -i.bak 's/- Light/side: Light/' {} \;
find 1999 2000 2001 2002 -type f -exec sed -i.bak 's/- Dark/side: Dark/' {} \;
find 1999 2000 2001 2002 -type f -exec sed -i.bak 's/tags://' {} \;
