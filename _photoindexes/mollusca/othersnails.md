---
title: "Photo index of limpets"
description: ""
label: "Limpets"
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

limpets, limpet-like animals and other strangely shaped snails

{% assign filtered_posts = site.entries | where_exp: "item", "item.order == 'Nacellida' or item.order=='Siphonariida' or item.order=='Lepetellida' or item.family=='Calyptraeidae' or item.family=='Vermetidae' or item.class=='Polyplacophora'"%}


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
<h2>These are NOT molluscs</h2>
<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Barnacles" | first %}
{% include entry-summary-card.html item=entry %}
</div>

