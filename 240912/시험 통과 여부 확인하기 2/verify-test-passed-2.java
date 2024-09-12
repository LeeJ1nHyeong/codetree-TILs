import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int passCount = 0;

        for (int i = 0; i < n; i++) {
            String[] scores = br.readLine().split(" ");
            int sum = 0;

            for (int j = 0; j < 4; j++) {
                int score = Integer.parseInt(scores[j]);
                sum += score;
            }

            double average = (double) sum / 4.0;

            if (average >= 60) {
                System.out.println("pass");
                passCount++;
            } else {
                System.out.println("fail");
            }
        }

        System.out.println(passCount);
    }
}