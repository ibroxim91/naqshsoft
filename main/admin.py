from django.contrib import admin

from .models import *



class Benefits_portfolio_Admin(admin.TabularInline):
    model = Benefits_portfolio

class Portfolio_image_Admin(admin.TabularInline):
    model = Portfolio_image




@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [Benefits_portfolio_Admin]


@admin.register(Detail_Portfolio)
class Detail_PortfolioAdmin(admin.ModelAdmin):
    inlines = [Portfolio_image_Admin]
    




admin.site.register(LatestResults)
admin.site.register(Services)
admin.site.register(Comunity)
admin.site.register(Benefits_portfolio)
admin.site.register(Portfolio_image)
