---
title: "Small shelled snails"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


1cm - 2cm living on and under rocks

{% assign filtered_posts = site.entries | where: "class", "Gastropoda" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s <= 2.0 and s >= 1.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true and post.attributes contains 75 %}

    {% include entry-summary-card.html item=post %}

{% endif %}
{% endfor %}
</div>



