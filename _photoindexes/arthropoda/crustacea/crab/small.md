---
title: "Small crabs"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---

Small crabs: body width < 3 cm

{% assign filtered_posts = site.entries | where_exp: "item", "item.infraorder=='Brachyura' and item.superfamily !='Ocypodoidea' "%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s < 3.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true 2 %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



