from django.contrib import admin
from myapp.models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Quotation)
admin.site.register(QuotationJob)
admin.site.register(Machine)
admin.site.register(Task)

