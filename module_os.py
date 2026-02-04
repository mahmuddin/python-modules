# module_os.py
import os

# Informasi direktoru
print("Ditektori kerja saat ini: ", os.getcwd)

# Informasi sistem
# 'nt' untuk Windows, 'posix' untuk Unix/Linux/Mac
print("Nama sistem:", os.name)

# Cek apakah file/direktiri ada
print("FIle ada: ", os.path.exists("test.txt"))
print("Direktori ada: ", os.path.exists("my_folder"))

# Informasi file
if os.path.exists("test.txt"):
    print("Adalah file: ", os.path.isfile("test.txt"))
    print("Adalah direktory: ", os.path.isdir("test.txt"))
    print("Ukuran file: ", os.path.getsize("test.txt"), "bytes")

# Path operation
file_path = "/home/mahmuddin/Documents/Tutorial/Python Modules/Exercise/file.txt"
print("Direktori: ", os.path.dirname(file_path))
print("Nama file: ", os.path.basename(file_path))
print("Nama tnapa ekstensi: ", os.path.splitext(file_path)[0])
print("Ekstensi: ", os.path.splitext(file_path)[1])