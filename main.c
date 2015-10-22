#include <stdio.h>
#include <stdlib.h>
#include "fomalib.h"

int main(int argc, char *argv[]) {
    if (argc <= 2) {
        printf("Usage: segment foo.foma 'stringtosegment'\n");
        exit(1);
    }

    struct fsm *net;
    struct apply_handle *ah;
    char *result;

    char *filename = argv[1];

    net = fsm_read_binary_file(filename);
    if (net == NULL) {
        perror("Error loading file");
        exit(EXIT_FAILURE);
    }
    ah = apply_init(net);
    //printf("%s\n", argv[1]);
    char *str = argv[2];
    result = apply_down(ah, str);
    while (result != NULL) {
        printf("%s\n", result);
        result = apply_down(ah, NULL);
    }
    apply_clear(ah);
    fsm_destroy(net);
}