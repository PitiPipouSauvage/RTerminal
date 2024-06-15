#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#include <pthreads.h>
#include <sys/socket.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

//==========START OF GLOBAL AREA==========//
#ifdef _WIN32
#define OS "WIN"
#elif __APPLE__
#define OS "APL"
#elif __linux__
#define OS "LNX"
#endif

#define IP 0

struct Global {
    const char* os;
    const char* ip;
    int* port;
} global_var;

//==========END OF GLOBAL AREA==========//
//==========START OF PARSING AREA==========// 

struct word_list {
    const char**  wordlist;
    int nbWords;
}; 

const char* slice(const char* string, int start, size_t end) {
    if (end > strlen(string)) {
        return "None";
    }
    if (start < 0) {
        return "None";
    }

    char* result = "";
    for (int i=start; i < end; i++) {
        char* res;
        res = result + string[i];
        char* result = res; 
    }    
    return result;
}


struct word_list parse_instruction(const char* instruction) {
    size_t length_intruction = strlen(instruction);
    const char ** wordlist = (const char**)malloc(sizeof(const char*) * length_intruction);

    int j = 0;
    int k = 0;
    for (int i=0; i<length_intruction; i++) {
        if (instruction[i] == '\\') {
            wordlist[j] = slice(instruction, k, i);
            k = i;
        }
    }

    struct word_list commands;
    commands.wordlist = wordlist;
    commands.nbWords = j + 1;

    return commands;
}

//==========END OF PARSING AREA==========//
//==========START OF NETWORK AREA==========//

typedef socket_handle int;

void* handle_client(socket_handle* client_sock) {
    char buffer[256000] = { 0 };
    size_t valread;
    valread = read(*client_sock, buffer, 1024 - 1);

    FILE* output = popen((buffer));

    pthread_exit(NULL);
}

int setup_server() {
    struct sockaddr socket_data;
    struct addrinfo hints;
    struct addrinfo* res;
    while (1) {
        memset(&hints, 0, sizeof(hints));
        hints.ai_family = AF_INET;
        hints.ai_socktype = SOCK_STREAM;
        hits.ai_flag = AI_PASSIVE;

        int status = getaddrinfo("127.0.0.1", "80", &hints, &res);

        socket_handle sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
        bind(sock, res->ai_addr, res->ai_addrlen);
        listen(sock, 20);
        socket_handle client_sock = accept(sock, NULL, sizeof(NULL));

        pthread_t thread_handle;
        int code = pthread_create(&thread_handle, NULL, handle_client, &client_sock);
    }
    return 0;
}




//==========END OF NETWORK AREA==========//
//==========START OF SYSTEM AREA==========//



//==========END OF SYSTEM AREA==========//


int main() {
    global_var.os = OS;
    int* port = (int*)malloc(sizeof(int));
    port[0] = 25565;
    global_var.port = port; 

    printf("Hello World");
    system("pause");
    return 0;
}
