from datetime import datetime

dogum_tarixi = input("Doğum tarixinizi daxil edin (YYYY-MM-DD): ")

cari_tarix = datetime.now()
dogum_tarixi = datetime.strptime(dogum_tarixi, '%Y-%m-%d')

fərq = cari_tarix - dogum_tarixi
saniyə = fərq.total_seconds()
deqiqə = saniyə / 60
saat = deqiqə / 60
gün = saat / 24
ay = gün / 30
yaş = int(gün / 365) 

print(f"Siz həyatda {int(saniyə)} saniyə, {int(deqiqə)} dəqiqə, {int(saat)} saat, {int(gün)} gün, {int(ay)} aydır ki mövcudsunuz.")
print(f"Sizin {yaş} yaşınız var.")
