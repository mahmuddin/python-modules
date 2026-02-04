def tambah(a, b):
    """Menambahkan dua angka"""
    return a + b

def kurang(a, b):
    """Mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Membagi dua angka"""
    if b != 0:
        return a / b
    else:
        return "Error: Tidak bisa dibagi nol!"
