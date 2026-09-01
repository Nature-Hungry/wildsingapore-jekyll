---
title: "Small crabs with long eye stalks"
description: ""
keywords: "photo, index, sea, anemone, cnidaria, field, guide, seashore, sea, shore, marine, coastal, intertidal, singapore, facts, fact sheet, info"
layout: default
---

Small crabs with long eye stalks and body width

{% assign filtered_posts = site.entries | where_exp: "item", "item.infraorder=='Brachyura' and item.superfamily =='Ocypodoidea' "%}


<div class="entry-summary-card-grid"
>
{% for post in filtered_posts %}
{% assign match_found = true %}


{% if match_found and post.hideFromPhotoindex != true %}
    {% include entry-summary-card.html item=post %}
{% endif %}
{% endfor %}
</div>



