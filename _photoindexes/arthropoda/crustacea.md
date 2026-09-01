---
title: Photo index of crustaceans on Singapore shores
child_pages:
- label: "<a href=\"/photoindexes/arthropoda/crustacea/shrimp\">shrimps \n            and shrimp-like</a><br/>\n\
    \            prawns and lobsters"
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/redband/051105sisg2991m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/brevicarpalis/040411hntd0083m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/stomatopoda/spearer/020328cjd7903m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/lobster/glypturus/040521sntbd0067m.jpg
- label: "<a href=\"/photoindexes/arthropoda/crustacea/crab\">crabs \n            and crab-like</a><br/>\n"
  images:
  - url: https://images.naturehungry.sg/crustacea/crab/ocypodoidea/dotilla/041127cjd8656m.jpg
  - url: https://images.naturehungry.sg/crustacea/crab/portunidae/spinimana/031224sisd0115m.jpg
  - url: https://images.naturehungry.sg/crustacea/crab/matutidae/planipes/050511cftd3257m.jpg
  - url: https://images.naturehungry.sg/crustacea/crab/parthenopidae/common/050511cftg6313m.jpg
- label: "<a href=\"/photoindexes/arthropoda/crustacea/hermit\">hermit \n            crabs</a><br/>\n        \
    \    (crab-like animals <br/>\n            living in shells)"
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/anomura/hermit/coenobita/040523sjiad0014m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/anomura/hermit/lavender/041019lbdd7676m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/anomura/hermit/banded/050113sntg2834m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/anomura/hermit/orangespot/030617skdd0093m.jpg
- label: <a href="/photoindexes/arthropoda/crustacea/barnacles">barnacles</a>
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/ciriipedia/balanus/050510tusg6179m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/ciriipedia/euraphia/050413labg4662m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/ciriipedia/tetraclita/050427tmd2868m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/ciriipedia/lepas/040703sisd1824m.jpg
- label: "<a href=\"/photoindexes/arthropoda/crustacea/other\">other \n            crustaceans</a><br/>\n"
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/isopoda/ligia/041018sntd7570m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/amphipoda/amphipoda/050508kusg5881ma.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/ostracoda/ostracoda/050806skdg0510m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/isopoda/isopoda/110123sisd5267m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}

<hr/>
<h2>These are NOT crustaceans</h2>
<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Mangrove horseshoe crab" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Coastal horseshoe crab" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Marine spider" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Limpets" | first %}
{% include entry-summary-card.html item=entry %}
</div>