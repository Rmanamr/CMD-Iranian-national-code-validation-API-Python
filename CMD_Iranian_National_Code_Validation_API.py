"""Python CMD program for validating Iranian national codes with an API request.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

import requests

def main():
     """
     main function for interacting with the user
     """
     while(True):
     # while loop to keep the program running

        print("Please enter the Iranian national code that you want to be validated (Type x or X to exit):") 
        raw_Input = input()
        if raw_Input.lower() == 'x':
            break
        
        input_Number = int(raw_Input)
        # reading the next integer number

        result = Iranian_National_Code_Validator_API(input_Number)
        # passing the input_Number to the Iranian_National_Code_Validator function to validate it
        # and storing the result in result variable

        print(result)
        print("*******************************************************************************************") 


def Iranian_National_Code_Validator_API(input_Number):
    """
    function for validating the Iranian national code with an API request.
    @param number: an Iranian national code
    @type number: integer
    @return: Result
    @rtype: String
    @examples: 
     >>> Iranian_National_Code_Validator_API(5890614592)
         The code is valid
     >>> Iranian_National_Code_Validator_API(48656)
         The number of digits is incorrect  
     >>> Iranian_National_Code_Validator_API(8676863554351530)
         The number of digits is incorrect 
    """ 
    url = f"https://api.codebazan.ir/codemelli/?code="
    Iranian_National_Code = "" + str(input_Number)
    response = requests.get(f"https://api.codebazan.ir/codemelli/?code={Iranian_National_Code}")
    response_JSON = response.json()
    return response_JSON['Result']


if __name__ == '__main__':
    main()
    # run the main function after executing this file