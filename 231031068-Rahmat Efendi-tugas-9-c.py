vd = {'key1' : 'Nilai 1',
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3'
      }
print(vd)
print(len(vd))
 
#Mengakses Dictionary
print(vd.get('key1'))
print(vd['key1'])

print('\n')

data = {'nama'   : 'Thomas',
        'nim'    : 'B2023001',
        'lulus'  : False
        }
print(data)
#mengakses data
print(data['nama'])
print(data['nim'])
print(data['lulus'])
print()
#mengupdate dan menambah data
# data.update({'nama':'Dimas'})
# data['nama'] = 'Dimas'
print(data)

# Menghapus data
del data['nim']
print(data)

#Nested Dictionary

kuliah = {'nama'   : 'Thomas',
          'nim'    : 'B2023001',
          'nilai'  : [89,93,95],
          'matkul' : {'mk1' : 'Pemrograman',
                      'mk2' : 'Kalkulus Dasar',
                      'mk3' : 'Pancasila'
                      }
        }
print(kuliah)

print(kuliah['matkul']['mk2'])
print(kuliah['nilai'][1])

print(kuliah['matkul'].keys()) # melihat seluruh keys


kuliah['matkul']['mk4'] = 'Sains Terpadu'

print(kuliah['matkul'].values()) # melihat seluruh nilai/value
# kuliah['matkul'].update({'mk4':'Sains Terpadu'})

print(kuliah)

print()
Biodata={ "nama"     : "Rahmat Efendi",
          "nim"      : 231031068,
          "kelas"    : "SI23-C",
          "alamat"   : "Barru",
          "ttl"      : " 01-Mei-2005",
          "kampus"   : "institut teknologi bj habibie",
          "hobi"     : "Volly",
          "minuman favorit" : "Le Minerale",
          "makanan favorit" : "Bakso"
          }
print(Biodata)
print(Biodata["nama"])
print(Biodata["nim"])
print(Biodata["kelas"])
print(Biodata["alamat"])
          
