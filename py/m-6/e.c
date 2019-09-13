#include <stdio.h>
int main() {
    int qtos;
    int n;
    int v[10000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
             scanf("%d", &qtos);
        for (int i = 0; i < qtos; i++) {
            scanf("%d", &v[i]);
        }
     }
    return 0;
}