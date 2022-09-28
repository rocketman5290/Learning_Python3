Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |      
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |      
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Splitting starts at the end of the string and works to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |      
 |        sep
 |          The separator used to split the string.
 |      
 |          When set to None (the default value), will split on any whitespace
 |          character (including \\n \\r \\t \\f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits (starting from the left).
 |          -1 (the default value) means no limit.
 |      
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

print("hello world")
hello world
name=
SyntaxError: invalid syntax
name = "william george"
print(name)
william george
print(name.strip(1)
      )
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(name.strip(1)
TypeError: strip arg must be None or str
print(name.strip())
          
william george
name
          
'william george'
name.pop'william george'
          
SyntaxError: invalid syntax
name.pop
          
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name.pop
AttributeError: 'str' object has no attribute 'pop'
help
          
Type help() for interactive help, or help(object) for help about object.
help()
          

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>   quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
x = z
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x = z
NameError: name 'z' is not defined
x = name
x = z
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x = z
NameError: name 'z' is not defined
z = x
print(z)
william george
x = z + "everett"
print(x)
william georgeeverett
def print_nums(n):
    i = 1
    while i <= n:
        print(i, end='\t')
        i += 1

        

def print_nums(n):
    i = 1
    while i <= n:
        print(i, end='\t')
        i += 1

        
def print_nums(n):
    i = 1
    while i <= n:
        print(i, end='\t')
        i += 1

        
print_nums(9)
1	2	3	4	5	6	7	8	9	
print_nums(15)
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	
print_nums(50)
1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	
a_really_long_string_solution = 'This is the solution for a really long string. What you want to do is use a backslash to help break the line and allow it to continue. Make sure \
never complete the quote on the first line but wrap the whole sentence or expression with a single set of wrapping quotes'
print(a_really_long_string_solution)
This is the solution for a really long string. What you want to do is use a backslash to help break the line and allow it to continue. Make sure never complete the quote on the first line but wrap the whole sentence or expression with a single set of wrapping quotes
my_string_with_backslash = 'I am typing a backslash: \\ \
in a long line.'
print(my_string_with_backslash)
I am typing a backslash: \ in a long line.

print(my_string_with_backslash)
I am typing a backslash: \ in a long line.
def to_power(n,power):
    print(n ** power)

    
to_power(2,20)
1048576
to_power(2, 2.3)
4.924577653379664
to_power(2,20)
1048576
5 == 5
True
5 != 5
False
class(False)
SyntaxError: invalid syntax
type(False)
<class 'bool'>
type(3)
<class 'int'>
type(3.3)
<class 'float'>
type([1,2,3])
<class 'list'>
type("william")
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax












seven_to_fortyth_power = 7**40
print(seven_to_fortyth_power)
6366805760909027985741435139224001
seven_to_foryth_power
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    seven_to_foryth_power
NameError: name 'seven_to_foryth_power' is not defined. Did you mean: 'seven_to_fortyth_power'?
seven_to_fortyth_power
6366805760909027985741435139224001
def calc_div_exercise
SyntaxError: invalid syntax
def calc_div_exercise(n,div)
SyntaxError: expected ':'
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0
    
SyntaxError: expected ':'
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
        if g == 0
        
SyntaxError: unexpected indent
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0
    
SyntaxError: expected ':'
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0:
        print(g + 1)
        elif g != 0:
            
SyntaxError: invalid syntax
def calc_div_exercise(n,div):
    n = 1
    g = (10 ** 100) + 1
    g = (g + n) % 13
    if g == 0:
        print(g)
    elif g != 0:
        n ++
        g = g + n
        
SyntaxError: invalid syntax
def calc_div_exercise(n,div):
    n = 1
    g = (10 ** 100) + 1
    g = (g + n) % div
    if g == 0:
        print(g)
    else g != 0:
        n += 1
        self.cacl_div_exercise(n,div)
        
SyntaxError: expected ':'
def calc_div_exercise(n,div):
    n = 1
    g = (10 ** 100) + 1
    g = (g + n) % div
    if g == 0:
        print(g)
    else g != 0:
        n += 1
        self.cacl_div_exercise(n,div):
            
SyntaxError: expected ':'
def calc_div_exercise(n,div):
    n = 1
    g = (10 ** 100) + 1
    g = (g + n) % div
    if g == 0:
        print(g)
    else g != 0:
        n += 1
        self.cacl_div_exercise(n,div)
        
SyntaxError: expected ':'
[DEBUG ON]
[DEBUG ON]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
[DEBUG ON]

[DEBUG ON]
[DEBUG OFF]
name
'william george'
help
Type help() for interactive help, or help(object) for help about object.
help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number



============ RESTART: C:/Users/rocketman5290/Desktop/helloworld.py ===========
William George
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0:
        print(g + 1)
        elif g != 0:
            
SyntaxError: invalid syntax
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0:
        print(g + 1)
        elif g != 0
        
SyntaxError: invalid syntax
def calc_div_exercise(n,div):
    g = 10 ** 100
    g = (g + 1) % 13
    if g == 0:
        print(g)
    elif g != 0:
        g += 1

calc_div_exercise(1,13)
def calc_div_exercise(n = 1):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        g += 1
        calc_div_exercise(n)
    else:
      print('try again')

calc_div_exercise(1)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    calc_div_exercise(1)
  File "<pyshell#110>", line 9, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#110>", line 9, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#110>", line 9, in calc_div_exercise
    calc_div_exercise(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#110>", line 5, in calc_div_exercise
    if a == 0:
RecursionError: maximum recursion depth exceeded in comparison
def calc_div_exercise(n = 1):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
        calc_div_exercise(n)

        
calc_div_exercise(1)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    calc_div_exercise(1)
  File "<pyshell#113>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#113>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#113>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#113>", line 5, in calc_div_exercise
    if a == 0:
RecursionError: maximum recursion depth exceeded in comparison
def calc_div_exercise(n = 1):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
        self.calc_div_exercise(n)

        
calc_div_exercise(1)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    calc_div_exercise(1)
  File "<pyshell#116>", line 10, in calc_div_exercise
    self.calc_div_exercise(n)
NameError: name 'self' is not defined
def calc_div_exercise(n = 1):
    global n = 1
    global g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
        self.calc_div_exercise(n)
        
SyntaxError: invalid syntax
def calc_div_exercise(n = 1):
    global n = 1
    global g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
        calc_div_exercise(n)
        
SyntaxError: invalid syntax
def calc_div_exercise(n = 1):
    global n = 1
    global g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(global g)
    elif a != 0:
        n += 1
        global g =+ global n
        main.calc_div_exercise(global n)
        
SyntaxError: invalid syntax
def calc_div_exercise(n):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
        calc_div_exercise(n)

        

calc_div_exercise
<function calc_div_exercise at 0x000000703C18FD90>
calc_div_exercise(1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    calc_div_exercise(1)
  File "<pyshell#122>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#122>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#122>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#122>", line 5, in calc_div_exercise
    if a == 0:
RecursionError: maximum recursion depth exceeded in comparison
    def calc_div_exercise(n):
        n = 1
        g = 10 ** 100
        a = (g + n) % 13
        if a == 0:
            print(g)
        elif a != 0:
            n += 1
            g =+ n
            calc_div_exercise(n)
            
SyntaxError: unexpected indent
def calc_div_exercise(n):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
    :calc_div_exercise(n)
    
SyntaxError: invalid syntax
def calc_div_exercise(n):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
calc_div_exercise(n)
SyntaxError: invalid syntax
calc_div_exercise(n)def calc_div_exercise(n):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
    calc_div_exercise(n)
    
SyntaxError: invalid syntax
def calc_div_exercise(n):
    n = 1
    g = 10 ** 100
    a = (g + n) % 13
    if a == 0:
        print(g)
    elif a != 0:
        n += 1
        g =+ n
    calc_div_exercise(n)

    
calc_div_exercise(1)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    calc_div_exercise(1)
  File "<pyshell#131>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#131>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  File "<pyshell#131>", line 10, in calc_div_exercise
    calc_div_exercise(n)
  [Previous line repeated 1021 more times]
  File "<pyshell#131>", line 5, in calc_div_exercise
    if a == 0:
RecursionError: maximum recursion depth exceeded in comparison
n = 15 / 2
nn = 15 // 2
print(n,nn)
7.5 7
print(n,nn,end='\t')
7.5 7	
print(n,nn,end='\n')
7.5 7

============ RESTART: C:/Users/rocketman5290/Desktop/helloworld.py ===========

============ RESTART: C:/Users/rocketman5290/Desktop/helloworld.py ===========
127.0

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1 2 3

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
(-0.9999999999999999+1.4142135623730951j)

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
(-0.9999999999999999+1.4142135623730951j)

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
(-0.9999999999999999+1.4142135623730951j)

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895
True

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895
True
False

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895
True
True

= RESTART: C:/Users/rocketman5290/Desktop/helloworld.py
50.0 inches equal 127.0 centimeters.
1.0 inches equal 2.54 centimeters.
2.0 inches equal 5.08 centimeters.
3.0 inches equal 7.62 centimeters.
1.618033988749895
True
1.618033988749895
True

= RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py
Hello, Please enter your first name in                     the prompt:william
Users first name: william

= RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py
Hello, Please enter your first name in the prompt:william
Users first name: william

= RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py
Hello, Please enter your first name in the prompt:william
Users first name: william
Traceback (most recent call last):
  File "C:/Users/rocketman5290/Desktop/taking_user_input.py", line 3, in <module>
    input_str2 = input(prompt='please enter your last name followed by enter:')
TypeError: input() takes no keyword arguments

=== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py ===
Hello, Please enter your first name in the prompt:william
Users first name: william
please enter your last name followed by enter:george
george

=== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py ===
Hello, Please enter your first name in the prompt:Will
Users first name: Will
please enter your last name followed by enter:George
Users last name: George

=== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py ===
Hello, Please enter your first name in the prompt:william
Users first name: william
please enter your last name followed by enter:george
Users last name: george
Thankyou and hello william george , welcome to your first cli app written in python.

=== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py ===
Hello, Please enter your first name in the prompt:william
Users first name: william
please enter your last name followed by enter:george
Users last name: george
Thankyou and hello william george, welcome to your first cli app written in python.

========================== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py =========================
Hello, Please enter your first name in the prompt:William
Users first name: William
please enter your last name followed by enter:George
Users last name: George


========================== RESTART: C:/Users/rocketman5290/Desktop/taking_user_input.py =========================
Hello, Please enter your first name in the prompt:William
Users first name: William
please enter your last name followed by enter:George
Users last name: George
Thank you and hello William George, welcome to your first cli app written in python.

======================== RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py =======================
true
false

======================== RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py =======================
true
false
false

====== RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py =====
true
false
false
1 2 3 4 5 6 7 8 9 10 

====== RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py =====
true
false
false
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 Traceback (most recent call last):
  File "C:/Users/rocketman5290/Desktop/decisions_and_looping.py", line 23, in <module>
    while_loop(20)
  File "C:/Users/rocketman5290/Desktop/decisions_and_looping.py", line 20, in while_loop
    print(n, end=' ')
KeyboardInterrupt
>>> 
====== RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py =====
true
false
false
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
>>> 
= RESTART: C:/Users/rocketman5290/Desktop/decisions_and_looping.py
true
false
false
True
neither true nor flase
True
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
