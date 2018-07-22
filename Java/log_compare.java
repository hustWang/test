import java.util.Scanner;

public class log_compare {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		int y = input.nextInt();
		if((y*Math.log10(x)) > (x*Math.log10(y))){
			System.out.println(">");
		}else if((y*Math.log10(x)) == (x*Math.log10(y))){
			System.out.println("=");
		}else{
			System.out.println("<");
		}
	}

}
