---
title: "Photo index of Ascidians"
description: ""
label: "Ascidians"
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

Tunicates and ascidians

{% assign filtered_posts = site.entries | where_exp: "item", "item.class=='Ascidiacea'" | where_exp: "item", "item.title != 'Pencil squids'"%}


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

*Ascidian species are difficult to positively identify without dissection and examination of internal parts. On this website, they are grouped by external features for convenience of display*

<h2>These are NOT ascidians</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Blue icing sponge" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Yellow prickly branching sponge" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Coralline red algae" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Zoanthids" | first %}
{% include entry-summary-card.html item=entry %}
</div>