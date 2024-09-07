import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String time = br.readLine();
        String[] timeArr = time.split(":");

        int h = Integer.parseInt(timeArr[0]) + 1;
        int m = Integer.parseInt(timeArr[1]);

        System.out.println(h + ":" + m);
    }
}