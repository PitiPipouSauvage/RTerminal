#include <bits/pthreadtypes.h>
#include <netinet/in.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define SO_KEEPALIVE 9;

struct word_list {
    const char **  wordlist;
    int nbWords;
}

const char* slice(const char* string, int start, int end) {
    if (end > strlen(string)) {
        return "None";
    }
    if (start < 0) {
        return "None";
    }

    const char* result = "";
    for (int i=start; i < end; i++) {
        const char* result = result + string[i] 
    }    
    return result;
}


word_list parse_instruction(const char* instruction) {
    int length_intruction = strlen(instruction);
    const char ** wordlist = (const char **)malloc(sizeof(const char*) * length_intruction);

    int j = 0;
    for (int i=0; i<length_intruction; i++) {
        if (instruction[i] == '/') {
            word_list[j];
        }
    }
}


int main() {
    int server_fd;
    int buffer = 2048;
    struct sockaddr_in server_addr;

    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(25566);

    bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)); 
    listen(server_fd, 10);

    while (1) {
        struct sockaddr_in client_addr;
        socklen_t client_addr_len = sizeof(client_addr);
        int *client_fd = malloc(sizeof(int));

        *client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_addr_len);
        char answer[buffer]; 
        read(server_fd, answer, buffer);
        
    }

    return 0;
}

