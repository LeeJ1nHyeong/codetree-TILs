import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());

            System.out.print(num * num + " ");
        }
    }
}