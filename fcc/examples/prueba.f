traigase "prueba1.f"

func void main(){
    int i = 0;
    int total = 0;

    for (int j = 0; j += 1; j < 4) {
        total += suma(j, 1);
    }

    while (i < 3) {
        total += cuadrado(i);
        i += 1;
    }

    total += ajuste_seguro(total);
    total += mezcla_segura(total, 7, 3);

    if (total > 20) {
        global_base = total;
    } elif (total == 20) {
        global_base = 20;
    } else {
        global_base = 0;
    }
}
