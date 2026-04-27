int global_result;

func void llenar(int[] datos){
    datos[0] = 10;
    datos[1] = 20;
    datos[2] = 30;
    datos[3] = 40;
}

func int sumar4(int[] datos){
    int total = 0;
    total = datos[0] + datos[1];
    total += datos[2];
    total += datos[3];
    ret total;
}

@secure(0x21)
func int mezclar(int a, int b, int c){
    int x = (a ^ b) ^ c;
    ret x;
}
