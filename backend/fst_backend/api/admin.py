from django.contrib import admin

from .models import (
    Allergy,
    Event,
    EventLocation,
    EventMedia,
    Person,
    ParentChildRelationship,
    SiblingRelationship,
    SpouseRelationship,
    Tag,
)

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(EventLocation)
admin.site.register(EventMedia)
admin.site.register(Person)
admin.site.register(Allergy)
admin.site.register(SiblingRelationship)
admin.site.register(SpouseRelationship)
admin.site.register(ParentChildRelationship)
