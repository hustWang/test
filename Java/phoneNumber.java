package t_0718;
/*
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
     给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
     示例：
     输入："23"
     输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
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
