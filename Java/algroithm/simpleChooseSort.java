package algroithm;

import java.util.Scanner;

public class simpleChooseSort {

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
		 int length = a.length;
	        for (int i = 0; i < length; i++) {//循环次数
	            int key = a[i];
	            int position=i;
	            for (int j = i + 1; j < length; j++) {//选出最小的值和位置
	                if (a[j] < key) {
	                    key = a[j];
	                    position = j;
	                }
	            }
	            a[position]=a[i];//交换位置
	            a[i]=key;
	        }
     }    

}
