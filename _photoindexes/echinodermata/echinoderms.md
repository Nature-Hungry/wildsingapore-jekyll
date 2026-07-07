---
title: Photo index of echinoderms
permalink: "/photoindexes/echinodermata"
child_pages:
- label: "Arms many, long feathery <br/>\n<a href=\"/photoindexes/echinodermata/crinoids\"\
    >feather stars</a>"
  images:
  - url: https://images.naturehungry.sg/echinodermata/crinoidea/blue/050820bbg1788m.jpg
  - url: https://images.naturehungry.sg/echinodermata/crinoidea/purpurea/050623cjg8337m.jpg
  - url: https://images.naturehungry.sg/echinodermata/crinoidea/red/080425cyrd1820m.jpg
  - url: https://images.naturehungry.sg/echinodermata/crinoidea/pale/060713rlhd4327m.jpg
- label: "Arms five, long bristley<br/>\n<a href=\"/photoindexes/echinodermata/ophiuroidea\"\
    >brittle stars</a>"
  images:
  - url: https://images.naturehungry.sg/echinodermata/ophiuroidea/flatarm/040702chgd1476m.jpg
  - url: https://images.naturehungry.sg/echinodermata/ophiuroidea/longipeda/030615cjd0228m.jpg
  - url: https://images.naturehungry.sg/echinodermata/ophiuroidea/tinysponge/050806skdg0477mb.jpg
  - url: https://images.naturehungry.sg/echinodermata/ophiuroidea/basket/120124sisd6015me.jpg
- label: "Arms 5-8, short<br/>\n<br/>\n <a href=\"/photoindexes/echinodermata/asteroideasmall\"
    >small</a>\n&lt;10cm<br/><a href=\"/photoindexes/echinodermata/asteroideabig\">large</a>\
    \ &gt; 10cm"
  images:
  - url: https://images.naturehungry.sg/echinodermata/asteroidea/sandpainted/050622chgg8118m.jpg
  - url: https://images.naturehungry.sg/echinodermata/asteroidea/luimaculata/060429skdg5789m.jpg
  - url: https://images.naturehungry.sg/echinodermata/asteroidea/culcita/060401ulrd0750m.jpg
  - url: https://images.naturehungry.sg/echinodermata/asteroidea/protoreaster/040508skdbd0025m.jpg
- label: "Hard \n            flat, coin-like <br/>\n<a href=\"/photoindexes/echinodermata/sanddollars\"\
    >sand dollars</a>"
  images:
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/sandollar/echinodiscus/050206cjd9966m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/sandollar/arachnoides/030927cjd0033m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/sandollar/peronella/080704sekd6789m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/sandollar/depressum/070420sntrd0301m.jpg
- label: "Hard \n            spherical, spiny<br/>\n<a href=\"/photoindexes/echinodermata/urchins\"\
    >sea urchins, heart urchins </a>"
  images:
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/urchin/salmacis/050621skdg8023m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/urchin/diadema/040830hntd5872m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/hearturchin/lovenia/040731kusd3539m.jpg
  - url: https://images.naturehungry.sg/echinodermata/echinoidea/urchin/prionocidaris/011019cjd121m.jpg
- label: "Soft \n            round or long<br/>\n            sea cucumbers <br/>\n\
    <a href=\"/photoindexes/echinodermata/cucumbersmall\">short</a> &lt;10cm "
  images:
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/colochirus/031226chgd0003m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/synsponge/030717skdd0090m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/beige/030518cjd0327m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/purple/031226chgd0061m.jpg
- label: "Soft \n            round or long<br/>\n            sea cucumbers <br/>\n\
    <a href=\"/photoindexes/echinodermata/cucumberbig\">long</a> &gt;10cm"
  images:
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/phyllophorus/050315cjd1805m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/lecanora/070203smkg7475m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/smooth/040425cjd0081m.jpg
  - url: https://images.naturehungry.sg/echinodermata/holothuroidea/scabra/020907cjd5425m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}

<h2>These are NOT echinoderms</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Sea anemones" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Cerianthids" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Fanworms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Acorn worms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Flowery sea pen" | first %}
{% include entry-summary-card.html item=entry %}
</div>


<h3>how to tell apart </h3>
<ul>
<li><a href="../glossary/wormstar.htm">bristley 
                  animals</a></li>
<li><a href="../glossary/feathery.htm">feathery 
                  animals</a></li>
<li><a href="cfbigstars.htm">large 
                  sea stars</a></li>
<li><a href="../glossary/sausage.htm">sausage-like 
                  animals</a></li>
<li> <a href="../glossary/wormy.htm">worm-like 
                  animal</a></li>
</ul>