class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("I",1);
        map.put("IV",4);
        map.put("V",5);
        map.put("IX",9);
        map.put("X",10);
        map.put("XL",40);
        map.put("L",50);
        map.put("XC",90);
        map.put("C",100);
        map.put("CD",400);
        map.put("D",500);
        map.put("CM",900);
        map.put("M",1000);
        
        int ptr = 0;
        char peek;
        int total = 0;
        
        for (int i = 0; i < s.length(); i++){
            ptr++;
            if (ptr < s.length()){
                peek = s.charAt(ptr);
                String together = Character.toString(s.charAt(i)) + Character.toString(peek);
                if (map.containsKey(together)){
                    total += map.get(together);
                    i++;
                    ptr++;
                    continue;
                }
                else{
                    total += map.get(Character.toString(s.charAt(i)));
                }
            }
            else{
                total += map.get(Character.toString(s.charAt(i)));
            }
        }
                                     
        return total;
    }
}
