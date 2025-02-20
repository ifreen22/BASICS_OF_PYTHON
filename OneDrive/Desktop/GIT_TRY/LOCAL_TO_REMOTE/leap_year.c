#include<stdio.h>
int main(){

// Check the given year is a leap year or not?

int year;
printf("enter the year : ");
scanf("%d", &year);

if(year % 100 ==0){
    if(year % 400 == 0){
        printf("Yes, the given year is a leap year");
    }

    else{
        printf("No, the given year is not a leap year"); 
    }
}

else if(year % 4 ==0){
    printf("Yes, the given year is a leap year");
}

else {
    printf("No, the given year is not a leap year"); 
}
    



    return 0;
}