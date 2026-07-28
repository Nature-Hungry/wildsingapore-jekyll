---
title: "Very large slugs"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


slugs with external gills: very large >10cm

{% assign filtered_posts = site.entries | where: "class", "Gastropoda" %}


<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s > 9.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true and post.attributes contains 22 %}
    {% unless post.attributes contains 100 %}
    {% include entry-summary-rows.html item=post %}
    {% endunless %}
{% endif %}
{% endfor %}
</div>



<h2>These are NOT sea slugs</h2>


<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Hoof-shield limpet" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Cowries" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Marine flatworms" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Naked moon snail" | first %}
{% include entry-summary-card.html item=entry %}
</div>