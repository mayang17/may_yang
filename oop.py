class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm

    def get_nama(self):
        return self.nama

    def get_npm(self):
        return self.npm

# Penggunaan kelas
mhs = Mahasiswa("Julia Mayang Sari", "G1A022010")
print("Nama:",mhs.get_nama()) 
print("Npm:",mhs.get_npm()) 
