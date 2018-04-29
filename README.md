# django-multiple-users
this is simple example of showing different views for multiple users in django admin panel
steps =>
1. Add fields in models.py
2. Add groups from django-admin-panel
3. While adding users assign them to different groups  so that you can specifically check in your code about particular  group
4. Assign fields to particular group in admin.py, by overriding get_fields method of ModelAdmin class.
