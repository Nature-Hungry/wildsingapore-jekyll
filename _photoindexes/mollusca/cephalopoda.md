---
title: "Cephalopods"
description: ""
label: "Cephalopoda"
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

octopuses, squids and cuttlefishes

{% assign filtered_posts = site.entries | where_exp: "item", "item.class=='Cephalopoda'" | where_exp: "item", "item.title != 'Pencil squids'"%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}

    {% include entry-summary-card.html item=post %}

{% endfor %}
</div>



