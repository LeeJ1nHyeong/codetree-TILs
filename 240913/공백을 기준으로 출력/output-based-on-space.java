import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");

        for (int i = 0; i < s.length; i++) {
            System.out.print(s[i]);
        }

        s = br.readLine().split(" ");
        for (int i = 0; i < s.length; i++) {
            System.out.print(s[i]);
        }

    }
}