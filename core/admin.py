from django.contrib import admin

# Register your models here.

from core.models import blog,Username, test_1, test_2


admin.site.register(blog)
admin.site.register(Username)
admin.site.register(test_1)
admin.site.register(test_2)

