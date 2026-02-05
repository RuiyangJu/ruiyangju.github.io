---
permalink: /projects/
title: "Projects"
layout: default
author_profile: true
---

<style>
/* Projects page: simple two-column layout */
.projects-layout{
  display:flex;
  gap: 1.2rem;
  align-items:flex-start;
}
.projects-sidenav{
  width: 260px;
  flex: 0 0 260px;
  position: sticky;
  top: 90px; /* adjust if your header height differs */
  padding: 0.9rem 0.8rem;
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 10px;
  background: #fff;
}
.projects-sidenav h3{
  margin: 0 0 0.6rem 0;
  font-size: 1rem;
}
.projects-sidenav ul{
  list-style: none;
  padding: 0;
  margin: 0;
}
.projects-sidenav li{
  margin: 0.2rem 0;
}
.projects-sidenav a{
  display:block;
  padding: 0.35rem 0.5rem;
  border-radius: 8px;
  text-decoration: none;
}
.projects-sidenav a:hover{
  background: rgba(0,0,0,0.06);
}
.projects-content{
  flex: 1 1 auto;
  min-width: 0;
}

/* Responsive: stack on small screens */
@media (max-width: 900px){
  .projects-layout{ display:block; }
  .projects-sidenav{
    width: 100%;
    position: static;
    margin-bottom: 1rem;
  }
}
</style>

<div class="projects-layout">
  <aside class="projects-sidenav">
    <h3>Projects</h3>
    <ul>
      {% for item in site.data.navigation.projects %}
        <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
      {% endfor %}
    </ul>
  </aside>

  <div class="projects-content">
    Select a project from the left menu.
  </div>
</div>
