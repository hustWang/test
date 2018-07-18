package t_0718;
/*
 * ����һ������������ 2-9 ���ַ����������������ܱ�ʾ����ĸ��ϡ�
     �������ֵ���ĸ��ӳ�����£���绰������ͬ����ע�� 1 ����Ӧ�κ���ĸ��
     ʾ����
     ���룺"23"
     �����["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class phoneNumber {

	String[] dict = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<String>();
        if(digits == null || digits.length()==0){
            return res;
        }
        backTracking(new StringBuilder(),digits,0,res);
        return res;

    }
    private void backTracking(StringBuilder temp,String digits,int index,List<String> res){
        if(temp.length() == digits.length()){
            res.add(temp.toString());
            return;
        }
        for(int i=0;i<dict[digits.charAt(index) - '0'].length();i++){
            temp.append(dict[digits.charAt(index)-'0'].charAt(i));
            backTracking(temp,digits,index+1,res);
            if(temp.length()>0){
                temp.deleteCharAt(temp.length()-1);
            }
        }
    }
    
    @org.junit.Test
    public void Test() {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();
        List<String> res0 = letterCombinations(num);
        System.out.println(res0);
        System.out.println(res0.size());
    }
}
