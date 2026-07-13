class Solution {
    public int strStr(String haystack, String needle) {
        if (!haystack.contains(needle)) return -1;

        int count = 0;
        int index = 0;
        int startIndex = 0;
        int needleLength = needle.length();
        int haystackLength = haystack.length();

        while(haystackLength > index && count < needleLength) {
            char h = haystack.charAt(index);
            char n = needle.charAt(count);
            
            if (h == n) {
                if (count == 0) startIndex = index;
                count++;
                index++;
            } else if (count != 0) {
                count = 0;
                index = startIndex + 1;
            } else {
                index++;
            }
        }

        if (count == needleLength) {
            return startIndex;
        } else {
            return -1;
        }
    }
}