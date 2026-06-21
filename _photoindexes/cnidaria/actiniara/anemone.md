---
title: "Sea anemones and anemone-like animals"
description: "Fact sheet with photos on flora and fauna of Singapore's intertidal shores"
keywords: "photo, index, actiniaria, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
coverimgs:
- https://images.naturehungry.sg/cnidaria/others/zoanthid/zoanthus/040828skdd5545ma.jpg
- https://live.staticflickr.com/65535/51397335434_46fe365f82_m.jpg
- https://live.staticflickr.com/2902/14364258483_1d5b79510e_m.jpg
- https://live.staticflickr.com/65535/50350364478_e6cdfa8d26_m.jpg
- https://live.staticflickr.com/1772/42236481640_0f74392243_m.jpg
attributes:
- 129
- 130
- 153
- 130
- 134
child_pages:
- label: "[Diameter < 3cm](/photoindexes/cnidaria/actiniara/anemone_lt3)<br>including small ones on snail shells"
  images:
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/beadbanded/050527srbd3486m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/others/zoanthid/tuberculosa/040123sisd0133m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/hermitbig/040701chgd1385m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/others/zoanthid/zoanthus/040828skdd5545ma.jpg"
- label: "[Diameter < 3-5cm Long tentacles]()"
  images:
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/sandstripe/060429skdd1375m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/spoke/050509hntg5945m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/star/060401ulrd0828m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/mangrove/060627krjd3666ma.jpg"
- label: "[Diameter < 3-5cm Short tentacles]()<br>"
  images:
  - url: "https://images.naturehungry.sg/cnidaria/others/corallimorphs/whitetip/120721tptd7882m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/others/corallimorphs/ridged/050807sjid5570m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/others/corallimorphs/beaded/060527sjig6070ma.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/others/corallimorphs/stubby/040705sisd2131m.jpg"
 
- label: "[Diameter 5-10cm]()<br>"
  images:
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/boloceroididae/060624skdg6189m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/tiger/050818chgg1345m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/pearly/091206tmd5757m.jpg"
  - url: "https://images.naturehungry.sg/cnidaria/actiniaria/pimply/080408chgd0640m.jpg"

- label: "[Diameter > 10cm smooth tentacles]()<br>"
  images:
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/gigantea/040606kusg0481m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/actinostephanus/090210trysvpd0133m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/doreensis/050821bbd5815m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/entacmaea/040410sisbd017m.jpg

- label: "[Diameter > 10cm frilly tentacles]()<br>"
  images:
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/cryptodendrum/060811rlhd5835m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/actinodendron/030714bbd0002m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/phymanthus/band/050808sntg0904m.jpg
  - url: https://images.naturehungry.sg/cnidaria/actiniaria/phymanthus/sixpoint/070602sjig9829m.jpg
  
- label: "[Cerianthids]()<br>also known as peacock or tube anemones"
  images:
  - url: https://images.naturehungry.sg/cnidaria/others/ceriantharia/common/030927cjd0058m.jpg
  - url: https://images.naturehungry.sg/cnidaria/others/ceriantharia/common/040701chgd1388m.jpg
  - url: https://images.naturehungry.sg/cnidaria/others/ceriantharia/shy/070901sjid6472m.jpg
  - url: https://images.naturehungry.sg/cnidaria/others/ceriantharia/blackmouth/050820bbg1690m.jpg

---


a central mouth; a ring of tentacles, or a disk covered with short tentacles (sometimes just bumps).
on sand, stuck to hard surfaces (stones, seagrasses, other animals).

<p> Other cnidarians <a href="">text index</a> | <a href="">photo index</a> </p>

<br>
{% for row in page.child_pages %}
<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}
---

## These are NOT sea anemones

<div class="flex flex-wrap gap-1">
{% assign entry = site.entries | where : "title","Brain anchor coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","White-tipped mushroom coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Anemone coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sunflower mushroom coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Broad feathery soft coral" | first %}
{% include entry-summary-card.html item=entry %}
</div>

---

how to tell apart

- [large 'hairy' cnidarians](cflargecnidarians.htm)
- [animals with a ring of smooth tentacles](cfringtentacles.htm)
- [animals with a ring of feathery arm](../glossary/feathery.htm)

  
  

