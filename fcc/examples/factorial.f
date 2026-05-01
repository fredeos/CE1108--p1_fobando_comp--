int global_result;
func int factorial(int a){
    int resultado = 1;
    int i = 1;

    while (i <= a) {
        resultado = resultado * i;
        i += 1;
    }
    ret resultado;
}

func void main(){
    global_result = factorial(5);
}