1#
fio_person ="Eraliev Marat Bolotovich".upper()
name,surname,midlname=fio_person[:7],fio_person[8:13],fio_person[14:24]
print(f"Name:{name}"
      f"\nSurname:{surname}"
      f"\nMiddlnmame:{midlname}")
print(fio_person)
print(len(fio_person))
#2
text="Bishkek"
text_2="city"+" "+text
print(text_2)
#3
text_5="Привет, как дела?"
print(text_5[::-1])
#4
text8="I like living in Bishkek"
tex_6=text8.lower()
print(tex_6)
print(text8.count("i"))
print(text8.count("k"))
text0=text8[:7]+" driving in Tokyo"
print(text0)
print(text8[:10])
text1=text8[2:13]
print(text1)
