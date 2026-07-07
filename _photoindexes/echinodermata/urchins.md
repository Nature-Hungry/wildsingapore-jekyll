---
title: "Photo index of urchins"
description: ""
label: "Sea urchins and heart urchins"
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

{% assign target = "Sand dollars, Cake sand dollar, Pink sand dollar, Keyhole sand dollar, Thick-edged sand dollar" | split: ", " %}

{% assign filtered_posts = site.entries | where: "class", "Echinoidea" %}


<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}

{% unless target contains post.title%}
    {% include entry-summary-rows.html item=post %}
{% endunless %}
{% endfor %}
</div>





