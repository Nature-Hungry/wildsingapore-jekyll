---
title: Photo index of mangrove trees on Singapore shores
child_pages:
- label: "small \n            oval fruits and<br/>\n<a href=\"mangfi6a.htm\">pneumatophores</a>\
    \ (pencil roots)"
  images:
  - url: mangrove/avicennia/alba/011107sbwrcpd583m.jpg
  - url: mangrove/avicennia/marina/090112smkd5020m.jpg
  - url: mangrove/avicennia/rumphiana/030914cjd0030mb.jpg
  - url: mangrove/avicennia/officinalis/020727cjcpd4361m.jpg
- label: "long \n            cylindrical fruits and<br/>\n<a href=\"mangfi6b.htm\"\
    >knee roots</a>"
  images:
  - url: mangrove/bruguiera/cylindrica/020418sbwrcpd8227ma.jpg
  - url: mangrove/ceriops/tagal/090117smkd5480m.jpg
  - url: mangrove/bruguiera/gymnorrhiza/090124ubnd6027m.jpg
  - url: mangrove/bruguiera/gymnorrhiza/090124ubnd6020ma.jpg
- label: "long \n            cylindrical fruits and<br/>\n<a href=\"mangfi6c.htm\"\
    >buttressed roots</a>"
  images:
  - url: mangrove/bruguiera/sexangula/090329cjd8652m.jpg
  - url: mangrove/bruguiera/hainesii/090529prpd2943m.jpg
  - url: mangrove/bruguiera/hainesii/090614ubnd4261m.jpg
  - url: mangrove/xylocarpus/granatum/090124ubnd6015m.jpg
- label: "long \n            cylindrical fruits and<a href=\"mangfi6d.htm\"><br/>\n\
    \            stilt and prop roots</a>"
  images:
  - url: mangrove/ceriops/zippeliana/090301prpd7368m.jpg
  - url: mangrove/ceriops/zippeliana/090124ubnd6058ma.jpg
  - url: mangrove/rhizophora/stylosa/081206smkd2573m.jpg
  - url: mangrove/rhizophora/stylosa/070520smkd1221ma.jpg
- label: "<a href=\"mangfi6f.htm\">large \n            round fruits</a><br/>\n   \
    \         with various kinds of roots"
  images:
  - url: mangrove/sonneratia/alba/090124ubnd5966m.jpg
  - url: mangrove/sonneratia/alba/090411lckd9580ma.jpg
  - url: mangrove/xylocarpus/granatum/090111smkd4886ma.jpg
  - url: mangrove/xylocarpus/granatum/090208smkd6458ma.jpg
- label: "<a href=\"mangfi7a.htm\">other \n            mangrove trees</a>"
  images:
  - url: mangrove/excoecaria/excoecaria/090321krjo3211569m.jpg
  - url: mangrove/heritiera/heritiera/090328sbwrd8495ma.jpg
  - url: mangrove/excoecaria/excoecaria/050809lckg0947ma.jpg
  - url: mangrove/dolichandrone/dolichandrone/090214sbwrd7054m.jpg
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