import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

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
		for (int i=0;i<n;i++){
			
			String str = input.next();//此处nextline()会出现空字符
			
			comb1.add(str);
			comb2.add(str);
			combL.add(str);
		}
		//System.out.println(comb1);
		//System.out.println(combL);
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
		//是否需要去重操作
		/*List<String> finallist = new ArrayList<String>();
		for (int i=0;i<list3.size();i++){
			if(!finallist.contains(list3.get(i))){
				finallist.add(list3.get(i));
			}
		}
		
		isbrackets(finallist);*/
		int s = isbrackets(list3);
		
		//System.out.println(finallist);
		System.out.println(s);
	}
	
	private static int isbrackets(List<String> list){
		int right = 0;
		Stack<Character> stack = null;
		for(int m = 0;m<list.size();m++){
			if(list.get(m).length()%2==1){
				continue;
			}else{
				stack = new Stack<Character>();

				for(int i=0;i<list.get(m).length();i++){
					if(stack.isEmpty()){
						stack.push(list.get(m).charAt(i));
					}else if(stack.peek() == '[' && list.get(m).charAt(i)==']'
						  || stack.peek() == '(' && list.get(m).charAt(i)==')'
						  || stack.peek() == '{' && list.get(m).charAt(i)=='}'){
						stack.pop();
					}else{
						stack.push(list.get(m).charAt(i));
					}
				}
				
				if(stack.isEmpty()){  
                    //如果栈是空的，说明括号匹配  
                    System.out.println("Yes");  
                    right++;
                }else{  
                    //说明栈不为空，括号不匹配  
                    System.out.println("No");  
                }  
			}
		}
		return right; 
	}
	
	
}