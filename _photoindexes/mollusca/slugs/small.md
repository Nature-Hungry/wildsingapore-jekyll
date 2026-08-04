---
title: "Small slugs"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


slugs with external gills: small <5cm

{% assign filtered_posts = site.entries | where: "order", "Nudibranchia" %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s < 5.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true and post.attributes contains 22 %}
    {% unless post.attributes contains 100 %}
    {% include entry-summary-card.html item=post %}
    {% endunless %}
{% endif %}
{% endfor %}
</div>



