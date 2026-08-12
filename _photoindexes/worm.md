---
title: Marine worms on Singapore shores
attributes:
- 130
- 129
- 131
- 132
- 133
- 134
- 137
- 143
- 144
- 148
- 149
- 150
coverimgs:
- https://images.naturehungry.sg/worm/sipuncula/sipuncula/031122cjd0011m.jpg
- https://images.naturehungry.sg/worm/polychaeta/reef/040804skdd4129m.jpg
- https://images.naturehungry.sg/worm/polychaeta/gregarious/060129skdg4109m.jpg
- https://images.naturehungry.sg/worm/polychaeta/sabellidae/banded/060611cjd2781m.jpg
- https://images.naturehungry.sg/worm/polycladida/acanthozoon/060625bbd3443m.jpg
child_pages:
- label: "<a href=\"smooth\">Typical \n            worms: smooth</a><br/>\n\
    \            acorn worms, peanut worms, ribbon worms"
  images:
  - url: https://images.naturehungry.sg/worm/enteropneusta/enteropneusta/050402cjd2070ma.jpg
  - url: https://images.naturehungry.sg/worm/sipuncula/sipuncula/031122cjd0011m.jpg
  - url: https://images.naturehungry.sg/worm/nemertea/redreef/060115sntg3977m.jpg
  - url: https://images.naturehungry.sg/worm/nemertea/verylong/050325sjid1973ma.jpg
- label: "<a href=\"bristle\">Typical \n            worms: bristley</a><br/>\n\
    \            bristleworms "
  images:
  - url: https://images.naturehungry.sg/worm/polychaeta/giant/040521sntad0079m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/chloeia/050412tusd2407m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/reef/040804skdd4129m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/scaleworm/120511tpld3253m.jpg
- label: "<a href=\"tube\">Worms \n            that make tubes</a> <br/>\n\
    \            to live in: keelworms, tubeworms"
  images:
  - url: https://images.naturehungry.sg/worm/polychaeta/serpulidae/020725chgd4058ma.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/strawtube/020627chgd0515m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/diopatra/050310smkd1573m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/serpulidae/050822cjg2064md.jpg
- label: "<a href=\"feather\">Feathery \n            worms</a> <br/>\n  \
    \          fanworms, phoronid worms"
  images:
  - url: https://images.naturehungry.sg/worm/polychaeta/sabellidae/banded/060611cjd2781m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/sabellidae/white/050526cjg6820m.jpg
  - url: https://images.naturehungry.sg/worm/phoronida/phoronida/031226chgd0056m.jpg
  - url: https://images.naturehungry.sg/worm/polychaeta/sabellidae/orange/060809skdd5505m.jpg
- label: <a href="flat">Flatworms</a>
  images:
  - url: https://images.naturehungry.sg/worm/polycladida/blueline/030518cjd0173m.jpg
  - url: https://images.naturehungry.sg/worm/polycladida/baibaiye/050709skdg9312m3.jpg
  - url: https://images.naturehungry.sg/worm/polycladida/acanthozoon/060625bbd3443m.jpg
  - url: https://images.naturehungry.sg/worm/polycladida/acanthozoon/050112smkd9730m3.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}
<br/>
<i>*Worm species are 
      difficult to positively identify without close examination. <br/>
      On this website, they are grouped by external features for convenience of 
      display.</i>
<hr/>



<h2>These are NOT worms</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Brittle stars" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Synaptid sea cucumbers" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sea slugs" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Worm snails" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Snake-eels" | first %}
{% include entry-summary-card.html item=entry %}
</div>
