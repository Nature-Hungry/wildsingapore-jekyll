---
title: Bivalves
child_pages:
- label: "<a href=\"small\">small \n            clams</a> <br/>\n      \
    \      (less than 8cm) "
  images:
  - url: https://images.naturehungry.sg/mollusca/bivalvia/veneridae/forked/070323skdg8233m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/mytilidae/viridis/031207cjd0034m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/arcidae/anadara/020710chgd1615m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/veneridae/ribbed/070204hntg7547m.jpg
- label: "<a href=\"large\">large \n            clams</a> <br/>\n      \
    \      (8cm and more)"
  images:
  - url: https://images.naturehungry.sg/mollusca/bivalvia/pinnidae/pinnidae/050511cftg6307ma.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/tridacnidae/squamosa/040123sisd0129m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/tridacnidae/crocea/050312hntg3342m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/placunidae/placuna/050609cftg7550m.jpg
- label: "<a href=\"odd\">odd-shaped \n            clams</a>"
  images:
  - url: https://images.naturehungry.sg/mollusca/bivalvia/cardiidae/cardissa/050918smkg2708m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/solenidae/solenidae/040120cjd0014m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/pteriidae/pteriidae/050724bbd5353m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/clavagellidae/brechites/070702chgg0937m.jpg
- label: "<a href=\"stuck\">clams \n            with one side stuck</a>\
    \ <br/>\n            to a rock or other hard surface"
  images:
  - url: https://images.naturehungry.sg/mollusca/bivalvia/ostreidae/saccostrea/030814skdd0217m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/ostreidae/plain/041031cjd7933m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/anomiidae/understone/020616cjd0734m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/ostreidae/zigzag/050611kusd3993ma.jpg
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


<h2>These are NOT bivalves</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Limpets" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Slipper snails" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Barnacles" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Hoof-shield limpet" | first %}
{% include entry-summary-card.html item=entry %}
</div>