---
title: "Sponges"
label: "Sponges in other shapes"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes:
- 129
- 131
- 134
- 139
- 151
coverimgs:
- https://images.naturehungry.sg/porifera/oceanapia/110521smks01955m3.jpg
- https://images.naturehungry.sg/porifera/rotijala/130723bbd0097m3.jpg
- https://images.naturehungry.sg/porifera/manyconed/120411thntd9374m3.jpg
- https://images.naturehungry.sg/porifera/coelocarteria/050112smkd9696m3.jpg
- https://images.naturehungry.sg/porifera/chimney/120508skdd1842m3.jpg
---

Sponges in other shapes


{% assign filtered_posts = site.entries | where: "phylum", "Porifera" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

{% if post.hideFromPhotoindex != true and post.attributes contains 160 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



*Sponge species are difficult to positively identify without close examination.*
*On this website, they are grouped by external features for convenience of display.*