barang = {'kd_barang': '001', 'barang' : 'Laptop'  , 'harga': 785000}
print('harga barang',barang.get('harga'))
print('harga barang',barang['harga'])
print('harga barang',barang['kategori'])
print('kategori barang',barang.get('kategori'))
barang['kategori'] = 'komputer'
print(barang)
barang['harga'] = 8250000
print(barang)
