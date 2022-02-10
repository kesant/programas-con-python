#funcion para obtener el nombre del dominio de una direccion url
def domain_name(url):
    import re 
    #utilizamos expresiones regulares para poder obtener el dominio en los posibles casos
    obj2 = re.findall('www.([\w\-\.]+)',url) 
    obj1 = re.findall('://www.([\w\-\.]+)',url) 
    obj = re.findall('://([\w\-\.]+)',url)
    obj3 = re.findall('([\w\-\.]+)',url) 
    #verificamos las condicionales y obtenemos solo el nombre del dominio
    if len(obj2)!=0:
        indice=obj2[0].find(".")
        return obj2[0][:indice]
    elif len(obj1)!=0:
        indice=obj1[0].find(".")
        return obj1[0][:indice]
    elif len(obj)!=0:
        indice=obj[0].find(".")
        return obj[0][:indice]
    elif len(obj3)!=0:
        indice=obj3[0].find(".")
        return obj3[0][:indice]

if __name__=="__main__":
   domain_name("www.xakep.ru")
