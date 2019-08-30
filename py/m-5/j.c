#include <stdio.h>
int main() {
    int qtos, a, b, n;
  scanf("%d", &qtos);
    if(qtos >= 1 && qtos <= 1000){
        for (int i = 0; i < qtos; i++) {
            scanf("%d %d %d", &a, &b, &n);
            if(a >= 0 && b >= 0 && n >= 0){
                if (n % 3 == 0)
                printf("%d\n", a);
                else if (n % 3 == 1)
                    printf("%d\n", b);
                else
                printf("%d\n", a ^ b);
            }
        }
    }
    return 0;
}