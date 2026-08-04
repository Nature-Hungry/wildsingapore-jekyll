---
title: "Large shelled snails"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


Larger than 8cm of various shell shapes and habitats

{% assign filtered_posts = site.entries | where: "class", "Gastropoda" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s > 8.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true and post.attributes contains 100 %}

    {% include entry-summary-card.html item=post %}

{% endif %}
{% endfor %}
</div>



