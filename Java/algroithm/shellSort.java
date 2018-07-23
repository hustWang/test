package algroithm;

import java.util.Scanner;

public class shellSort {

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
        	int d  = a.length;
            while (d!=0) {
                d=d/2; 
                System.out.println(d);
                for (int x = 0; x < d; x++) {//分的组数
                    for (int i = x + d; i < a.length; i += d) {//组中的元素，相差d的为一组，从第二个数开始
                        int j = i - d;//j为有序序列最后一位的位数
                        int temp = a[i];//要插入的元素
                        for (; j >= 0 && temp < a[j]; j -= d) {//从后往前遍历。
                            a[j + d] = a[j];//向后移动d位
                        }
                        a[j + d] = temp;
                    }
                }
            }
        }
    }       

