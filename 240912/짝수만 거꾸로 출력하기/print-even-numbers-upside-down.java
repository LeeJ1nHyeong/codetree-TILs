import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numArr = new int[n];
        String[] numbers = br.readLine().split(" ");

        for (int i = 0; i < n; i++) {
            numArr[i] = Integer.parseInt(numbers[i]);
        }

        for (int i = n - 1; i >= 0; i--) {
            if (numArr[i] % 2 == 0) {
                System.out.print(numArr[i] + " ");
            }
        }
    }
}