int global_base;

func int suma(int a, int b){
    int r = a + b;
    ret r;
}

func int cuadrado(int x){
    ret x * x;
}

@secure(0x21)
func int ajuste_seguro(int x){
    int y = x + 5;
    ret y;
}

@secure(0x44)
func int mezcla_segura(int a, int b, int c){
    int y = (a ^ b) ^ c;
    ret y;
}
