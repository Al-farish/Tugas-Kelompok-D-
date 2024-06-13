import mysql.connector
import os
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db = "tugas_kelompok"
)

cursor = mydb.cursor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu ():
    clear_screen()
    print("==== APLIKASI DATABASE PYTHON ====")
    print("[1] Insert Data")
    print("[2] Tampilkan Data")
    print("[3] Update Data")
    print("[4] Hapus Data")
    print("[5] Cari Data")
    print("[0] Exit")
    print(25 * "-")
    menu = input("Pilih menu : ")

    if menu == '1':
        insert()
    elif menu == '2':
        show()
    elif menu == '3':
        update()
    elif menu == '4':
        delete()
    elif menu == '5':
        search()
    elif menu == '0':
        print("Terimakasih Telah Berkunjung")
        exit()
    else:
        print("Menu yang anda masukan tidak ada, Masukan Pilihan yang tersedia...!")
        kembali()
    

def insert():
    print("\n", "="* 10, "Input Data Mahasisawa", "="* 10, "\n")
    nim = input("Masukan NIM anda : ")
    nama = input("Masukan Nama anda : ")
    alamat = input("Masukan Alamat anda : ")
    
    sql = "INSERT INTO anggota_kelompok (nim, nama_mahasiswa, alamat) VALUES (%s, %s, %s)"
    val =(nim, nama, alamat)
    cursor.execute(sql,val)

    mydb.commit()
    print("=== Data berhasil di tambahkan ===")
    kembali()

def show(): 
    print("\n", "="* 10, "Daftar Mahasisawa", "="* 10, "\n")
    print("NIM \t\tNama Mahasiswa \t\tAlamat")
    sql = "SELECT * FROM anggota_kelompok"
    cursor.execute(sql)
    results = cursor.fetchall()

    for data in results:
        print(data)
    kembali()

def update():
    print("\n", "="* 10, "Update Data Mahasisawa", "="* 10, "\n")
    nim = input("Masukan NIM anda : ")
    nama = input("Masukan Nama baru anda : ")
    alamat = input("Masukan Alamat baru anda : ")
    
    sql = "UPDATE anggota_kelompok SET nama_mahasiswa=%s, alamat=%s WHERE nim=%s"
    val = (nama, alamat, nim)
    cursor.execute(sql, val)
    
    mydb.commit()
    print("\n=== Data berhasil diubah ===")
    kembali()

def delete():
    print("\n", "="* 10, "Delete Data Mahasisawa", "="* 10, "\n")
    nim = input("Masukan NIM Anda : ")
    sql = "DELETE FROM anggota_kelompok WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql, val)
    mydb.commit()
    print("\n=== Data berhasil dihapus ===")
    kembali()

def search():
    print("\nMasukkan NIM / Alamat / Nama mahasiswa yang akan dicari")
    cari = input("Cari: ")
    cari = "%" + cari + "%"

    sql = "SELECT * FROM anggota_kelompok WHERE nim LIKE %s OR nama_mahasiswa LIKE %s OR alamat LIKE %s"
    val = (cari, cari, cari)
    cursor.execute(sql, val)

    results = cursor.fetchall()

    if cursor.rowcount <= 0:
        print('\n!!! Data tidak di temukan !!!')
    else:
        for data in results:
            print("\n", "="* 10, "Daftar Mahasiswa", "="* 10, "\n")
            print(data)
    kembali()


def kembali():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()
    
while(True):
    show_menu()