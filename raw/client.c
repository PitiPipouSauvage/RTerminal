#include <arpa/inet.h>
#include <netinet/in.h>
#include <netdb.h>
#include <pthread.h>
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
    char**  wordlist;
    int nbWords;
}; 

char* slice(char* string, int start, size_t end) {
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


struct word_list split(char* instruction, char* separator) {
    size_t length_intruction = strlen(instruction);
    char ** wordlist = (char**)malloc(sizeof(char*) * length_intruction);

    int j = 0;
    int k = 0;
    for (int i=0; i<length_intruction; i++) {
        if (instruction[i] == (char)*separator) {
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
//==========START OF FUNCTIONALITY AREA==========//

void cam() {
    return NULL;
}

//==========END OF FUNCTIONALITY AREA==========//
//==========START OF NETWORK AREA==========//

typedef int socket_handle;
struct associative_array {
    struct word_list keys;
    struct word_list values;
}

void* handle_client(void* client_sock_void) {
    struct word_list keywords;
    keywords.wordlist = (char**)malloc(sizeof(char*) * 1);
    keywords.wordlist[0] = "cam";
    keywords.nbWords = 1;

    struct word_list funcs;
    funcs.wordlist = (char**)malloc(sizeof(char*) * 1);
    void (*camPtr)();
    camPtr = &cam;
    funcs.wordlist[0] = camPtr;
    funcs.nbWords = 1;    

    struct associative_array commands;
    commands.keys = keywords;
    commands.values = funcs;

	int client_sock = *((int*) client_sock_void);
    char buffer[256000] = { 0 };
    size_t valread;
    valread = read(client_sock, buffer, 1024 - 1);

	char* command= buffer;
	struct word_list splitted_command;
	splitted_command = split(command, "-");

    for (int i=0; i<commands.keys.nbWords; i++) {
        if (splitted_command[0] == commands.keys.wordlist[i]) {
            *commands.values.wordlist[i];
        }
    }
	
	char* tags = malloc(sizeof(char) * (splitted_command.nbWords - 1));
	for (int i=1; i<splitted_command.nbWords; i++) {
		strcat(tags, splitted_command.wordlist[i]);
	}

	char* output = malloc(sizeof(char) * 2048);
    FILE* output_file = popen(buffer, tags);
	fread(output, 1024, 2, output_file);

	send(client_sock, output, strlen(output), 0);
	
	close(client_sock);
	free(output);
	free(tags);
    
	for (int i=0; i<splitted_command.nbWords; i++) {
		free(splitted_command.wordlist[i]);
	}

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
        hints.ai_flags = AI_PASSIVE;

        int status = getaddrinfo("127.0.0.1", "80", &hints, &res);

        socket_handle sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
        bind(sock, res->ai_addr, res->ai_addrlen);
        listen(sock, 20);
        socket_handle client_sock = accept(sock, NULL, (int *)sizeof(NULL));

		void* client_sock_void = &client_sock;
        pthread_t thread_handle;
        int code = pthread_create(&thread_handle, NULL, &handle_client, client_sock_void);
    }
    return 0;
}

//==========END OF NETWORK AREA==========//

int main() {
    global_var.os = OS;
    int* port = (int*)malloc(sizeof(int));
    port[0] = 25565;
    global_var.port = port; 

	int status = setup_server(); 
    return 0;
}

