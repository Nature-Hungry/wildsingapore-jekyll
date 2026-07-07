---
title: "Photo index of long sea cucumbers"
description: ""
label: "Long sea cucumbers"
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


{% assign filtered_posts = site.entries | where: "class", "Holothuroidea" %}


<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s > 12.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true %}

    {% include entry-summary-rows.html item=post %}

{% endif %}
{% endfor %}
</div>


<br>
<h2>These are NOT sea cucumbers</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Peanut worms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Acorn worms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Flowery sea pen" | first %}
{% include entry-summary-card.html item=entry %}
</div>



