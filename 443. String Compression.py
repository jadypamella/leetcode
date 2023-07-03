# URL: https://leetcode.com/problems/string-compression/
# Time complexity: O(n)

class Solution:
    def compress(self, chars: List[str]) -> int:

        # initialize the pointers and the counter
        read = 0
        write = 0
        count = 1

        # loop through the array
        while read < len(chars):

            # check if the next character is the same as the current one
            if read + 1 < len(chars) and chars[read] == chars[read + 1]:
                
                # increment the counter
                count += 1
            
            else:
                
                # write the current character
                chars[write] = chars[read]
                write += 1

                # check if the counter is greater than 1
                if count > 1:

                    # convert the counter to a string and write its digits
                    count_str = str(count)
                    for digit in count_str:
                        chars[write] = digit
                        write += 1

                # reset the counter
                count = 1

            # move the reading pointer
            read += 1

        # return the size of the new array 
        return write
