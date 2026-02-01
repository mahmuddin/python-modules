# alias.py
import matematika as math

if __name__ == "__main__":
    # Gunakan functions dari module
    hasil1 = math.tambah(10,5)
    hasil2 = math.kali(7,3)

    print("10 + 5 = ", hasil1)
    print("7 x 3 = ", hasil2)

    # Gunakan variable dari module
    print("Nilai PI : ", math.PI)
    print("Dibuat oleh : ", math.NAMA_PEMBUAT)
    print("Versi : ", math.VERSI)

    # Gunakan function built-in dir()
    print("\nIsi module matematika:")
    print(dir(math))