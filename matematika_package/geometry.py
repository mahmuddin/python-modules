# matematika_package/geometry.py
import math

def luas_persegi(sisi):
    """Menghitung luas persegi"""
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

def luas_lingkaran(radius):
    """Menghitung luas lingkaran"""
    return math.pi * radius * radius