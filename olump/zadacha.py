#Task1
"""
Кайталоосуз бардык үндүү латын тамгаларынан турган S сабын кайтарып берүүчүү
MakeStr(const S:string):string,функциясын иштеп чыккыла. Бул функциянын жардамы менен
киргизилген ар бир сап үчүн саптын бардык үндүү латын тамгаларын кайталоосуз чыгаргыла.
Үндүү тамгалар: aeiouyAEIOUY.
"""
def string(s):
    for letter in 'BCDFGHJKLMNPQRSTVWXZbcdfglklmnpqrstvwxz':
        s = s.replace(letter,'')
    return(s)
print(string("Menin atym Ramazan"))
