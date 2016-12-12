import java.security.*;

public class HelloWorld {
    
    public static void main(String[] args) throws Exception {
        System.out.println(findPassword("wtnhxymk"));
    }
    
    private static String findPassword(String doorId) throws Exception {
        StringBuilder password = new StringBuilder("________");        
        int index = 0;
        while (password.indexOf("_") >= 0) {
            String message = doorId + Integer.toString(index);
            byte[] data = message.getBytes("UTF-8");
            byte[] hash = md5Hash(data);
            String hexHash = bytesToHex(hash);
            
            if (hexHash.startsWith("00000")) {
                Integer position = Character.getNumericValue(hexHash.charAt(5));
                char c = hexHash.charAt(6);
                
                if (position < 8) {
                    if (password.charAt(position) == '_') {
                        password.setCharAt(position, c);
                    }
                }
            }            
            index++;
        }        
        return password.toString();
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