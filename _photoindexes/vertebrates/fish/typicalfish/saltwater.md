---
title: "Marine & brackish fishes"
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

<!-- ## Gudgeons
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Eleotridae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div> -->

## Gobies
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.subfamily=='Gobiinae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Mudskippers
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.subfamily=='Oxudercinae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>





## Mullets
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.order=='Mugiliformes'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Damselfishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Pomacentridae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Snappers
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Lutjanidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Asian Glassfishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Ambassidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Goatfishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Mullidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Cardinalfishes & Nurseryfishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.suborder=='Apogonoidei'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Perches, Groupers & Allies
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.suborder=='Percoidei'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>

## Archerfishes
<div class="entry-summary-card-grid">
{% for post in filtered_posts %}
{% if post.hideFromPhotoindex != true and post.attributes contains 155  and post.family=='Toxotidae'%}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>


