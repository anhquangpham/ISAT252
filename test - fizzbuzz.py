# test 


from fizzbuzz import fizzbuzz

fb = fizzbuzz()

# # smoke test 
def test_smoke();
	assert True == True

	def test_fizz();
		assert fb.fizz(3) == "fizz"
		assert fb.fizz(33) == "fizz"
		assert fb.fizz(30303033)== "fizz"
		assert fb.fizz(1) == 1
		assert fb.fizz(5) == 5
		assert fb.fizz(37) == 37 


	def test_buzz();
		assert fb.fizz(5) == "buzz"
		assert fb.fizz(55) == "buzz"
		assert fb.fizz(55055095) == "buzz"
		assert fb.fizz(1) == 1
		assert fb.fizz(3) == 3
		assert fb.fizz(37) == 7
