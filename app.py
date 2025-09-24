def tambah(x, y):
  """Fungsi untuk menjumlahkan dua angka."""
  return x + y

def kurang(x, y):
  """Fungsi untuk mengurangkan dua angka."""
  return x - y

def kali(x, y):
  """Fungsi untuk mengalikan dua angka."""
  return x * y

def bagi(x, y):
  """Fungsi untuk membagi dua angka."""
  if y == 0:
    return "Error! Tidak bisa membagi dengan nol."
  else:
    return x / y

print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

while True:
  # Meminta input dari pengguna
  pilihan = input("Masukkan pilihan (1/2/3/4): ")

  # Memeriksa apakah pilihan adalah salah satu dari empat opsi
  if pilihan in ('1', '2', '3', '4'):
    try:
      angka1 = float(input("Masukkan angka pertama: "))
      angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
      print("Input tidak valid. Harap masukkan angka.")
      continue

    if pilihan == '1':
      print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")

    elif pilihan == '2':
      print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")

    elif pilihan == '3':
      print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")

    elif pilihan == '4':
      print(f"{angka1} / {angka2} = {bagi(angka1, angka2)}")
    
    # Menanyakan apakah pengguna ingin melakukan perhitungan lain
    lanjut = input("Apakah ingin melakukan perhitungan lain? (ya/tidak): ")
    if lanjut.lower() != 'ya':
      break
  else:
    print("Pilihan tidak valid.")