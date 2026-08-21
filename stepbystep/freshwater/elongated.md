---
title: "Elongated animals in freshwater"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
---

Long, may or may not have visible fins or legs

## Snakes
{% assign filtered_posts = site.entries | where_exp: "item", "item.family == 'Homalopsidae' or item.family=='Pythonidae'"%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
    {% if post.zone contains "freshwater"%}
        {% include entry-summary-card.html item=post %}
    {% endif %}

{% endfor %}
</div>

## Ray-finned fish

{% assign filtered_posts = site.entries | where_exp: "item", "item.order == 'Synbranchiformes' or item.genus=='Pangio' or item.order=='Siluriformes' or item.family=='Channidae'"%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
    {% if post.zone contains "freshwater"%}
        {% include entry-summary-card.html item=post %}
    {% endif %}

{% endfor %}
</div>



