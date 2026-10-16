---
title: "Freshwater fishes"
label: ""
description: "Fish that can be found in freshwater"
layout: default
attributes:
- 129
- 133
- 134
- 138
- 141
- 146
- 150
- 156
coverimgs:
- https://images.naturehungry.sg/porifera/sprawlorange/050309smkd1535m3.jpg
- https://images.naturehungry.sg/porifera/dactylospongia/100518bbbd3074m3.jpg
- https://images.naturehungry.sg/porifera/elegantbranch/100727chgd9336m6l.jpg
- https://images.naturehungry.sg/porifera/tubespiky/100614bbd5961m3.jpg
- https://images.naturehungry.sg/porifera/thickpink/100627hntd7322m3.jpg
---



{% assign filtered_posts = site.entries | where_exp: "item", "	item.class == 'Actinopterygii' " %}

## Barbs and carps
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.family=='Cyprinidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Danionids and rasbora
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.family=='Danionidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Loaches
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.suborder=='Cobitoidei'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Catfish
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Siluriformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Swamp eels
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Synbranchiformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Rivulines, Killifishes, and Livebearers
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Cyprinodontiformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Labyrinth fishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Anabantiformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Halfbeaks, needlefishes & ricefish
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Beloniformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Bonytongues
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.order=='Osteoglossiformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Cichlids
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 156  and post.family=='Cichlidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>


