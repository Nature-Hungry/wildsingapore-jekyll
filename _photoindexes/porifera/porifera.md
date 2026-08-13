---
title: Photo index of sponges on Singapore shores
child_pages:
- label: "<a href=\"../branching\">branching \n            or lumpy</a>"
  images:
  - url: https://images.naturehungry.sg/porifera/branchblack/050806skdd5505m.jpg
  - url: https://images.naturehungry.sg/porifera/sprawlorange/041214smkd8859m.jpg
  - url: https://images.naturehungry.sg/porifera/chocolate/050509hntd3170m.jpg
  - url: https://images.naturehungry.sg/porifera/lumpypink/050709skdg9251m.jpg
- label: <a href="../encrusting">encrusting</a>
  images:
  - url: https://images.naturehungry.sg/porifera/spatula/050413labg4698m.jpg
  - url: https://images.naturehungry.sg/porifera/smoothblue/050808sntg0856m.jpg
  - url: https://images.naturehungry.sg/porifera/meltedchoc/080522cjd5881m.jpg
  - url: https://images.naturehungry.sg/porifera/encrustprickly/051204sisg3279m.jpg
- label: "<a href=\"../ball\">balls, \n            vases</a>"
  images:
  - url: https://images.naturehungry.sg/porifera/potyellow/050312hntg3326m.jpg
  - url: https://images.naturehungry.sg/porifera/../echinodermata/ophiuroidea/tinysponge/050623cjg8307m.jpg
  - url: https://images.naturehungry.sg/porifera/xestospongia/050510tusg6111m.jpg
  - url: https://images.naturehungry.sg/porifera/ballprickly/040803tusd3982m.jpg
- label: "<a href=\"../other\">other \n            shapes</a>"
  images:
  - url: https://images.naturehungry.sg/porifera/oceanapia/050526cjg6896m.jpg
  - url: https://images.naturehungry.sg/porifera/horn/050526cjg6829m.jpg
  - url: https://images.naturehungry.sg/porifera/coelocarteria/050309smkd1532m.jpg
  - url: https://images.naturehungry.sg/porifera/manyconed/101106burs00338m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}


<h2>These lifeforms are not sponges</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Thumbs-up sea squirt" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Yellow clustered bead ascidians" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Rock slime ascidian" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Encrusting coralline red seaweed" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Puffy brown seaweed" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Bubble green seaweed" | first %}
{% include entry-summary-card.html item=entry %}
</div>