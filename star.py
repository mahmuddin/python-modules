# star.py
from matematika import *

if __name__ == "__main__":
    # Gunakan functions dari module
    hasil1 = tambah(10,5)
    hasil2 = kali(7,3)

    print("10 + 5 = ", hasil1)
    print("7 x 3 = ", hasil2)

    # Gunakan variable dari module
    print("Nilai PI : ", PI)
    print("Dibuat oleh : ", NAMA_PEMBUAT)
    print("Versi : ", VERSI)

    # Gunakan function built-in dir()
    print("\nIsi module matematika:")
    print(dir(matematika))