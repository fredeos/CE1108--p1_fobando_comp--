traigase "math_utils.f"

@secure(0xAB12F)
func int calcular(int a, int b){
    int resultado = 0;
    int temp = a << 2;
    resultado = temp + b;
    ret resultado;
}

func void main(){
    int x = 15;
    int y = 3;
    int z = calcular(x, y);

    bool activo = true;
    char letra = 'k';

    # comentario de una sola línea

    #*
    Este es un comentario
    multilinea bien cerrado.
    Debe ser ignorado por el lexer.
    *#
    

    if (z >= 10){
        z += 1;
    } elif (z == 9){
        z -= 1;
    } else {
        z = z >> 1;
    }

    for (int i = 0; i += 1; i < 5){
        x = x + i;
    }

    while (x > 0){
        x -= 1;
        continue;
    }

    vault clave;
    break
}