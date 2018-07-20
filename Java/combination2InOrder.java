package t_0718;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * 字符串两两组合，对调算两种
 * nextInt()在读取输入后将光标放在同一行中。
 * next()它不能读两个由空格分隔的单词。另外，在读取输入后将光标放在同一行中 。 
 * nextline()在读取输入之后，将光标放在下一行。
 */
public class combination2InOrder {
	
	public static void main(String[] args) {
		
		List<String> comb1 = new ArrayList<String>();
		List<String> comb2 = new ArrayList<String>();
		List<String> combL = new ArrayList<String>();
		Scanner input = new Scanner(System.in);
		
		int n = input.nextInt();
		for (int i=0;i<=n;i++){
			
			String str = input.nextLine();
			
			comb1.add(str);
			comb2.add(str);
		}
			
		play(comb1,comb2,combL);
		
	    }
	
	private static void play(List<String> list1,List<String> list2,
			List<String> list3){
		int time = 0;
		for (int i=0;i<list1.size();i++){
			for(int j=0;j<list2.size();j++){
				if(j!=i){
					String str1 = list1.get(i)+list2.get(j);
					list3.add(str1);
					time++;
				}
				
			}
		}
		System.out.println(list3);
		System.out.println(time);
	}
	
	
	
	
}
