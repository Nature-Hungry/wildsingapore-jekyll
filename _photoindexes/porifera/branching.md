---
title: "Sponges"
label: "Branching & Lumpy Sponges"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes:
- 129
- 131
- 134
- 140
- 139
- 151
coverimgs:
- https://images.naturehungry.sg/porifera/sprawlorange/050309smkd1535m3.jpg
- https://images.naturehungry.sg/porifera/dactylospongia/100518bbbd3074m3.jpg
- https://images.naturehungry.sg/porifera/elegantbranch/100727chgd9336m6l.jpg
- https://images.naturehungry.sg/porifera/tubespiky/100614bbd5961m3.jpg
- https://images.naturehungry.sg/porifera/thickpink/100627hntd7322m3.jpg
---

Branching or lumpy sponges

{% assign filtered_posts = site.entries | where: "phylum", "Porifera" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

{% if post.hideFromPhotoindex != true and post.attributes contains 140 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



*Sponge species are difficult to positively identify without close examination.*
*On this website, they are grouped by external features for convenience of display.*