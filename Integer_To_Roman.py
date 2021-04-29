class Solution:
    def intToRoman(self, num: int) -> str:
        #5 --> 5-1  --> IV
        #9 --> 10-1 --> IX
        #40 -> 50-10 -> XL
        #90 -> 100-10 -> XC
        #400 -> 500-100 -> CD
        #900 -> 1000-100 -> CM
        
        conversions = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
            
        }
        
        #We can consider one digit at a time
        roman_number = ""
        for k, v in conversions.items():
            occurences = num // k
            roman_number = roman_number + v*occurences
            num = num % k
        return roman_number
    
    #time comlexity O(N), we iterate over each character in our int.
    #Space complexity O(1), since conversion hashMap does not grow as input size grows.
            
        
        