---
title: Photo index of molluscs on Singapore shores
child_pages:
- label: '<a href="bivalviafi.htm">Bivalves<br/>

    </a>clams'
  images:
  - url: bivalvia/veneridae/forked/070323skdg8233m.jpg
  - url: bivalvia/mytilidae/viridis/031207cjd0034m.jpg
  - url: bivalvia/anomiidae/understone/020616cjd0734m.jpg
  - url: bivalvia/tridacnidae/squamosa/040123sisd0129m.jpg
- label: "<a href=\"gastropodafi.htm\">Shelled \n            snails</a>"
  images:
  - url: gastropoda/trochidae/umbonium/050206cjd0010m.jpg
  - url: gastropoda/cypraeidae/milliaris/050206cjd9930m.jpg
  - url: gastropoda/strombidae/lambis/040122sisdd0143ma.jpg
  - url: gastropoda/naticidae/didyma/030315cjd0047m.jpg
- label: '<a href="gastropodafi9.htm">Limpets</a><br/>

    limpet-like and other<br/>

    strangely shaped snails'
  images:
  - url: gastropoda/limpets/patelloida/050108cjd9238m.jpg
  - url: gastropoda/limpets/scutus/020716cjd3562m.jpg
  - url: gastropoda/vermetidae/vermetidae/020715chgd3451m.jpg
  - url: gastropoda/calyptraeidae/crepidula/050315cjd1823m2.jpg
- label: "<a href=\"slugfi.htm\">Sea \n            slugs</a>"
  images:
  - url: slugs/nudibranchia/hypselodoris/020629chgd1310m.jpg
  - url: slugs/sacoglossa/ornata/040423snt0116m.jpg
  - url: slugs/anaspidae/geographica/020626chgd0432m.jpg
  - url: slugs/nudibranchia/boholiensis/060212sisg4800m.jpg
- label: '<a href="cephalopodafi.htm">Cephalopoda</a><br/>

    squids and cuttlefishes<br/>

    and octopuses'
  images:
  - url: cephalopoda/sqindian/030712hntbd0022m.jpg
  - url: cephalopoda/pygmy/030802hntd0082m.jpg
  - url: cephalopoda/slenderseagrass/060726chgd4943m.jpg
  - url: cephalopoda/sepiolida/050622cftd4092m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}
#EndEditable