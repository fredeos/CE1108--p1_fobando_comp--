# Cifrado TEA para F32IS.
# La llave de 128 bits vive en vault[4] y las operaciones criptograficas
# se ejecutan dentro de una funcion segura.

int tea_cipher0;
int tea_cipher1;

@secure(0xBEEF0)
func int tea_encrypt(int[] v, vault[4] key){
    int v0 = v[0];
    int v1 = v[1];
    int delta = 0x9e;
    int sum = 0;
    int i = 0;

    delta = (delta << 8) | 0x37;
    delta = (delta << 8) | 0x79;
    delta = (delta << 8) | 0xb9;

    while (i < 32) {
        sum += delta;
        v0 += ((v1 << 4) + key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + key[1]);
        v1 += ((v0 << 4) + key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + key[3]);
        i += 1;
    }

    v[0] = v0;
    v[1] = v1;
    ret 0;
}

@secure(0xBEEF0)
func void main(){
    int block[2];
    vault[4] key;

    block[0] = 100;
    block[1] = 200;

    key[0] = 1;
    key[1] = 2;
    key[2] = 3;
    key[3] = 4;

    tea_encrypt(block, key);

    tea_cipher0 = block[0];
    tea_cipher1 = block[1];
}
