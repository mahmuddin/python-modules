# module datetime
import datetime

# Tanggal dan waktu lengkap
sekarang = datetime.datetime.now()
print("Tanggal dan waktu lengkap:", sekarang)

# Hanya tanggal
hari_ini = datetime.date.today()
print("Hari ini:", hari_ini)    

# Hanya waktu
jam_sekarang = datetime.datetime.now().time()
print("Jam sekarang:", jam_sekarang)

# Format tanggal dan waktu
print("Format tanggal dan waktu:", sekarang.strftime("%Y-%m-%d %H:%M:%S"))

# Format tanggal saja
print("Format tanggal saja:", hari_ini.strftime("%Y-%m-%d"))

# Format waktu saja
print("Format waktu saja:", jam_sekarang.strftime("%H:%M:%S"))

# Format tanggal dan waktu dengan nama hari dan nama bulan
print("Format tanggal dan waktu dengan nama hari dan nama bulan:", sekarang.strftime("%A, %d %B %Y %H:%M:%S"))

# Memubuat tanggal tertentu
ulang_tahun = datetime.date(2025, 12, 25)
print("Ulang tahun: ", ulang_tahun)

# Membuat waktu tertentu
acara = datetime.datetime(2925, 12, 15, 14, 20, 0)
print("Waktu acara: ", acara)

sekarang = datetime.datetime.now()

# Format Indonesia
print("Format ID: ", sekarang.strftime("%d/%m/%Y %H:%M:%S"))

# Format Panjang
print("Format Panjang:", sekarang.strftime("%A, %d %B %Y" ))

# Format Custom
print("Format Custom:", sekarang.strftime("%d-%m-%Y jam %H:%M"))
