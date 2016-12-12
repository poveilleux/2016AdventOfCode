import java.security.*;

public class Day5 {
    
    public static void main(String[] args) throws Exception {
        System.out.println(findPassword("abc"));
        System.out.println(findPassword("wtnhxymk"));
    }
    
    private static String findPassword(String doorId) throws Exception {
        String password = "";
        
        int index = 0;
        while (password.length() != 8) {
            String message = doorId + Integer.toString(index);
            byte[] data = message.getBytes("UTF-8");
            byte[] hash = md5Hash(data);
            String hexHash = bytesToHex(hash);
            
            if (hexHash.startsWith("00000")) {
                password += hexHash.charAt(5);
            }
            
            index++;
        }
        
        return password;
    }
    
    private static byte[] md5Hash(byte[] data) throws Exception {
        MessageDigest md5 = MessageDigest.getInstance("MD5");
        return md5.digest(data);
    }
     
    final protected static char[] hexArray = "0123456789ABCDEF".toCharArray();
    private static String bytesToHex(byte[] bytes) {
        char[] hexChars = new char[bytes.length * 2];
        for ( int j = 0; j < bytes.length; j++ ) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = hexArray[v >>> 4];
            hexChars[j * 2 + 1] = hexArray[v & 0x0F];
        }
        return new String(hexChars);
    }
}