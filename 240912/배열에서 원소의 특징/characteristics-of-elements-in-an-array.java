import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int[] numArr = new int[10];

        for (int i = 0; i < 10; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (num % 3 == 0) {
                System.out.println(numArr[i - 1]);
                break;
            }

            numArr[i] = num;
        }
    }
}