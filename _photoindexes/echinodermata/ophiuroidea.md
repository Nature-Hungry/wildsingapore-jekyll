---
title: "Photo index of brittle stars"
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


{% assign filtered_posts = site.entries | where: "class", "Ophiuroidea" | where_exp: "item", "item.title != 'brittle stars'" %}
<p>
    <a href="/entries/cnidaria/crinoidea/crinoidea/">Fact sheet on brittle stars in Singapore</a>
</p>

<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}

    {% include entry-summary-rows.html item=post %}

{% endfor %}
</div>


<br>
<h2>These are NOT brittle stars</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Bristleworms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Feather stars" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sea cucumbers" | first %}
{% include entry-summary-card.html item=entry %}
</div>

### How to tell apart
- [bristly animals]()
- [feathery animals]()


