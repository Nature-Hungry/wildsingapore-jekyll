---
title: "Sponges"
label: "Ball & Vase shaped Sponges"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes:
- 129
- 131
- 134
- 144
- 141
- 145
- 139
- 151
coverimgs:
- https://images.naturehungry.sg/porifera/xestospongia/020101cjbd4392m3.jpg
- https://images.naturehungry.sg/porifera/patera/clionapatera1.JPG
- https://images.naturehungry.sg/porifera/blackprickly/120410chgd9133m3.jpg
- https://images.naturehungry.sg/porifera/hairyolives/100130brkd8706m3.jpg
- https://images.naturehungry.sg/porifera/golfball/201117labrk1.jpg
---

Sponges in the shape of balls or vases


{% assign filtered_posts = site.entries | where: "phylum", "Porifera" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

{% if post.hideFromPhotoindex != true and post.attributes contains 141 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



*Sponge species are difficult to positively identify without close examination.*
*On this website, they are grouped by external features for convenience of display.*