---
title: "Medium sized crabs"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---

Medium sized crabs: body width 3-5cm

{% assign filtered_posts = site.entries | where_exp: "item", "item.infraorder=='Brachyura' and item.superfamily !='Ocypodoidea' "%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = false %}
{% if post.size %}
{% assign max_size = post.size | sort | last %}
{% assign min_size = post.size | sort | first %}

    {% if min_size < 5.0 and max_size > 3.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endif %}

{% if match_found and post.hideFromPhotoindex != true %}
    
    {% include entry-summary-card.html item=post %}

{% endif %}
{% endfor %}
</div>



