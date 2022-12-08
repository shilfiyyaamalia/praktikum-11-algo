"""
Created on Fri Dec  2 14:54:09 2022

@author: shilaaaa
"""

class Mahasiswa() :
    MhsCount = 0
    
    def init(self,Nama,Nim,Angkatan):
        self.nama = Nama
        self.nim = Nim
        self.angkatan = Angkatan

    def input_mhs(self):
        self.nama = input("Masukan nama :")
        self.nim = input("masukan nim :")
        self.angkatan =input("masukan tahun angkatan:")
        Mahasiswa.MhsCount += 1

    def count_mhs(self):
        print("\nTotal mahasiswa %d" % Mahasiswa.MhsCount)

    def display_mhs(self):
        print("\nnama",self.nama)
        print("nim",self.nim)
        print("Tahun angkatan",self.angkatan)


dataMhs = Mahasiswa()
dataMhs.input_mhs()
dataMhs.count_mhs()
dataMhs.display_mhs()
print("Total mahasiswa %d" % Mahasiswa.MhsCount)

