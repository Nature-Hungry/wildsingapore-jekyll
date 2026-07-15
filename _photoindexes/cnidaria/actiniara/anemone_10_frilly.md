---
title: "Cnidarians on Singapore shores"
description: "Fact sheet with photos on flora and fauna of Singapore's intertidal shores"
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


## sea anemones and anemone-like animals
diameter > 10cm, with smooth tentacles

*Size given is the diameter with tentacles expanded*

<br>
{% assign filtered_posts = site.entries | where: "order", "Actiniaria" | where_exp: "item" ,"item.genus == 'Phymanthus'"%}



<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}


{% assign match_found = false %}
{% for s in post.size %}
    {% if s >= 10.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}


{% if match_found and post.hideFromPhotoindex != true %}
    
    {% include entry-summary-rows.html item=post %}

{% endif %}
{% endfor %}
</div>



---

## Other useful links
- how to tell apart 
    - [large hairy cnidarians](cflargecnidarians.htm)
    - [animals with a ring of feathery arms](feathery.htm)   

