from django.contrib import admin
from .models import (
    Allergy,
    Member,
    Tag,
    Event,
    EventMedia,
    CustomDate,
    Node,
    SiblingRelationship,
    SpouseRelationship,
    ParentChildRelationship,
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
