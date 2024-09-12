import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] numArr = new int[10];
        String[] numbers = br.readLine().split(" ");

        for (int i = 0; i < 10; i++) {
            numArr[i] = Integer.parseInt(numbers[i]);
        }

        int answer = numArr[2] + numArr[4] + numArr[9];
        System.out.println(answer);
    }
}