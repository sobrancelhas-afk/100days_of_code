a= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

txt = input('input text:\n')
shift = input('encoding shift: ')
e_d = input('encode[1] or decode[2]? ')

def encoder_decoder(txt=txt,shift=shift,e_d=e_d):
  global a
  if e_d == "2":
    a = a[::-1]
  indices = []
  txt_final = ''
  shift = int(shift) % len(a)
  #capturar o indice de cada caracter
  for i in txt:
    if i == " ":
      indices.append(" ")
    else:
      indices.append(a.index(i)) #indexes do input original
  final = [int(x) + int(shift) if x != " " else " " for x in indices] #indexes + encoder ahift
  for c in final: #nova string encodd
    if c == " ":
      txt_final += " "
    else:
      txt_final += a[(c+shift)%len(a)]
  print(txt_final)

encoder_decoder()