---
title: "Cnidarians on Singapore shores"
description: "Fact sheet with photos on flora and fauna of Singapore's intertidal shores"
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


## sea anemones and anemone-like animals
polyp diameter 3-5cm short tentacles

*Size given is the diameter with tentacles expanded*

<br>
{% assign filtered_posts = site.entries | where: "subclass", "Hexacorallia"%}



<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}


{% assign match_found = false %}
{% if post.size %}
{% assign max_size = post.size | sort | last %}
{% assign min_size = post.size | sort | first %}

    {% if min_size <= 5.0 or max_size >= 3.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endif %}

{% if match_found and post.hideFromPhotoindex != true and post.attributes contains 102 %}
    
    {% include entry-summary-card.html item=post %}

{% endif %}
{% endfor %}
</div>




---

## Other useful links
- how to tell apart [animals with a ring of smooth tentacles](cfringtentacles.htm)
- [cnidarians with soft body](cnidariafi2.htm)   
- Other anemone-like animals
    - Diameter 3-5cm 
        - [short tentacles](anemonefi4.htm)
        - [long tentacles](anemonefi3.htm)  
    - [Diameter 5-10cm](anemonefi5.htm)  
    - Diameter >10cm  
        - [smooth tentacles](anemonefi7.htm)  
        - [frilly tentacles](anemonefi6.htm)
    
    - [Cerianthids](anemonefi8.htm)

