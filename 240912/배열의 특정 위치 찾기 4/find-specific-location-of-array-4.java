import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] numbers = br.readLine().split(" ");

        int count = 0;
        int sum = 0;

        for (int i = 0; i < 10; i++) {
            int number = Integer.parseInt(numbers[i]);

            if (number == 0) {
                break;
            }

            if (number % 2 == 0) {
                count++;
                sum += number;
            }
        }

        System.out.println(count + " " + sum);
    }
}