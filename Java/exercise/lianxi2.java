package test;
/*
 * 假定每个小朋友只知道有多少同学和自己拿到了相同颜色的糖果。
上课后，有一部分小朋友兴奋的把这一结果告诉小明老师，并让小明老师猜一猜，最少有多少同学拿到了糖果。
例如有三个小朋友告诉小明老师这一结果如下：
其中第一个小朋友发现有1人和自己糖果颜色一样，第二个小朋友也发现有1人和自己糖果颜色一样，第三个小朋友发现有3人和自己糖果颜色一样。
第一二个小朋友可互相认为对方和自己颜色相同，比如红色；
第三个小朋友不可能再为红色（否则第一二个小朋友会发现有2人和自己糖果颜色相同），假设他拿到的为蓝色糖果，那么至少还有另外3位同学拿到蓝色的糖果，最终至少有6位小朋友拿到了糖果。
现在请你帮助小明老师解答下这个谜题。

输入描述:
假定部分小朋友的回答用空格间隔，如 1 1 3

输出描述:
直接打印最少有多少位小朋友拿到糖果
如 6
 * 
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
//注意多位数的条件
public class lianxi2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		List<Integer> list = new ArrayList<Integer>();
		List<Integer> list1 = new ArrayList<Integer>();
		List<Integer> list2 = new ArrayList<Integer>();
		
		//String s = scan.nextLine().replace(" ", "");//去掉空格
		
		/*int a[] = new int[s.length()];
		for(int i=0;i<s.length();i++){
			a[i]=s.charAt(i)-'0';
		}*/
		
		while(scan.hasNextInt()){
			list.add(scan.nextInt());
		}
		int a[]=new int[list.size()];
		for(int i=0;i<list.size();i++){
			a[i]=list.get(i);
		}
		
		int sum =0;
		for(int i = 0;i<a.length;i++){
			if(list1.contains(a[i])){
				int m = list1.indexOf(a[i]);//获得list中指定元素的位置
			
				if(a[i]==0){
					sum=sum+1;
				}else if(list2.get(m)==(a[i]-1)){
					list2.set(m, -1);
				}else if(list2.get(m)==(-1)){
					sum=sum+a[i]+1;
					list2.set(m, list2.get(m)+1);
				}else{
					list2.set(m, list2.get(m)+1);
					//sum=sum+1;
				}
			}else{
				sum = sum+a[i]+1;
				list1.add(a[i]);
				list2.add(0);
			}
		} 
		System.out.println(sum);
		}

	

}
