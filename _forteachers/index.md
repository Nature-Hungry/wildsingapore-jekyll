---
title: "Classroom Activities for Teachers"
layout: default
description: "Shareable classroom activities for teaching Singapore's marine biodiversity"
permalink: /forteachers/
---

Discover and share hands-on classroom activities that help students learn about Singapore's amazing marine biodiversity!

## About This Section

Teachers: Have you created an engaging classroom activity about Singapore's shores? We'd love to feature it here! Activities should include learning objectives, materials needed, step-by-step instructions, and assessment ideas. For more information, please [click here to find out more!](/forteachers/aboutactivities)

**Want to contribute?** Please email your classroom activities to [thewildsingapore@gmail.com](mailto:thewildsingapore@gmail.com).

---

## All Activities

{% assign activities = site.forteachers | where_exp: "item", "item.path contains '/activities/'" | sort: "date" | reverse %}
{% assign subjects = "" | split: "" %}

{% for activity in activities %}
  {% unless subjects contains activity.subject %}
    {% assign subjects = subjects | push: activity.subject %}
  {% endunless %}
{% endfor %}

<div class="forteacher-filters">
  <button class="filter-btn active" data-filter="all">All Subjects</button>
  {% for subject in subjects %}
    <button class="filter-btn" data-filter="{{ subject | slugify }}">{{ subject }}</button>
  {% endfor %}
</div>

{% if activities.size == 0 %}
<p><em>No activities found yet. Check back soon or contribute one!</em></p>
{% else %}

{% for activity in activities %}
  <div class="forteacher-item" data-subject="{{ activity.subject | slugify }}">
    {% include forteacher-preview.html activity=activity %}
  </div>
{% endfor %}

{% endif %}

<script>
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const filter = this.dataset.filter;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    this.classList.add('active');
    
    document.querySelectorAll('.forteacher-item').forEach(item => {
      if (filter === 'all' || item.dataset.subject === filter) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    });
  });
});
</script>

<style>
  .forteacher-filters {
    margin: 2rem 0;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
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
</style>