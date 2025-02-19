from django.db import models

# Create your models here.
class User(models.Model):
    uemail = models.CharField(primary_key=True, max_length=20)
    upassword = models.CharField(max_length=20, default="passwd")

    class Meta:
        db_table = "user"

class Genre(models.Model):
    gid = models.AutoField(primary_key=True, db_column='gid')
    gname = models.CharField(max_length=255)

    class Meta:
        db_table = 'genre'

    def __str__(self):
        return self.gname
    
class Artist(models.Model):
    aid = models.AutoField(primary_key=True, db_column='aid')
    aname = models.CharField(max_length=255)
    genres = models.ManyToManyField(
        Genre, 
        through='ArtistGenre', 
        related_name='artists'
    )

    class Meta:
        db_table = 'artist'

    def __str__(self):
        return self.aname

class ArtistGenre(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column='aid')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, db_column='gid')

    class Meta:
        db_table = 'artist_genre'
        unique_together = (('artist', 'genre'),)

class City(models.Model):
    cid = models.AutoField(primary_key=True, db_column='cid')
    cname = models.CharField(max_length=255)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.cname

class Festival(models.Model):
    fid = models.AutoField(primary_key=True, db_column='fid')
    fname = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE, db_column='cid')
    start_date = models.DateField()
    end_date = models.DateField()
    artists = models.ManyToManyField(
        'Artist', 
        through='FestivalArtist', 
        related_name='festivals'
    )
    poster = models.CharField(max_length=500, default="", blank=True)
    description = models.CharField(max_length=500, default="", blank=True)
    playlist = models.CharField(max_length=500, default="", blank=True)

    class Meta:
        db_table = 'festival'

    def __str__(self):
        return self.fname
    
    def get_genre_classes(self):
        genres = set()
        for artist in self.artists.all():
            for genre in artist.genres.all():
                genres.add(genre.gname.lower())
        return " ".join(genres)

class FestivalArtist(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, db_column='fid')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column='aid')

    class Meta:
        db_table = 'festival_artist'
        unique_together = (('festival', 'artist'),)      
        
class ContactMessage(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class TicketType(models.Model):
    id = models.AutoField(primary_key=True)
    TICKET_TYPES = [
        ('Camping', 'Camping'),
        ('Non-Camping', 'Non-Camping'),
        ('VIP', 'VIP'),
    ]

    ticket_type_name = models.CharField(max_length=20, choices=TICKET_TYPES, unique=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tickettype"

    def __str__(self):
        return f"{self.ticket_type_name} - ${self.ticket_price}"

class Ticket(models.Model):
    tid = models.AutoField(primary_key=True, db_column='tid')
    fid = models.ForeignKey('Festival', on_delete=models.CASCADE, db_column='fid', related_name='tickets')
    ticket_type_id = models.ForeignKey(TicketType, on_delete=models.CASCADE, db_column='ticket_type_id',null=True)
    ticket_quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    ticket_date = models.DateField(default=None, blank=True)
    uemail = models.ForeignKey(User, on_delete=models.CASCADE, db_column='uemail',null=True)

    class Meta:
        db_table = "ticket"

    def save(self, *args, **kwargs):
        if self.ticket_type_id:
            self.total_price = self.ticket_quantity * self.ticket_type_id.ticket_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_quantity} {self.ticket_type_id.ticket_type_name} tickets for {self.fid.fname} - ${self.total_price}"