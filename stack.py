# =========================== Stack ==============================
# By : Dendy Julianata M - 170411100040

# Stack: Kumpulan item yang dipesan di mana penambahan item baru dan penghapusan item yang sudah ada selalu terjadi di ujung yang sama. Ujung ini biasanya 
# disebut sebagai "atas." Ujung yang berlawanan atas dikenal sebagai "basis." Prinsip pemesanan ini kadang-kadang disebut LIFO.

# Stack(), membuat stack(tumpukan) baru yang kosong.
# push(data), menambahkan data baru pada posisi top dari stack.
# pop(), menghapus data di posisi top dari stack.
# peek(), informasi letak data.
# isEmpty(), memeriksa apa stack dalam keadaan kosong atau tidak.
# size(), informasi jumlah data dalam stack.


# Contoh Syntax :

def stack():
    st = []
    return(st)
def push(st,data):
    st.append(data)
def pop():
    data = st.pop()
    return(data)
def peek(st):
    return(st[len(st)-1])
def isEmpty(st):
    return(st==[])
def size(st):
    return(len(st))

st = stack()
push(st,100)

# Program Membalikkan kata

kata=input("Masukkan Kata = ")
st=stack()
hasil=""
for i in range(len(kata)):
    push(st,kata[i])
for i in range(len(kata)):
    hasil=hasil + pop()
print(hasil)

# Program Konversi Bilangan Desimal ke Biner

angka = int(input("Masukkan Angka = "))
st = stack()
hasilbagi = angka
hasil = 0
while hasilbagi>0:
    temp = hasilbagi%2
    push(st,temp)
    hasilbagi = hasilbagi//2
temp = ""
while not(isEmpty(st)):
    temp = temp+str(pop())
print(temp)