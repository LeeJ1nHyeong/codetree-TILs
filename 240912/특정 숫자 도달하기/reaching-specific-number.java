import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] numbers = br.readLine().split(" ");

        int sum = 0;
        int count = 0;
        for (int i = 0; i < 10; i++) {
            int number = Integer.parseInt(numbers[i]);

            if (number >= 250) {
                break;
            }

            sum += number;
            count++;
        }

        double average = (double) sum / count;
        System.out.println(sum + " " + average);
    }
}