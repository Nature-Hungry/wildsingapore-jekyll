---
title: "Photo index of feather stars"
description: ""
label: "Hydroids"
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
attributes: []
coverimgs:
- https://images.naturehungry.sg/cnidaria/others/hydrozoa/delicate/050819cjg1531m3.jpg
- https://images.naturehungry.sg/cnidaria/others/hydrozoa/candy/090511chgd1389m6l.jpg
- https://images.naturehungry.sg/cnidaria/others/hydrozoa/sertularella/030714bbd0074m3.jpg
- https://images.naturehungry.sg/cnidaria/others/hydrozoa/giant/050510tusg6144m3.jpg
- https://images.naturehungry.sg/cnidaria/others/hydrozoa/thread/040409tuscd0019m3.jpg
---


{% assign filtered_posts = site.entries | where: "class", "Crinoidea" | where_exp: "item", "item.title != 'Feather stars'" %}
<p>
    <a href="/entries/cnidaria/crinoidea/crinoidea/">Fact sheet on feather stars in Singapore</a>
</p>

<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

    {% include entry-summary-card.html item=post %}

{% endfor %}
</div>


<br>
<h2>These are NOT feather stars</h2>
<div class="entry-summary-card-grid">
{% assign entry = site.entries | where : "title","Bristleworms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Brittle stars" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Fanworms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sea cucumbers" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Frilly anemones" | first %}
{% include entry-summary-card.html item=entry %}
</div>

