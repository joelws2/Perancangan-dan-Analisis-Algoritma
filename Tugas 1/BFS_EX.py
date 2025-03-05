def bfs(graf, simpul_awal):
    antrian = []  # Inisialisasi antrian
    dikunjungi = set()  # Himpunan untuk melacak simpul yang telah dikunjungi

    # Tambahkan simpul awal ke antrian dan tandai sebagai dikunjungi
    antrian.append(simpul_awal)
    dikunjungi.add(simpul_awal)

    # Selama antrian tidak kosong
    while antrian:
        # Keluarkan simpul dari depan antrian
        simpul = antrian.pop(0)
        print(simpul, end=' ')

        # Periksa setiap tetangga dari simpul saat ini
        for tetangga in graf[simpul]:
            if tetangga not in dikunjungi:
                antrian.append(tetangga)
                dikunjungi.add(tetangga)

# Contoh penggunaan
graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Hasil penelusuran BFS:")
bfs(graf, 'A')
