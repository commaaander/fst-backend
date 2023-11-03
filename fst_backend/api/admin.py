from django.contrib import admin

from .models import (
    Allergy,
    CustomDate,
    Event,
    EventMedia,
    Member,
    Node,
    ParentChildRelationship,
    SiblingRelationship,
    SpouseRelationship,
    Tag,
)

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(EventMedia)
admin.site.register(Member)
admin.site.register(Allergy)
admin.site.register(CustomDate)
admin.site.register(Node)
admin.site.register(SiblingRelationship)
admin.site.register(SpouseRelationship)
admin.site.register(ParentChildRelationship)
