---
title: "Individuals Making a Change"
layout: default
description: "Shareable classroom activities for teaching Singapore's marine biodiversity"
permalink: /forindividuals/
---

<style>
  .forindividual-filters {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 1rem;
  }

  .filter-btn {
    padding: 0.5rem 1rem;
    border: 1px solid #ccc;
    background: white;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .filter-btn:hover {
    background: #f0f0f0;
  }

  .filter-btn.active {
    background: slategray;
    color: white;
    border-color: slategray;
  }

  .forindividual-item.hidden {
    display: none;
  }
</style>

There are countless ongoing programmes targeted at individuals like you. These programmes can be run by the government, Nature Groups, or interest groups.

## National Parks Board

The National Parks Board (NParks) is a statutory board under the Ministry of National Development (MND). NParks is in charge of our beautiful streetscape, neighbourhood parks, nature parks, and our beloved nature reserves. Learn the difference between these categories [here](/landusetypes).

## Nature Groups

There are multiple nature groups, and they range from non-governmental organisations (NGOs) or Societies, to interest groups that are simply collections of passionate individuals.

## Explore our Nature Community

{% assign groups = site.forindividuals | where_exp: "item", "item.path contains '/groups/'" | sort: "date" | reverse %}
{% assign grouptypes = "" | split: "" %}

{% for group in groups %}
  {% unless grouptypes contains group.grouptype %}
    {% assign grouptypes = grouptypes | push: group.grouptype %}
  {% endunless %}
{% endfor %}

<div class="forindividual-filters">
  <button class="filter-btn active" data-filter="all">All Groups</button>
  {% for grouptype in grouptypes %}
    <button class="filter-btn" data-filter="{{ grouptype | slugify }}">{{ grouptype }}</button>
  {% endfor %}
</div>

{% if groups.size == 0 %}
<p><em>No groups found yet.</em></p>
{% else %}

{% for group in groups %}
  <div class="forindividual-item" data-grouptype="{{ group.grouptype | slugify }}">
    {% include forindividual-preview.html group=group %}
  </div>
{% endfor %}

{% endif %}

<script>
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const filter = this.dataset.filter;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    this.classList.add('active');
    
    document.querySelectorAll('.forindividual-item').forEach(item => {
      if (filter === 'all' || item.dataset.grouptype === filter) {
        item.classList.remove('hidden');
      } else {
        item.classList.add('hidden');
      }
    });
  });
});
</script>