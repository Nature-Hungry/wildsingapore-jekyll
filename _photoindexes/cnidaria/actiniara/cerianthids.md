---
title: "Cerianthids on Singapore shores"
description: "Fact sheet with photos on flora and fauna of Singapore's intertidal shores"
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---


outer ring of long tentacles, inner ring of very short tentacles, makes a tube to live in.

*Size given is the diameter with tentacles expanded*

<br>
{% assign filtered_posts = site.entries | where: "subclass", "Ceriantharia"%}



<div style="
    display:grid;
    grid-template-columns: repeat(auto-fill, minmax(min(480px, 100%), 1fr));
    gap:1rem;
"
>
{% for post in filtered_posts %}


{% if post.hideFromPhotoindex != true %}
    
    {% include entry-summary-rows.html item=post %}

{% endif %}
{% endfor %}
</div>



---

## Other useful links
- how to tell apart [animals with a ring of smooth tentacles](cfringtentacles.htm)   

