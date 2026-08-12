---
title: "Feathery marine worms "
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
---

Worms with feathery heads

{% assign filtered_posts = site.entries | where_exp: "item", "item.family=='Sabellidae' " %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

    {% include entry-summary-card.html item=post %}

{% endfor %}
</div>

<h2>These are NOT fanworms</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Cerianthid phoronid worm" | first %}
{% include entry-summary-card.html item=entry %}
</div>



