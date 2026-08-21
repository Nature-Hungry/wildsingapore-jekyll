---
title: Photo index of crustaceans on Singapore shores
child_pages:
- label: "<a href=\"shrimpfi1.htm\">shrimps \n            and shrimp-like</a> &lt;3cm<br/>\n\
    \            including snapping shrimps, anemoneshrimps"
  images:
  - url: othercrust/shrimp/alphballsoft/110518bbd1955m.jpg
  - url: othercrust/shrimp/brevicarpalis/040411hntd0083m.jpg
  - url: othercrust/shrimp/alphsmooth/060810rlhd5635m.jpg
  - url: othercrust/isopoda/ligia/041018sntd7570m.jpg
- label: "<a href=\"shrimpfi2.htm\">prawns, \n            shrimp, lobsters</a> &gt;3cm<br/>\n\
    \            including mudlobster, ghost shrimp, mantis shrimp"
  images:
  - url: othercrust/shrimp/penbluetail/050509hntg5929m.jpg
  - url: othercrust/stomatopoda/spearer/020328cjd7903m.jpg
  - url: othercrust/lobster/glypturus/040521sntbd0067m.jpg
  - url: othercrust/shrimp/penbanded/050621skdg7955m.jpg
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