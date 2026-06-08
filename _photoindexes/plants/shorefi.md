---
title: Photo index of seashore plants on Singapore shores
child_pages:
- label: <a href="shorefi1.htm">creepers</a>
  images:
  - url: coastal/sesuvium/portulacastrum/090405smkd9021m.jpg
  - url: coastal/sesuvium/portulacastrum/090126ubnd6233ma.jpg
  - url: coastal/ipomoea/pescaprae/090405smkd8945m.jpg
  - url: coastal/canavalia/canavalia/090405smkd9044m.jpg
- label: " <a href=\"shorefi2.htm\">climbers, \n            vines</a><br/>\n     \
    \       and rattans"
  images:
  - url: mangrove/derris/trifoliata/090321krjo3211493m.jpg
  - url: mangrove/finlaysonia/obovata/090322krjd8354m.jpg
  - url: mangrove/hoya/verticillata/011216cjcpd2455m.jpg
  - url: coastal/flagellaria/indica/090111smkd4873ma.jpg
- label: "<a href=\"shorefi3.htm\">herbs \n            and ground plants</a>"
  images:
  - url: coastal/crinum/asiaticum/090214sbwrd7060m.jpg
  - url: coastal/crinum/asiaticum/090307blyd7421m.jpg
  - url: coastal/tacca/leontopetaloides/090111smkd4869ma.jpg
- label: "<a href=\"shorefi7.htm\">seashore \n            ferns</a> "
  images:
  - url: others/asplenium/nidus/090613admd4177m.jpg
  - url: others/drymoglossum/piloselloides/090408wdld9130m.jpg
  - url: mangrove/acrostichum/speciosum/090328sbwrd0033m.jpg
  - url: mangrove/acrostichum/aureum/090328sbwrd8453ma.jpg
- label: "\n<p><a href=\"shorefi4.htm\">palms, \n              pandans</a></p>\n"
  images:
  - url: mangrove/nypa/nypa/090124ubnd5977m.jpg
  - url: mangrove/nypa/nypa/030511cjd0184m.jpg
  - url: coastal/pandanus/tectorius/051018smkg2732m.jpg
  - url: coastal/pandanus/tectorius/051018smkg2732ma.jpg
- label: "seashore \n            shrubs &lt;2m"
  images: []
- label: "<a href=\"shorefi5a.htm\">thick/leathery \n            leaves</a>"
  images:
  - url: coastal/scaevola/taccada/090405smkd9069m.jpg
  - url: coastal/ximenia/americana/090117smkd5540m.jpg
  - url: coastal/ximenia/americana/090117smkd5533m.jpg
  - url: coastal/ardisia/elliptica/050626smkd4451m.jpg
- label: "<a href=\"shorefi5b.htm\">thin \n            leaves </a>"
  images:
  - url: coastal/clerodendrum/inerme/030809ulrd0146mb.jpg
  - url: coastal/desmodium/umbellatum/090412hntd9881m.jpg
  - url: coastal/morinda/citrifolia/090328sbwrd8470m.jpg
  - url: coastal/hibiscus/tiliaceus/090117smkd5536m.jpg
- label: "seashore \n            trees &gt;2m"
  images: []
- label: "at \n            the shore<br/>\n<a href=\"shorefi6b.htm\">small simple\
    \ leaves</a>"
  images:
  - url: coastal/knema/globularia/040208cjd0011m.jpg
  - url: coastal/memecylon/edule/080720cjd8074m.jpg
  - url: coastal/knema/globularia/040208cjd0013m.jpg
  - url: coastal/pouteria/linggensis/011106cjd395m.jpg
- label: "at \n            the shore<br/>\n<a href=\"shorefi6c.htm\">large simple\
    \ leaves</a>"
  images:
  - url: coastal/calophyllum/inophyllum/090124ubnd5979m.jpg
  - url: coastal/terminalia/catappa/040831sjid6040m.jpg
  - url: coastal/cerbera/odollam/090410ubnd9387m.jpg
  - url: coastal/barringtonia/asiatica/030910sbwrad0078ma.jpg
- label: "at \n            the shore<br/>\n<a href=\"shorefi6d.htm\">compound or other\
    \ leaves</a>"
  images:
  - url: coastal/adenanthera/pavonina/090413blyd0040m.jpg
  - url: coastal/pongamia/pinnata/090410ubnd9423mb.jpg
  - url: coastal/leucaena/leucocephala/090405smkd9059ma.jpg
  - url: coastal/casuarina/equisetifolia/090314smkd8048m.jpg
- label: "mangrove \n            trees"
  images: []
- label: "<a href=\"mangfi.htm\">mangrove \n            trees</a><br/>\n         \
    \   at or below the high water mark"
  images:
  - url: mangrove/sonneratia/alba/090124ubnd5966m.jpg
  - url: mangrove/bruguiera/gymnorrhiza/090124ubnd6027m.jpg
  - url: mangrove/rhizophora/stylosa/070520smkd1221ma.jpg
  - url: mangrove/rhizophora/stylosa/081206smkd2573m.jpg
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