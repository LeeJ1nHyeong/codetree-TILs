import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] scores = br.readLine().split(" ");

        double sum = 0;

        for (int i = 0; i < n; i++) {
            double score = Double.parseDouble(scores[i]);

            sum += score;
        }

        double average = (double) (sum / n);
        System.out.println(String.format("%.1f", average));

        if (average >= 4.0) {
            System.out.println("Perfect");
        } else if (average >= 3.0) {
            System.out.println("Good");
        } else {
            System.out.println("Poor");
        }
    }
}