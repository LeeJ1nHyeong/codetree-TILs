import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] date = br.readLine().split("-");

        String month = date[0];
        String day = date[1];
        String year = date[2];

        System.out.println(year + "." + month + "." + day);
    }
}