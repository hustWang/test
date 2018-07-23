package algroithm;

import java.util.Scanner;

public class bubbleSort {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] a= new int[n];
        for(int i =0;i<n;i++){
           a[i]=input.nextInt();
        }
        Sort(a);
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }

	}
	
	 public static void Sort(int[] a){
		 int length=a.length;
	        int temp;
	        for(int i=0;i<a.length;i++){
	            for(int j=0;j<a.length-i-1;j++){
	                if(a[j]>a[j+1]){
	                    temp=a[j];
	                    a[j]=a[j+1];
	                    a[j+1]=temp;
	                }
	            }
	        }
     }    

}
