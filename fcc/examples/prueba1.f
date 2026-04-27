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
