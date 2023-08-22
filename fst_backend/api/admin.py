from django.contrib import admin
from .models import Allergy, Member, Tag, Event, EventMedia

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(EventMedia)
admin.site.register(Member)
admin.site.register(Allergy)
