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
* `O(1)` - because we are returning a single line with 0 instantiation, and splicing, concatinating with a list comprehension...
  * without assigning any values or increasing the amount of values, the space complexity is constant O(1)


5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
