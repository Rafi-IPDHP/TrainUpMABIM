# NIM : 2404777
# ! Nama : Rafi Islami Pasha Dini Hari Putra
# Kelas : RPL 1B
# Kelompok : Kelompok 5 - Aurora

# Input nama pasangan (siapa tau mau input :D)
# suami1 = input("Masukkan nama pasangan 1 (Suami): ")
# istri1 = input("Masukkan nama pasangan 1 (Istri): ")
# suami2 = input("Masukkan nama pasangan 2 (Suami): ")
# istri2 = input("Masukkan nama pasangan 2 (Istri): ")
# suami3 = input("Masukkan nama pasangan 3 (Suami): ")
# istri3 = input("Masukkan nama pasangan 3 (Istri): ")

suami1 = 'P1'
suami2 = 'P2'
suami3 = 'P3'
istri1 = 'I1'
istri2 = 'I2'
istri3 = 'I3'
# Susun pasangan suami istri
pasangan = {
    suami1: istri1,
    suami2: istri2,
    suami3: istri3,
}

# Status awal
pulau_a = [suami1, istri1, suami2, istri2, suami3, istri3]
pulau_b = []
perahu = []

# Cek aturannya dilanggar atau ngga
def is_invalid_state(side):
    for suami in pasangan:
        istri = pasangan[suami]

        # cek kalo istri nya ga sama suaminya di pulau tersebut
        if(istri in side and suami not in side):
            # Cek lagi kalo bener ga ada suaminya, dia sama suami orang atau ngga
            if any(p in side for p in pasangan if p != suami):
                print('gaboleh nih')

def print_state():
    print(f'Pulau A: {pulau_a}')
    print(f'Pulau B: {pulau_b}')
    print(f'Perahu: {perahu}')
    print('-' * 30)

def menyebrang():
    global pulau_a, pulau_b, perahu

    steps = [
        ([istri1, suami1], 'Langkah 1'),
        ([suami1], 'Langkah 2'),        
        ([istri2], 'Langkah 3'),
        ([istri1], 'Langkah 4'),
        ([suami2], 'Langkah 5'),
        ([suami2], 'Langkah 6'),
        ([istri3], 'Langkah 7'),
        ([istri2], 'Langkah 8'),
        ([suami3], 'Langkah 9'),
        ([istri3, suami3], 'Langkah 10'),
    ]

    print_state()

    for step, description in steps:
        print(description)
        if(set(step).issubset(set(pulau_a))):
            for person in step:
                pulau_a.remove(person)
            perahu.extend(step)
        elif(set(step).issubset(perahu)):
            for person in step:
                perahu.remove(person)
            pulau_b.extend(step)

        print_state()

        if(is_invalid_state(pulau_a) or is_invalid_state(pulau_b)):
            print('Aturan dilanggar!!!')
            return

menyebrang()

if(pulau_a == []):
    print("Semua orang berhasil menyeberang dengan aman")
else:
    print('Lahh ada yang ketinggalan')
