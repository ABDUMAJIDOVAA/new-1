# dictionary part-2

davlat = {
    'davlat' : 'Uzbekistan',
    'viloyat_soni':13,
    'viloyatlar':['Andijon', 'Farg`ona', 'Namangan']
}
# 1
davlat['viloyat_soni']=len(davlat['viloyatlar'])
viloyat_nomi = input('_')
davlat['viloyatlar'].append(viloyat_nomi)
# 2
davlat['viloyatlar'].sort()
# 3
davlat['viloyatlar']=list(map(lambda x:x.upper(), davlat['viloyatlar']))
print(davlat)b