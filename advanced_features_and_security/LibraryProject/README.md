\# Bookshelf Permissions and Groups



\## Groups

\- \*\*Editors\*\*: can add and change books

\- \*\*Viewers\*\*: can only view books

\- \*\*Admins\*\*: can add, change, and delete books



\## Custom Permissions

Defined in `Book` model:

\- `can\_add\_book`

\- `can\_change\_book`

\- `can\_delete\_book`



\## Enforcing Permissions

Views in `views.py` are decorated with `@permission\_required`:

\- `create\_book` → `can\_add\_book`

\- `edit\_book` → `can\_change\_book`

\- `delete\_book` → `can\_delete\_book`



Assign users to groups via Django admin to control access.



