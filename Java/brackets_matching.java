package t_0718;

import java.util.Scanner;
import java.util.Stack;

/*
 * ����ƥ��
 */
public class brackets_matching {

	public static void main(String[] args) {  
        Scanner sc = new Scanner(System.in);  
          
        int n= sc.nextInt();
          
        Stack<Character> stack = null;  
          
        while(n!=0){  
              
            //�ӿ���̨����һ�������ַ���[]() [(])  
            String str = sc.next();  
            //����������ַ���Ϊ������˵����ƥ��  
            if(str.length() % 2 == 1){  
                System.out.println("No");  
            }else{  
                //˵���ַ���ż��  
                stack = new Stack<Character>();  
                for(int i=0;i<str.length();i++){  
                    if(stack.isEmpty()){  
                        //���ջ�ǿյ�  
                        stack.push(str.charAt(i));  
                    }else if(stack.peek() == '[' && str.charAt(i) == ']' || stack.peek() == '(' && str.charAt(i) == ')'
                    		|| stack.peek() == '{' && str.charAt(i) == '}'){  
                        //˵����ʱջ���ַ����ǿյ�,���ҷ��ϣ�  
                        stack.pop();  
                    }else{  
                          
                        stack.push(str.charAt(i));  
                    }  
                }  
                  
                if(stack.isEmpty()){  
                    //���ջ�ǿյģ�˵������ƥ��  
                    System.out.println("Yes");  
                }else{  
                    //˵��ջ��Ϊ�գ����Ų�ƥ��  
                    System.out.println("No");  
                }  
            }  
              
            n--;  
        }  
          
    }  

}
