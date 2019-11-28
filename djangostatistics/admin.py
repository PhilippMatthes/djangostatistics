from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.db import models
from django.views.decorators.cache import never_cache

from . import views
from .models import Interaction


class StatisticsAdminSite(AdminSite):
    site_header = 'Statistics Admin Site'

    index_template = "djangostatistics/index.html"

    @never_cache
    def index(self, request, extra_context=None):
        """Get the index statistics page."""
        extra_context = extra_context or {}
        counted_interaction_types = Interaction.objects\
            .all()\
            .values("interaction_type")\
            .annotate(count=models.Count("pk"))
        extra_context.update(counted_interaction_types=counted_interaction_types)
        return super().index(request, extra_context)

    def get_urls(self):
        return super().get_urls() + [
            url(r'interactions/', views.interactions, name="interactions")
        ]


admin_site = StatisticsAdminSite(name='statistics_admin_site')
