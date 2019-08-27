#include <stdio.h>
#include <stdlib.h>
#define true 1
typedef enum week{
    Mon = 1,
    Tues = 2,
    Wed = 3,
    Thurs = 4,
    Fri = 5,
    Sat = 6,
    Sun = 7
 }week;
typedef struct planeINFO{
    char planeID[10];
    char startStation[10];
    char endStation[10];
    week depature;
}planeINFO;
typedef struct planeSet{
    planeINFO fligtINFO;
    int       flightTICKETS;
}planeSet;

void uploadFiles(char *fileName){
    FILE *fp;
    char ch;
    if((fp=fopen(fileName,'w'))==NULL){
        printf("cannot open this file\n");
        exit(0);
    }
    getchar();
}

void main(){
    char fileName[] = "planeSchedule";
    printf("%s",fileName);
}