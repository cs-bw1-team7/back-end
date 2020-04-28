from django.contrib.auth.models import User
from adventure.models import Area, Player, Room


Room.objects.all().delete()

area = Area(width=50,
            height=50,
            level=0,
            max_regions=10,
            max_region_size=7,
            min_region_size=3
            )

area.save()
area.generate_regions(area.id)


players = Player.objects.all()
for p in players:
    p.currentArea = area.id
    p.save()
