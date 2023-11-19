
NO_OF_CHARS = 256
def canFormPalindrome(st):
        count = [0] * (NO_OF_CHARS)
        for i in range(0, len(st)):
            count[ord(st[i])] = count[ord(st[i])] + 1
        odd = 0
        for i in range(0, NO_OF_CHARS):
            if (count[i] & 1):
                odd += 1
            if (odd > 1):
                return False
        return True

class NearPalindromesDiv1():
    
    @classmethod
    def Solve(string, input):
        total_steps = 0
        if canFormPalindrome(input):
            return total_steps
        alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        temporal_total_steps = list('')
        for i in range(0, int(len(input))): 
                input_list = list(input)   
                print(input_list)
                temporal_total_steps.append(0)     
                char_position = 0
                for j in range (26):
                    char_position += 1
                    if (alphabeth[j] == input_list[i]):
                        print("posicion:", char_position, ' - caracter:', alphabeth[j])
                        break                
                for j in range (26):      
                    temporal_total_steps[i] += 1    
                    input_list[i] = alphabeth[char_position]
                    temp_input = "".join(input_list)
                    if (canFormPalindrome(temp_input)):
                        break
                    char_position += 1
                    if char_position > 25:
                        char_position = char_position - 26    
        temporal_total_steps.sort()
        total_steps = temporal_total_steps[0]
        return total_steps
        
result = NearPalindromesDiv1.Solve("daddy")
print (result)