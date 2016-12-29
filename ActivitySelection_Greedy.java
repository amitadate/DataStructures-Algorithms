import java.util.*;
import java.lang.*;
import java.io.*;

class ActivitySelection{
    public static void printMaxActivities(int start[], int finish[]){
        int n=start.length;
        //sort(start,finish);
        System.out.print("AFollowing activities are selected : \n");
        int i=0;
        System.out.print(i+" ");
        for(int j=1;j<n;j++){
            if(start[j]>=finish[i]){
                System.out.print(j+" ");
                i=j;
            }
        }
    }
    
    public static void main(String[] args){
        int start[]={1, 3, 0, 5, 8, 5};
        int finish[]={2, 4, 6, 7, 9, 9};
        printMaxActivities(start, finish);
    }
}
