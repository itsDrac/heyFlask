# HeyFlask
---
In this commit, I have implement **U** i.e **Update** and **D** i.e **Delete** of **CRUD**. Using _`flask_sqlalchemy`_ 
for this, I have added **two** new **routes** of **GET** type i.e `add/complete` and `add/delete`.
Which are handled by function `complete_todo` and `delete_todo`, respectively

As for **U** i.e **Update** part of **CRUD**, I have added a new field which is :

- is_completed --> Boolean(default value = False)
