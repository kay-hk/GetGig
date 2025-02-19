from django.contrib import admin
from .models import User, Genre, Artist, ArtistGenre, City, Festival, FestivalArtist
from .models import ContactMessage, TicketType, Ticket


# Register your models here.

admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(ArtistGenre)
admin.site.register(City)
admin.site.register(Festival)
admin.site.register(FestivalArtist)
admin.site.register(ContactMessage)
admin.site.register(TicketType)
admin.site.register(Ticket)