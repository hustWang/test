/*
 一个抽奖游戏,有7个连续整数的球(比如1,2,3,4,5,6,7),连续随机抽取3个,如果连续抽取的两个球是连续的,
 则中奖,问中奖几率多大?

结果 11/21

数学方法 
因为连续抽取三个数，如果连续抽取的两个是连续的则中奖分为两种情况 
思路先组合在排列 
①三个数直接连续 如123 本身又有6种变化 ，又因连续有5种 5*6=30种
A(3,3)*5 = 60

②有且只有两个数是连续 如 12 4 本身有4种变化 所以为 20*4=80种
因为取三个数所以边上两个是特殊的所以为 
2*C(1,4)*A(2,2)*A(2,2)+4*C(1,3)*A(2,2)*A(2,2) = 80
共计110种

总结：如果连续抽取三个那么边上两个就是特殊情况需要区别对待，如果抽取4个那么边上三个要区别对待，
在判断连续情况要分情况讨论，如果连续两个，但是抽取三个会出现连续三个和连续两个的情况。
那么抽取N个呢，连续M个呢，那么有 M到N共 (N-M)种情况需要区别对待。
 * 
 */
package t_0718;

import org.junit.Test;

public class pickBall {

	public void printArray(int[] array) {
		//因为不知道有几个
        //先遍历数组
        int time = 0;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                for (int k = 0; k < array.length; k++) {
                    if (array[i] != array[k] && array[j] != array[k] && array[i] != array[j]) {
                        System.out.println(array[i] + "," + array[j] + "," + array[k]);
                        time++;
                    }
                }
            }
        }
        //time为计算有多少种
        int[][] rank = new int[time][3];
        time = 0;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                for (int k = 0; k < array.length; k++) {
                    if (array[i] != array[k] && array[j] != array[k] && array[i] != array[j]) {
                        rank[time][0] = array[i];
                        rank[time][1] = array[j];
                        rank[time][2] = array[k];
                        time++;
                    }
                }
            }
        }
        System.out.println("共计" + time + "种情况");
        //上面为二次遍历赋值ֵ


        System.out.println("现在输出符合连续的情况");
        time=0;
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                for (int k = 0; k < array.length; k++) {
                    if (array[i] != array[k] && array[j] != array[k] && array[i] != array[j]) {
                        if(Math.abs(array[i]-array[j])==1||Math.abs(array[j]-array[k])==1){
                            System.out.println(array[i] + "," + array[j] + "," + array[k]);
                            time++;
                        }

                    }
                }
            }
        }
        System.out.println("共计" + time + "种情况");
    }

    @Test
    public void Test() {
        int[] array = {1, 2, 3, 4, 5, 6, 7};
        printArray(array);
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
