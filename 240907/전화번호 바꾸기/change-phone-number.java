import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] phoneNumber = br.readLine().split("-");

        System.out.println(phoneNumber[0] + "-" + phoneNumber[2] + "-" + phoneNumber[1]);
    }
}