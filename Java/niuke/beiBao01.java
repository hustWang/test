package niuke;

import java.util.Scanner;

public class beiBao01 {

    @org.junit.Test
    public void test() {
    	Scanner input = new Scanner(System.in); 
    	
	    int n =5;
	    //对3,4,5,6这种带逗号的格式的处理
	    //先读取全部一行，去掉逗号，放入数组，将每个字符转换为整型。
	    String p1 = input.nextLine();
	    String w1 = input.nextLine();
	    int m = input.nextInt();

	    String []array1 = p1.split(",");
	    String []array2 = w1.split(",");
        int p[] = new int[n];
        int w[] = new int[n];
        
        for(int i=0;i<p.length;i++){
        	p[i]=Integer.parseInt(array1[i]);
        
        }
        
        for(int j=0;j<w.length;j++){
        	w[j]=Integer.parseInt(array2[j]);
   
        }
        //int[] v = {6,3,5,4,6};
        //int[] w = {2,2,6,5,4};
        //压缩容量
        //packOptimal(m, w, p);
        //不压缩容量
        int c[][] = BackPack_Solution(m,n,w,p);
        for (int i = 1; i <=n; i++) {
            for (int j = 1; j <=m; j++) {
                System.out.print(c[i][j]+"\t");
                if(j==m){
                    System.out.println();
                }
            }
        }
    }

    /**
     * 01背包-容量压缩
     *
     * @param c      包容量
     * @param weight 各物品质量
     * @param value  各物品价值
     */
    public void packOptimal(int c, int[] weight, int[] value) {
        int n = weight.length; //物品数量
        int[] w = new int[n + 1];
        int[] v = new int[n + 1];
        int[][] G = new int[n + 1][c + 1];
        for (int i = 1; i < n + 1; i++) {
            w[i] = weight[i - 1];
            v[i] = value[i - 1];
        }

        //初始化values[0...c]=0————在不超过背包容量的情况下，最多能获得多少价值
        //原因：如果背包并非必须被装满，那么任何容量的背包都有一个合法解“什么都不装”，这个解的价值为0，
        //所以初始时状态的值也就全部为0了
        int[] values = new int[c + 1];
        
        for (int i = 1; i < n + 1; i++) {
            for (int t = c; t >= w[i]; t--) {
                if (values[t] < values[t - w[i]] + v[i]) {
                    values[t] = values[t - w[i]] + v[i];
                    G[i][t] = 1;
                }
            }
        }
        System.out.println("最大价值为： " + values[c]);
        System.out.print("装入背包的物品编号为： ");
        /*
        输出顺序:逆序输出物品编号
        注意：这里另外开辟数组G[i][v],标记上一个状态的位置
        G[i][v] = 1:表示物品i放入背包了，上一状态为G[i - 1][v - w[i]]
        G[i][v] = 0:表示物品i没有放入背包，上一状态为G[i - 1][v]
        */
        int i = n;
        int j = c;
        while (i > 0) {
            if (G[i][j] == 1) {
                System.out.print(i + " ");
                j -= w[i];
            }
            i--;
        }
    }
    
    /*
     * 01背包-不压缩容量
     * @param m 表示背包的最大容量
     * @param n 表示商品个数
     * @param w 表示商品重量数组
     * @param p 表示商品价值数组
     */
    public static int[][] BackPack_Solution(int m, int n, int[] w, int[] p) {
        //c[i][v]表示前i件物品恰放入一个重量为m的背包可以获得的最大价值
        int c[][] = new int[n + 1][m + 1];
        for (int i = 0; i < n + 1; i++)
            c[i][0] = 0;
        for (int j = 0; j < m + 1; j++)
            c[0][j] = 0;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                //当物品为i件重量为j时，如果第i件的重量(w[i-1])小于重量j时，c[i][j]为下列两种情况之一：
                //(1)物品i不放入背包中，所以c[i][j]为c[i-1][j]的值
                //(2)物品i放入背包中，则背包剩余重量为j-w[i-1],所以c[i][j]为c[i-1][j-w[i-1]]的值加上当前物品i的价值
                if (w[i - 1] <= j) {
                    if (c[i - 1][j] < (c[i - 1][j - w[i - 1]] + p[i - 1]))
                        c[i][j] = c[i - 1][j - w[i - 1]] + p[i - 1];
                    else
                        c[i][j] = c[i - 1][j];
                } else
                    c[i][j] = c[i - 1][j];
            }
        }
        return c;
    }
    
    
}