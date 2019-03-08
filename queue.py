# =========================== Queues ==============================
# By : Dendy Julianata M - 170411100040

# Queue pada Struktur Data atau antrian adalah sekumpulan data yang mana penambahan elemen hanya bisa dilakukan pada suatu ujung disebut dengan 
# sisibelakang(rear), dan penghapusan(pengambilan elemen) dilakukan lewat ujung lain (disebut dengan sisi depan atau front). 
# Prinsip pemesanan ini kadang-kadang disebut FIFO, masuk pertama keluar pertama.

# Antrian (), membuat antrian baru yang kosong. Tidak perlu parameter dan mengembalikan antrian kosong.
# enqueue (data), menambahkan item baru ke bagian belakang antrian. Perlu item dan tidak mengembalikan apa pun.
# dequeue (), menghapus item depan dari antrian. Tidak perlu parameter dan mengembalikan item. Antrian dimodifikasi.
# isEmpty (), menguji untuk melihat apakah antrian kosong. Tidak perlu parameter dan mengembalikan nilai boolean.
# size (), mengembalikan jumlah item dalam antrian. Tidak perlu parameter dan mengembalikan integer.

# Contoh Sintaks :

def queue():
    q=[]                    
    return (q)
def enqueue(q, data):
    q.insert(0,data)        
    return (q)              
def dequeu(q):
    data = q.pop()         
    return(data)            
def isEmpty(q):
    return(q==[])           
def size(q):
    return (len(q))         

qt = queue()
enqueue(qt, "Matematika")          
enqueue(qt, "Bahasa Inggris")
enqueue(qt, "Algoritma Pemrograman")
print(qt)
print(size(qt))             
dequeu(qt)                  
print(qt)
