---
title: "Typical fish-shape in freshwater"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
---

Tapered body shape with fins

{% assign filtered_posts = site.entries | where_exp: "item", "item.class=='Actinopterygii' and item.order != 'Synbranchiformes' and item.genus!='Pangio' and item.order!='Siluriformes' and item.family!='Channidae'"%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
    {% if post.zone contains "freshwater"%}
        {% include entry-summary-card.html item=post %}
    {% endif %}

{% endfor %}
</div>



