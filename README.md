# HeyFlask
---
In this commit i have polished up my todo app 
All the completed todos are rendered in `complete/all` page handled by `complete_all` function
To render this out i have created an new html page i.e `all.html`
__i have fixed a bug from last commit i.e **v0.6** branch `{% if stuff.todo.is_completed %}` -> `{% if not stuff.is_completed %}`
