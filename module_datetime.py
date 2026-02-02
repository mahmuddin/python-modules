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

# Format tanggal dan waktu dengan nama hari
print("Format tanggal dan waktu dengan nama hari:", sekarang.strftime("%A, %d %B %Y %H:%M:%S"))

# Format tanggal dan waktu dengan nama hari dan nama bulan
print("Format tanggal dan waktu dengan nama hari dan nama bulan:", sekarang.strftime("%A, %d %B %Y %H:%M:%S"))

