#include <curl/curl.h>
#include <stdlib.h>
#include <stdio.h>


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


int main() {
	
	const char** files = (const char**)malloc(sizeof(const char*)*2);
#ifdef __linux__
	files[0] = "client";
	files[1] = "updater";
#elif _WIN32
	files[0] = "client.exe";
	files[1] = "updater.exe";
#elif __APPLE__
	files[0] = "apple_client";
	files[1] = "apple_updater";
#endif
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

