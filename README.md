![DeckTech.net Archive](img/dechnet_archive.gif)

* Contents retrieved from archive.org for the old DeckTech.net website.
* Website built is a static content site.
* Static content built using Jekyll.


* Requires Ruby 3.0
* Install Jekyll using bundler:
```bash
bundle install
```
* Build the Jekyll site using bundler:
```bash
bundle exec jekyll build
```
* During development, use `jekyll build` for real-time updates to site:
```bash
bundle exec jekyll serve
```

## Generating the Index Pages

* The **Decks** and **Tournament Reports** are indexed dynamically by scripts within the `_decks` and `_tournament_reports`.
* The scripts are written in Python3.
* The scripts use the `python-frontmatter` module to parse the frontmatter for the decks and tournament reports.

```bash
pip3 install python-frontmatter

cd _decks
python3 _decks/_make_posts_indexes.py
cd ..
cd _tournament_reports
python3 _decks/_make_reports_indexes.py
cd ..

jekyll build
```


## Contributing other games from the DeckTech.net archives

* The SWCCG Player's Committee owns the DeckTech.net domain, which is why all the content currently hosted here is SWCCG focused.
* Any relevant old DeckTech.net content contributions will be accepted, be they from LOTR, ImagiNation, StarTrek, et. al., So long as the content used to exist on DeckTech.net, it is welcome here.


## Project History

* This project began with [Stephen Skilton pulling the DeckTech SWCCG decks and SWCCG tournament reports from archive.org](https://github.com/stevetotheizz0/decktech_archives).
* The SWCCG Player's Committee owns the DeckTech.net domain.
