---
title: "Marine flatworms"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
---


{% assign filtered_posts = site.entries | where_exp: "item", "item.order=='Polycladida' " %}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

    {% include entry-summary-card.html item=post %}

{% endfor %}
</div>

<h2>These are NOT flatworms</h2>


<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Leathery soft coral ctenophores" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Acoel worms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Ribbon worms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Tiny striped nudibranch" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Onch slugs" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Soles" | first %}
{% include entry-summary-card.html item=entry %}
</div>



