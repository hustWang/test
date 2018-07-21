import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.lang.Math;
/*
 * �༭����
 * Edit Distance
 * �ֳ�Levenshtein���룬��ָ�����ִ�֮�䣬��һ��ת����һ����������ٱ༭����������
 * �༭����������һ���ַ��滻����һ���ַ�������һ���ַ���ɾ��һ���ַ���
 * һ����˵���༭����ԽС�������������ƶ�Խ��
 */

public class editDistance {

	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		/*List<String> list = new ArrayList<String>();
		for (int i=0;i<2;i++){
			
			list.add(input.nextLine());
			
		}*/
		String str1 = input.next();
		String str2 = input.next();
		//String str1 = list.get(0);
		//String str2 = list.get(1);
		
		
		/*ArrayList s1=new ArrayList();
		ArrayList s2=new ArrayList();*/
		int[][] ed ;
		/*for(int i=0;i<str1.length();i++){
			s1.add(str1.charAt(i));
		}
		for(int i=0;i<str2.length();i++){
			s2.add(str2.charAt(i));
		}*/
		
		//ed = new int[s1.size()+1][s2.size()+1];
		ed = new int[str1.length()+1][str2.length()+1];

		for(int i=0;i<=str1.length();i++){ 
			ed[i][0]=i;
		}
		for(int j=0;j<=str2.length();j++){
			ed[0][j]=j;
		}
		
		for(int j=1;j<=str2.length();j++){
			for(int i=1;i<=str1.length();i++){
				if(str1.charAt(i-1)==str2.charAt(j-1)){
					ed[i][j]=Math.min(ed[i-1][j]+1,Math.min(ed[i][j-1]+1,ed[i-1][j-1]));
				}else{
					ed[i][j]=Math.min(ed[i-1][j]+1,Math.min(ed[i][j-1]+1,ed[i-1][j-1]+1));
				}
			}
		}
		for(int i=0;i<str1.length()+1;i++){
			for(int j=0;j<str2.length()+1;j++){
				System.out.print(ed[i][j]);
			}
			System.out.println(" ");
		}
		System.out.println(ed[str1.length()][str2.length()]);
	}
}
