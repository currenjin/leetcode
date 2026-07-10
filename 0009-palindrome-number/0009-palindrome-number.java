class Solution {
    public boolean isPalindrome(int x) {
        String stringX = String.valueOf(x);
        int length = stringX.length();
        if (length == 1) return true;
        
        int middleLength = length / 2;
        if (length % 2 == 1) {
            String stringFirst = stringX.substring(0, middleLength + 1);
            String stringSecond = stringX.substring(middleLength, length);
            return stringFirst.equals(new StringBuffer(stringSecond).reverse().toString());
        }

        String stringFirst = stringX.substring(0, middleLength);
        String stringSecond = stringX.substring(middleLength, length);
        return stringFirst.equals(new StringBuffer(stringSecond).reverse().toString());
    }
}