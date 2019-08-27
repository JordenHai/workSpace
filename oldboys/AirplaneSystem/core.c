/*
'''
2、飞机订票 系统设计
假定民航机场共有n个航班，
每个航班有一航班号、
确定的航线(起始站、终点站)、
确定的飞行时间(星期几)
和一定的成员订额。
试设计一民航订票系统，使之能提供下列服务:
(1)航班信息录入功能(航班信息用文件保存)
(2)航班信息浏览功能
(3)查询航线:
按航班号查询，按终点站查询
(4)承勒订票和退票业务
'''
*/
/*#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    FILE *fp;
    char ch;
    if((fp=fopen("123.txt","r"))==NULL)
        printf("file cannot open \n");
    else
        printf("file opened for writing \n");
    while((ch=fgetc(fp))!=EOF)
        fputc(ch,stdout); //这里是输出到屏幕
    if(fclose(fp)!=0)
        printf("file cannot be closed \n");
    else
        printf("file is now closed \n");
    return 0;
}
*/
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
void menu(){

    printf(" ◤       ************************       ◥\n");
    printf("┃              飞机订票系统              ▕\n");
    printf("┃        ************************       ▕\n");
    printf("┃              ★ 航线录入(1)            ▕\n");
    printf("┃              ★ 航线浏览(2)            ▕\n");
    printf("┃              ★ 航线查询(3)            ▕\n");
    printf("┃              ★ 订票请按(4)            ▕\n");
    printf("┃              ★ 退票请按(5)            ▕\n");
    printf("┃              ★ 系统退出(6)            ▕\n");
    printf(" ◣                                      ◢\n");

}
//
void loadFiles(char *fileName,planeSet *plane){
    FILE *fp;
    char ch;
    planeINFO p;

    if((fp=fopen(fileName,'r'))==NULL){

        printf("cannot open the file\n");

    }else{
        rewind(fp);
        printf("file opened for writing \n");
    }

    while((ch = fgetc(fp))!=EOF){
    }
}

/*
10013#beijing#taijing#1#200！10013 shanghai hangzhou 2 300！！

*/
void uploadFiles(char *fileName,planeSet *plane){
    FILE *fp;
    planeINFO p;
    char ch;
    if((fp=fopen(fileName,'w'))==NULL){
        printf("cannot open this file\n");
        exit(0);
    }
    getchar();

    p = plane->
    ch =

}

//录入航班信息
void entryFight(planeSet *f){
    planeINFO p;

}

int main(){
    int choice;
    planeSet f,*fp;
    fp = &f;
    while(true){
        menu();
        printf("请输入选项：\n");
        scanf("%d",&choice);
        getchar();
        switch(choice){
            case 1:
                entryFight(f);
                break;
            case 2:
                break;
            case 3:
                break;
            case 4:
                break;
            case 5:
                break;
            case 6:
            default:
                break;
        }
    }

}


