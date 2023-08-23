from django.contrib import admin
from .models import AddBranch,pyq,pyq,pdf_formate

# Register your models here.
# admin.site.register(AddBranch)
# admin.site.register(pyq)
# admin.site.register(pdf_formate)


@admin.register(AddBranch)
class AddBranch(admin.ModelAdmin):
    list_display=['branch_name']
@admin.register(pyq)
class pyq(admin.ModelAdmin):
    list_display=['branch_name','pyq_title']
@admin.register(pdf_formate)
class pdf_formate(admin.ModelAdmin):
    list_display=['branch_name','year','pyq_pdf']