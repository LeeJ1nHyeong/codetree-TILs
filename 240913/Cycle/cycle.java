import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        int n = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        int[] visited = new int[n + 1];

        int number = n;
        visited[number] = 1;
        while (true) {
            if (visited[number] == 3) {
                break;
            }

            number = (number * n) % p;
            visited[number] += 1;
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] >= 2) {
                count++;
            }
        }

        System.out.println(count);
    }
}