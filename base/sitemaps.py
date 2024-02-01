from django.contrib.sitemaps import Sitemap
from .models import RoomMember

class RoomMemberSitemap(Sitemap):
    def items(self):
        return RoomMember.objects.all()

    def location(self, item):
        return item.get_absolute_url()