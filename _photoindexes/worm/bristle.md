---
title: "Marine worms"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
---

Typical worm-shaped with bristles

{% assign filtered_posts = site.entries | where_exp: "item", "item.phylum=='Annelida' and item.attributes contains 149" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

    {% include entry-summary-card.html item=post %}

{% endfor %}
</div>

<h2>These are NOT worms</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Synaptid sea cucumbers" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sea slugs" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Snake-eels" | first %}
{% include entry-summary-card.html item=entry %}
</div>



