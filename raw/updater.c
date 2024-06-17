#include <bits/pthreadtypes.h>
#include <netinet/in.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

#define SO_KEEPALIVE 9;

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
//==========START OF DOWNLOADING AREA==========//

#define MAX_FILE_SIZE 5120000
#define MAX_FILENAME_SIZE 32


void downloader(const char* url, const char** file_names) {
    CURL* curl;
    for (int i=0; i<sizeof(file_names) / sizeof(file_names[0]); i++) {
        const char* outfilename = file_names[i];
        curl = curl_easy_init();
        if (curl) {
            FILE* file = fopen(outfilename, "wb");
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);
            curl_easy_perform(curl);
            fclose(file);
        }
        curl_easy_cleanup(curl);
        curl_global_cleanup();
    }
}

//==========END OF DOWNLOADING AREA==========//


int main(int argc, char* argv[]) {
    char** files = (const char**)malloc(sizeof(const char*)*(argc - 1));
    for (int i=1; i < argc; i++) {
        files[i] = argv[i];
    }

    char* url = "127.0.0.1";
    downloader(url, files);

#ifdef __linux__
    system("./client");
#elif _WIN32
    system(".\\client.exe");
#elif __APPLE__
    system("./apple_client");
#endif
    return 0;
}

