---
title: "Sponges"
label: "Encrusting sponges"
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
- https://images.naturehungry.sg/porifera/branchbrown/050610sntg7665m3.jpg
- https://images.naturehungry.sg/porifera/crumbly/130822pgld2055m3.jpg
- https://images.naturehungry.sg/porifera/orangeprickly/130723bbd0085m3.jpg
- https://images.naturehungry.sg/porifera/encrustprickly/051204sisg3279m3.jpg
- https://images.naturehungry.sg/porifera/rainbow/091217sbglks.JPG
---

Encrusting sponges


{% assign filtered_posts = site.entries | where: "phylum", "Porifera" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

{% if post.hideFromPhotoindex != true and post.attributes contains 161 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



*Sponge species are difficult to positively identify without close examination.*
*On this website, they are grouped by external features for convenience of display.*