#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>

#define MAX_USERNAME_SIZE 16
#define MAX_COMMAND_SIZE 256

#define PORT 12011

char admin_username[] = "no227";

int main() {
    char *username = malloc(MAX_USERNAME_SIZE);

    printf("Enter username : ");
    fgets(username, MAX_USERNAME_SIZE, stdin);

    if ((strlen(username) > 0) && (username[strlen(username) - 1] == '\n'))
        username[strlen(username) - 1] = '\0';

    printf("Enter password : ");


    return 0;
}
