# Import necessary modules
import os
import django
import json

# Import your Django models
from bands.models import *

'''
# Path to your JSON file
json_file = 'bands/json/bands.json'

# Read JSON data from file
with open(json_file, 'r') as f:
    bands_data = json.load(f)

# Clear existing data (optional)
Band.objects.all().delete()
BandMember.objects.all().delete()

# Iterate over bands data and create Band and BandMember instances
for band_data in bands_data:
    # Create Band instance
    band = Band.objects.create(
        band_name=band_data['band_name'],
        start_date=band_data['start_date'],
        music_type=band_data['music_type']
    )

    # Create BandMember instances for each band
    for member_data in band_data['members']:
        BandMember.objects.create(
            name=member_data['name'],
            birth_date=member_data['birth_date'],
            band=band
        )

        print(f"Added BandMember: {member_data['name']} to Band: {band_data['band_name']}")

print("Database populated with bands and band members successfully!")
'''

json_file = 'bands/json/ledzeplin.json'

# Read JSON data from file
with open(json_file, 'r') as f:
  musics_data = json.load(f)


band_name = musics_data['band_name']
band = Band.objects.get(band_name=band_name)

for album_data in musics_data['albums']:
  # Create Album object
  album = Album.objects.create(
      album_name=album_data['album_name'],
      album_release_date=album_data.get('album_release_date'),  # Optional field

      band=band,
  )

  # Create Music objects for each song in the album
  for music_data in album_data['musics']:
    # Find or create writer based on name (assuming name is unique)
    writer_name = music_data.get('writer', {}).get('name')
    writer = None
    if writer_name:
      try:
        writer = BandMember.objects.get(name=writer_name)
      except BandMember.DoesNotExist:
        pass  # Skip creating writer if not found

    # Create Music object
    musicJson = Music.objects.create(
        music_name=music_data['music_name'],
        release_date=music_data.get('release_date'),  # Optional field
        writer=writer,
    )

    album.musics.add(musicJson)


