#include <stdio.h>
#include "../include/session.h"
#include <stddef.h>

__attribute__((visibility("default")))

void save_session(Session s){
    FILE *file = fopen("Sessions.bin", "ab");
    if (file != NULL){
        fwrite(&s, sizeof(Session), 1, file);
        fclose(file);
    }
}