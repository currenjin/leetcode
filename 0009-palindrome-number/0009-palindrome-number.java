class Solution {
    public boolean isPalindrome(int x) {
        String stringX = String.valueOf(x);
        int length = stringX.length();
        if (length == 1) return true;

        for (int i=0; i<length/2; i++) {
            if (stringX.charAt(i) != stringX.charAt(length-i-1)) return false;
        }

        return true;
    }
}