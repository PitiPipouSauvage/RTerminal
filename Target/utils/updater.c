#include <arpa/inet.h>
#include <dirent.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>


int main(char server_ip[], int server_port) {
    bool noUpdate = True;

    while (noUpdate) {
        int sockfd = socket(int AF_INET, int SOCK_STREAM, 0);
        int setsockopt(int sockfd, int TCP, int SO_KEEPALIVE, const void *optval, socklen_t optlen);
        int bind(int sockfd, const struct sockaddr *server_ip, socklen_t addrlen);

  }

  return 0;
  }

int update(char files[][]) {
    // list files in directory
    char dir[];
    DIR *d;
    struct dirent *dir;
    d = opendir(".");
    id (d) {
    int i = 0;
    while ((dir = readdir(d)) != NULL) {
        dir[i] = dir->d_name;
        i += 1;
    }
    closedir(d);
  }

  return 0;
  }
