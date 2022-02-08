#convertidor de decimal a hexadecimal usando el metodo de division sistemas deigitales
def rgb(r, g, b):
    lista_hexadecimal=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    lista_rgb=[r,g,b]
    output=""
    for i in lista_rgb :      
        if i>255:
            elemento1=15
            elemento2=15
        elif i<0:
            elemento1=0
            elemento2=0
        else :
            elemento1=int(i/16)
            elemento2=int(i%16)
        output+=lista_hexadecimal[elemento1]+lista_hexadecimal[elemento2]
    return output        
    
    
if __name__=="__main__":
   rgb(255,165,175)
