from django.contrib import admin
from .models import chaiVariety, chaiReview, Store, ChaiCertificate


# Register your models here.
class chaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 2


class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "chai_type",
        "date_added",
    )
    inlines = [chaiReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("chai_variety",)


class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ("chai", "certificate_number")


admin.site.register(chaiVariety, chaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
