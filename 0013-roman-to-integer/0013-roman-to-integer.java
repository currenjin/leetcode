class Solution {
    public int romanToInt(String s) {
        int result = 0;
        HashMap<Character, Integer> symbolNumber = new HashMap<Character, Integer>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};

        for (int i = 0; i < s.length() - 1; i++) {
            if (symbolNumber.get(s.charAt(i)) < symbolNumber.get(s.charAt(i + 1))) {
                result -= symbolNumber.get(s.charAt(i));
            } else {
                result += symbolNumber.get(s.charAt(i));
            }
        }

        return result + symbolNumber.get(s.charAt(s.length() - 1));
    }
}
