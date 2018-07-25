package algroithm;

import java.util.Scanner;

public class quickSort {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] a= new int[n];
        for(int i =0;i<n;i++){
           a[i]=input.nextInt();
        }
        
        int start = 0;
        int end = a.length-1;
        
        Sort(a,start,end);
        for(int i=0;i<a.length;i++){
            System.out.print(a[i]+" ");
        }
	}
	
	public static void Sort(int[] numbers, int start, int end) {   
	    if (start < end) {   
	        int base = numbers[start]; // 选定的基准值（第一个数值作为基准值）   
	        int temp; // 记录临时中间值   
	        int i = start, j = end;   
	        do {   
	            while ((numbers[i] < base) && (i < end))   
	                i++;   
	            while ((numbers[j] > base) && (j > start))   
	                j--;   
	            /*第一种：从前到后和从后往前分别与基准值比较，分别找到是否有需要交换值.
	             * 如果有，分别和基准值交换位置，算作一遍循环。
	             * 第二种：前后指针分别与基准值比较，找到需要交换的值，前后指针对应的值交换
	             * 此程序使用的是第二种。
	             * 
	             * 前后指针相遇的位置为该轮结束时基准值的位置。
	             */
	            if (i <= j) {   
	                temp = numbers[i];   
	                numbers[i] = numbers[j];   
	                numbers[j] = temp;   
	                i++;   
	                j--;   
	            }   
	        } while (i <= j);   
	        if (start < j)   
	            Sort(numbers, start, j);   
	        if (end > i)   
	            Sort(numbers, i, end);   
	    }   
	}  

}
