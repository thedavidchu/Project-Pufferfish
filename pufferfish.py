"""
# Count Puffer Fish

## Purpose

Gonzalo (i.e. Gonzalo Martinez Santos) and I have been sending fufferfish emojis
back and forth. However, we increment the number of pufferfish emojis is
incremented by one every time someone sends a packet.

E.g. If I were to send 14 pufferfish, Gonzalo should respond with 15 pufferfish.

N.B. Interrupting someone's pufferfish message means they must start over.

## Functionality
Count the number of puffer fish characters in a string and return a string of
pufferfish delimited by '\n' plus one more pufferfish.

## TODO
- Make only one input to the class for the type of character to print
- Make attributes private
- Debug

## Note
This was done as a joke. I am freezing the code as of 2021-04-15 21:45.

"""

class Pufferfish():
    def __init__(self, number_of_pufferfish: int = 0, pufferfish_ord: int = None, pufferfish_chr: str = None):

        # Define pufferfish constants
        if pufferfish_ord is None:
            self.pufferfish_ord = 128033
        else:
            assert isinstance(pufferfish_ord, int)
            assert pufferfish_ord >= 0
            self.pufferfish_ord = pufferfish_ord

        if pufferfish_chr is None:
            self.pufferfish_chr = chr(128033)
        else:
            assert isinstance(pufferfish_chr, str)
        
        # Ensure that the _ord_ and _chr_ match
        assert chr(self.pufferfish_ord) == self.pufferfish_chr
        
        # Define the number of pufferfish
        assert isinstance(number_of_pufferfish, int)
        assert number_of_pufferfish >= 0
        self.number_of_pufferfish = number_of_pufferfish
        
        return

    def __str__(self, number_of_pufferfish: int = None, show: bool = False) -> str:
        if number_of_pufferfish is None:
            number_of_pufferfish = self.number_of_pufferfish

        pufferfish = '\n'.join([self.pufferfish_chr for i in range(number_of_pufferfish)])

        if show:
            print(pufferfish)

        return pufferfish

    def __call__(self, number_of_pufferfish: int = None, show: bool = False) -> str:
        """
        Return the number of pufferfish requested.

        :param number_of_pufferfish: int (default: self.number_of_pufferfish) -
        the number of pufferfish to print. The default is the internal state of
        pufferfish. (i.e. previous number printed).
        :param show: bool (default: False) - whether to print the pufferfish.

        :return: str - a '\n' delimited string with the number of pufferfish requested.
        """

        return self.__str__(number_of_pufferfish, show)

    # ============================== MATH OPERATIONS ============================== #
    def __ensure_same_species(self, other):
        """
        Ensure the _ord_ of both self and other pufferfish are the same.
        """
        if self.pufferfish_ord == other.pufferfish_ord:
            return
        else:
            raise TypeError

    def __add__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish + other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish + other.number_of_pufferfish
        else:
            raise TypeError
        
        return Pufferfish(new_value, self.pufferfish_ord)
        

    def __sub__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish - other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish - other.number_of_pufferfish
        else:
            raise TypeError
        
        return Pufferfish(new_value, self.pufferfish_ord)

    def __mul__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish * other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish * other.number_of_pufferfish
        else:
            raise TypeError
        
        return Pufferfish(new_value, self.pufferfish_ord)

    def __floordiv__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish // other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish // other.number_of_pufferfish
        else:
            raise TypeError
        
        return Pufferfish(new_value, self.pufferfish_ord)

    def __mod__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish % other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish % other.number_of_pufferfish
        else:
            raise TypeError
        
        return Pufferfish(new_value, self.pufferfish_ord)

    def __pow__(self, other: int):
        if isinstance(other, int):
            new_value = self.number_of_pufferfish ** other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            new_value = self.number_of_pufferfish ** other.number_of_pufferfish
        else:
            raise TypeError
        return Pufferfish(new_value, self.pufferfish_ord)
    
    # OPERATE ON SELF
    def __iadd__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish += other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish += other.number_of_pufferfish
        else:
            raise TypeError
        return self

    def __isub__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish -= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish -= other.number_of_pufferfish
        else:
            raise TypeError
        return self

    def __imul__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish *= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish *= other.number_of_pufferfish
        else:
            raise TypeError
        return self

    def __ifloordiv__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish //= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish //= other.number_of_pufferfish
        else:
            raise TypeError
        return self

    def __imod__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish %= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish %= other.number_of_pufferfish
        else:
            raise TypeError
        return self

    def __ipow__(self, other: int):
        if isinstance(other, int):
            self.number_of_pufferfish **= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            self.number_of_pufferfish **= other.number_of_pufferfish
        else:
            raise TypeError
        return self
    
    # Comparison Operators
    def __lt__(self, other: int) -> bool:
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish < other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish < other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    def __le__(self, other: int) -> bool:
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish <= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish <= other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    def __eq__(self, other: int) -> bool:
        """
        TODO: if the type doesn't match maybe just return False
        """
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish == other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish == other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    def __ne__(self, other: int) -> bool:
        """
        TODO: if the type doesn't match maybe just return True
        """
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish != other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish != other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    def __ge__(self, other: int) -> bool:
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish >= other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish >= other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    def __gt__(self, other: int) -> bool:
        if isinstance(other, int):
            bool_value = self.number_of_pufferfish > other
        elif isinstance(other, Pufferfish):
            self.__ensure_same_species(other)
            bool_value = self.number_of_pufferfish > other.number_of_pufferfish
        else:
            raise TypeError
        return bool_value

    # ============================== USER DEFINED FUNCTIONS ============================== #
    def __get_text(self, text: str = None) -> str:
        # Print message
        if text is not None:
            print(text, end='')

        # Get each line of text
        raw_text = []
        while True:
            line = input()
            if line:
                raw_text.append(line)
            else:
                break

        # Join lines of list into '\n' delimited string
        return '\n'.join(raw_text)


    def increment(self, raw_text: str = None) -> str:
        """
        Take in a message of pufferfish and return a '\n' delimited message with one
        more pufferfish.

        :param raw_text: str (default: None) - the input message containing the
        pufferfish that you wish to one-up (literally).
            - N.B. If not provided, you will be prompted for it.

        :return: str - a '\n' delimited string with one more pufferfish than the
        input has.
        """

        # Get the pufferfish text
        if raw_text is None:
            raw_text = self.__get_text('Please paste the previous pufferfish message here:\n')

        # Count the number of pufferfish
        count = raw_text.count(self.pufferfish_chr)

        # Increment internal pufferfish counter
        self.number_of_pufferfish = count + 1

        return '\n'.join([self.pufferfish_chr for i in range(self.number_of_pufferfish)])
    
    
    def check(self, raw_text_one: str = None, raw_text_two: str = None):
        """
        Check that two consecutive messages have the correct number of pufferfish.

        :param raw_text_one: str (default: None) - the first pufferfish message
        :param raw_text_two: str (default: None) - the second pufferfish message

        :return: bool - whether this is a valid sequence of pufferfish.
        """

        # Get the pufferfish text
        if raw_text_one is None:
            raw_text_one = self.__get_text('Please paste the first pufferfish message here:\n')
        if raw_text_two is None:
            raw_text_two = self.__get_text('Please paste the second pufferfish message here:\n')

        count_one = raw_text_one.count(self.pufferfish_chr)
        count_two = raw_text_two.count(self.pufferfish_chr)

        print(count_one, count_two)

        return (count_one + 1 == count_two)


if __name__ == '__main__':
    p, q = Pufferfish(), Pufferfish()
    
    # TODO: Debug
    
