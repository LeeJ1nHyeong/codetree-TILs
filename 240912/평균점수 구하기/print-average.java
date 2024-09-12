import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] scores = br.readLine().split(" ");
        
        double sum = 0;
        for (int i = 0; i < 8; i++) {
            double score = Double.parseDouble(scores[i]);
            sum += score;
        }

        double average = (double) (sum / 8);
        System.out.println(String.format("%.1f", average));
    }
}