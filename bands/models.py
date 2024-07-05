from django.db import models

class Band(models.Model):
    band_name = models.CharField(max_length=50)
    start_date = models.IntegerField()
    description = models.TextField()

    ROCK = 1
    METAL = 2
    POP = 3
    BLUES = 4
    JAZZ = 5
    FOLK = 6
    RAP = 7
    TIPO_CHOICES = [
        (ROCK, "Rock"),
        (METAL, "Metal"),
        (POP, "Pop"),
        (BLUES, "Blues"),
        (JAZZ, "Jazz"),
        (FOLK, "Folk"),
        (RAP, "Rap"),
    ]

    music_type = models.IntegerField(choices=TIPO_CHOICES, default=ROCK)
    band_image = models.ImageField(upload_to='bands/', blank=True)

    def __str__(self):
        return f'{self.band_name} - {self.start_date}, {self.get_music_type_display()}'


class BandMember(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.IntegerField("Birth Date")
    musician_image = models.ImageField(upload_to='musicians/', blank=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='members')


    def __str__(self):
        return f'{self.name}'


class Music(models.Model):
    music_name = models.CharField(max_length=50)
    writer = models.ForeignKey(BandMember, on_delete=models.CASCADE, related_name='musics', null=True, blank=True)
    release_date = models.IntegerField()
    lyrics = models.TextField()

    def __str__(self):
        return f'{self.music_name} - {self.release_date}'


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_release_date = models.IntegerField(blank=True)
    musics = models.ManyToManyField(Music, related_name='albums')
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f'{self.album_name} - {self.album_release_date}'
