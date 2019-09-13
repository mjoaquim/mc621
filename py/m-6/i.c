#include <stdio.h>
int main() {
    int qtos;
    scanf("%d", &qtos);
    int aux = 0;
    if(qtos > 0 && qtos < 5001)
        for (int i = 1; i < qtos+1; i++) {
            for (int j = i ; j < qtos+1; j++){
                if(((i+j) <= qtos && ((i*j) <= qtos)) || ((i == 1) && ((i+j) <= qtos+1) && (i*j<=qtos))){
                    aux++;
                }
            }
            
        }
    printf("%d\n", aux);
    return 0;
}