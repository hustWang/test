package t_0718;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * �ַ���������ϣ��Ե�������
 * nextInt()�ڶ�ȡ����󽫹�����ͬһ���С�
 * next()�����ܶ������ɿո�ָ��ĵ��ʡ����⣬�ڶ�ȡ����󽫹�����ͬһ���� �� 
 * nextline()�ڶ�ȡ����֮�󣬽���������һ�С�
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
