---
title: Sea slugs on Singapore shores
child_pages:
- label: "<a href=\"small\">small \n            slugs</a> &lt;5cm"
  images:
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/gymnodorisblack/080702prpd6489m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/rubropapulosa/050918smkg2720m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/lineolata/050917smkg2532ma.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/hypselodoris/020629chgd1310m.jpg
- label: "<a href=\"large\">large \n            slugs</a> &gt;5cm"
  images:
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/atromarginata/050529sjig7134m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/boholiensis/030420skdd0254m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/funebris/040509skdbd0114m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/sinuatum/050917smkg2515m.jpg
- label: "<a href=\"verylarge\">very \n            large slugs</a> &gt;10cm"
  images:
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/boholiensis/060212sisg4800m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/villosa/050526cjg6776m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/spongiosa/020713cjd2437m.jpg
  - url: https://images.naturehungry.sg/mollusca/slugs/nudibranchia/actinocyclus/040520sntbd0052m.jpg

child_pages2: 
- label: "<a href=\"twoflaps\">body in two flaps</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/anaspidae/geographica/020626chgd0432m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/anaspidae/dactylomela/050610sntg7628m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/sacoglossa/ornata/070602sjig9801m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/anaspidae/extraordinaria/050410kusg4346m.jpg"
- label: "<a href=\"bumpy\">body rounded with bumps</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/onchidiidae/bigpimply/040123sisd0022m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/onchidiidae/smooth/050527srbg7003m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/varicosa/050529sjig7150m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/nigra/030712hntd0193m.jpg"
- label: "<a href=\"hairy\">body hairy or with finger-like projections</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/ianthina/030714bbd0018m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/anaspidae/bursatella/040509skdbd0143m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/sibogae/050724bbg0235m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/cerberilla/060624skdg6198m.jpg"
- label: "<a href=\"tendrils\">body with tendrils</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/notobryon/051105sisg3049m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/bornella/050210kusd0058m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/sacoglossa/polybranchia/050623cjg8455m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/crosslandia/060131sjig4508m.jpg"
- label: "<a href=\"smooth\">body smooth</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/semperi/020711chgd1918m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/babai/020724chdd3827m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/notaspidae/euselenops/070415sisg8655mb.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/nudibranchia/dermatobranchus/050529sjig7198m.jpg"
- label: "<a href=\"shelled\">with external shell</a>"
  images:
  - url: "https://images.naturehungry.sg/mollusca/slugs/cephalaspidea/haminoea/070224cjd8492ma.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/cephalaspidea/haminoea/050917smkg2564m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/sacoglossa/lobiger/050622cftg8209m.jpg"
  - url: "https://images.naturehungry.sg/mollusca/slugs/sacoglossa/volvatella/090625cyrd5563m.jpg"

layout: default
---

## slugs with feathery external gills on their backs
{% for row in page.child_pages %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}

## slugs without external gills
{% for row in page.child_pages2 %}<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}







