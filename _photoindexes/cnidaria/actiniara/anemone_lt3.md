---
title: "Photo index of cnidarians on Singapore shores"
description: "Fact sheet with photos on flora and fauna of Singapore's intertidal shores"
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


## sea anemones and anemone-like animals with polyp diameter < 3cm
*Size given is the diameter with tentacles expanded*

<br>
{% assign filtered_posts = site.entries | where: "order", "Actiniaria" %}


<div style="display:flex;flex-wrap:wrap;gap:1rem;">
{% for post in filtered_posts %}
{% assign match_found = false %}

{% for s in post.size %}
    {% if s < 3.0 %}
    {% assign match_found = true %}
    {% endif %}
{% endfor %}

{% if match_found and post.hideFromPhotoindex != true %}

<div style="max-width:550px;width:stretch;">
    {% include entry-summary-rows.html item=post %}
</div>
{% endif %}
{% endfor %}
</div>



---
## These are NOT sea anemones

<div class="flex flex-wrap gap-2">
{% assign entry = site.entries | where : "title","Sea mat zoanthid" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Broad zoanthid" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Button zoanthid" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Pink button zoanthid" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Ball-tip corallimorphs" | first %}
{% include entry-summary-card.html item=entry %}
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

