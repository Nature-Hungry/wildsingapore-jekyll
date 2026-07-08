---
title: Photo index of molluscs
child_pages:
- label: '<a href="/photoindexes/mollusca/bivalvia">Bivalves<br/>
    </a>clams'
  images:
  - url: https://images.naturehungry.sg/mollusca/bivalvia/veneridae/forked/070323skdg8233m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/mytilidae/viridis/031207cjd0034m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/anomiidae/understone/020616cjd0734m.jpg
  - url: https://images.naturehungry.sg/mollusca/bivalvia/tridacnidae/squamosa/040123sisd0129m.jpg
- label: "<a href=\"/photoindexes/mollusca/shelledsnails\">Shelled \n            snails</a>"
  images:
  - url: https://images.naturehungry.sg/mollusca/gastropoda/trochidae/umbonium/050206cjd0010m.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/cypraeidae/milliaris/050206cjd9930m.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/strombidae/lambis/040122sisdd0143ma.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/naticidae/didyma/030315cjd0047m.jpg
- label: '<a href="/photoindexes/mollusca/othersnails">Limpets</a><br/>

    limpet-like and other<br/>

    strangely shaped snails'
  images:
  - url: https://images.naturehungry.sg/mollusca/gastropoda/limpets/patelloida/050108cjd9238m.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/limpets/scutus/020716cjd3562m.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/vermetidae/vermetidae/020715chgd3451m.jpg
  - url: https://images.naturehungry.sg/mollusca/gastropoda/calyptraeidae/crepidula/050315cjd1823m2.jpg
- label: "<a href=\"/photoindexes/mollusca/slug\">Sea \n            slugs</a>"
  images:
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/hypselodoris/020629chgd1310m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/sacoglossa/ornata/040423snt0116m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/anaspidae/geographica/020626chgd0432m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/boholiensis/060212sisg4800m.jpg
- label: '<a href="/photoindexes/mollusca/cephalopoda">Cephalopoda</a><br/>

    squids and cuttlefishes<br/>

    and octopuses'
  images:
  - url: https://images.naturehungry.sg/mollusca/cephalopoda/sqindian/030712hntbd0022m.jpg
  - url: https://images.naturehungry.sg/mollusca/cephalopoda/pygmy/030802hntd0082m.jpg
  - url: https://images.naturehungry.sg/mollusca/cephalopoda/slenderseagrass/060726chgd4943m.jpg
  - url: https://images.naturehungry.sg/mollusca/cephalopoda/sepiolida/050622cftd4092m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}