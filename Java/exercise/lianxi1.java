package test;

import java.util.Scanner;
//注意考虑边界条件，跨行的情况。
/*
 * 现在你需要用一台规定的打字机书写一封书信。信的每行只能容纳宽度为100的字符，也就是说如果写下某个字符会导致行宽超过100，那么就要另起一行书写
信的内容由a-z的26个小写字母构成，而每个字母的宽度均会事先约定。例如字符宽度约定为[1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]，
那么就代表'a'到'd'四个字母的宽度分别是1,2,3,4，而'e'到'z'的宽度均为5
那么按照上述规则将给定内容S书写成一封信后，这封信共有几行？最后一行宽度是多少？

输入描述:
输入为两行：
第一行是存储了每个字符宽度的字符串，包含26个数字，以1个空格分隔，每个数字均小于等于10
第二行是存储了待输入字符的字符串S，字符串S的长度在1到1000之间


输出描述:
输出为信的行数以及最后一行所包含的字符个数，中间以1个空格分隔
 */
public class lianxi1 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int a[]= new int[26];
		for(int i=0;i<26;i++){
		   a[i]=input.nextInt();
		}
		
		String s = input.next();
		
		int count=0;
		int line = 1;
		for(int i=0;i<s.length();i++){
			//每个字符与字符a的差。
			int index = s.charAt(i)-'a';
			if(count<=100&&(count+a[index])>100){
				line++;
				count = 0;
			}
			count = count+a[index];
			if(i==(s.length()-1)){
				System.out.println( line+" "+count);
			}
		}
		
	}

}
