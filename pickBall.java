/*
 һ���齱��Ϸ,��7��������������(����1,2,3,4,5,6,7),���������ȡ3��,���������ȡ����������������,
 ���н�,���н����ʶ��?

��� 11/21

��ѧ���� 
��Ϊ������ȡ�����������������ȡ�����������������н���Ϊ������� 
˼·����������� 
��������ֱ������ ��123 ��������6�ֱ仯 ������������5�� 5*6=30��
A(3,3)*5 = 60
������� 
������ֻ�������������� �� 12 4 ������4�ֱ仯 ����Ϊ 20*4=80��
2*C(1,4)*A(2,2)*A(2,2)+4*C(1,3)*A(2,2)*A(2,2) = 80
��Ϊȡ���������Ա������������������Ϊ 
�������=80 
����110��

�ܽ᣺���������ȡ������ô���������������������Ҫ����Դ��������ȡ4����ô��������Ҫ����Դ���
���ж��������Ҫ��������ۣ�����������������ǳ�ȡ����������������������������������
��ô��ȡN���أ�����M���أ���ô�� M��N�� (N-M)�������Ҫ����Դ���
 * 
 */
package t_0718;

import org.junit.Test;

public class pickBall {

	public void printArray(int[] array) {
        //��Ϊ��֪���м���
        //�ȱ�������
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
        //timeΪ�����ж�����
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
        System.out.println("����" + time + "�����");
        //����Ϊ���α�����ֵ


        System.out.println("��������������������");
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
        System.out.println("����" + time + "�����");
        //�������ж�
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
