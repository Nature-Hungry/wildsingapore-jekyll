---
title: "Sea slugs without external gills"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


body with tendrils, etc

{% assign filtered_posts = site.entries | where: "class", "Gastropoda" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

{% if post.hideFromPhotoindex != true and post.attributes contains 30 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



<h2>These are NOT sea slugs</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Hoof-shield limpet" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Cowries" | first %}
{% include entry-summary-card.html item=entry %}
</div>