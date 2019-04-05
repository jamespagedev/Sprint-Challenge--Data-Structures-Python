Add your answers to the questions below.

* `RingBuffer` Object: I would like to add that since it wasn't asked where the ring_buffer uses space complexity in the questions...
  * `capacity` type is int -> O(1)
  * `current` type is int -> O(1)
  * `storage` type is list -> O(n)
  * No space complexity is instantiated during the append/get...
  * We can conclude the worst case of space complexity for the RingerBuffer object is `O(n)`

1. What is the runtime complexity of your ring buffer's `append` method?
* `O(1)` - there are no iterations done, the element is already stored in the object.
  * Depending on the location of current and the data type of the element in the list...
  * a list in python to replace an element where you already know you want to replace it will have O(1)

2. What is the space complexity of your ring buffer's `append` function?
* `O(1)` - because this question refers to the method and not the entire class (where the values are stored)...
  * the method only makes comparisons and stores no extra values in memory when changing the values already stored,
  * therefore, the it is constant O(1)

3. What is the runtime complexity of your ring buffer's `get` method?
* `O(n)` - according to python time complexity wiki, splicing part of an array in python is O(k)
  * Since we are splicing both sides of the array and concatinating them in reverse, this makes it O(n)
  * When we concatinate both sides of the spliced arrays (without `None`'s if exist), the operation is O(n) not nested
  * this makes the runtime O(2n) which is the same as O(n)

4. What is the space complexity of your ring buffer's `get` method?
* `O(n)` - because we are copying array using a list comprehension (space of n) before returning it

5. What is the runtime complexity of the provided code in `names.py`?
* `O(n^2)` - the second for loop is nested forcing the iterations to be 10,000 * 10,000 when comparing values

6. What is the space complexity of the provided code in `names.py`?
* 2 files -> O(2n)
* 2 lists to hold file lines -> O(2n)
* 1 list to hold duplicates -> O(n)
* total = O(5n) -> `O(n)`

7. What is the runtime complexity of your optimized code in `names.py`?
* First Optomized Solution
  * each file open is a single O(n) -> O(2n)
  * 1 list to hold the name values from file2.read().readlines() -> O(n)
  * loop through file1 n times -> O(n)
    * conditionally loop through list holding file2 names, exit loop early if condition met -> O(log n)
  * Because the conditional loop is nested in the n loop...
  * Total = O(n) * O(log n) -> `O(n log n)`
* MVP
  * each file open is a single O(n) -> O(2n)
  * Create a dictionary by iterating through both files (at the same time) -> O(2n)
  * Iterating through the values in the dictionary to check for duplicates(in the key) before adding the duplicates to the list -> O(n)
  * Checking if a key exists in a dictionary -> O(1)
  * Appending the found duplicate to the duplicate list -> O(1)
  * Total = O(5n) -> `O(n)`
* Stretch
  * each file open is a single O(n) -> O(2n)
  * by using file.read().readlines() on both files (2n)...
  * while parsing through the lines removing `\n` during the `set` module sub-method to compare values for instantion of duplciates -> O(n)
  * Total = O(5n) -> `O(n)`

8. What is the space complexity of your optimized code in `names.py`?
* First Optomized Solution
  * each file open is a single O(n) -> O(2n)
  * 1 list to hold the name values to compare against -> O(n)
  * 1 list to hold duplicate values -> O(n)
  * Total = O(4n) -> `O(n)`
* MVP
  * 2 files -> O(2n)
  * 1 dictionary to hold lines as key/value pair -> O(2n)
  * 1 list to hold duplicates -> O(n)
  * Total = O(5n) -> `O(n)`
* Stretch
  * 2 files -> O(2n)
  * 1 set to hold duplicates -> O(n)
  * Total = O(3n) -> `O(n)`