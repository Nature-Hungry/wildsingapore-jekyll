---
title: Photo index of shrimp-like crustaceans
child_pages:
- label: "<a href=\"small\">shrimps \n            and shrimp-like</a> &lt;3cm<br/>\n\
    \            including snapping shrimps, anemoneshrimps"
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/alphballsoft/110518bbd1955m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/brevicarpalis/040411hntd0083m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/alphsmooth/060810rlhd5635m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/isopoda/ligia/041018sntd7570m.jpg
- label: "<a href=\"big\">prawns, \n            shrimp, lobsters</a> &gt;3cm<br/>\n\
    \            including mudlobster, ghost shrimp, mantis shrimp"
  images:
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/penbluetail/050509hntg5929m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/stomatopoda/spearer/020328cjd7903m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/lobster/glypturus/040521sntbd0067m.jpg
  - url: https://images.naturehungry.sg/crustacea/othercrust/shrimp/penbanded/050621skdg7955m.jpg
layout: default
---
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}
