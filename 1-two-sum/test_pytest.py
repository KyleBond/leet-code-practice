import pytest
import solution
import numpy as np

class TestClass:
    def test_two_ints(self):
        # Arrange
        sourceNumber = [1,3]
        target = 4
        expectedResult = [0,1]
        # Act
        result = solution.twoSum(self,nums=sourceNumber, target=target)
        # Assert
        assert result == expectedResult

    def test_five_ints(self):
        # Arrange
        sourceNumber = [1,3,5]
        target = 8
        expectedResult = [1,2]
        # Act
        result = solution.twoSum(self,nums=sourceNumber, target=target)
        # Assert
        assert result == expectedResult

    def test_random_100_ints(self):
    # Arrange
        sourceNumber = np.random.randint(1, 100000000, 100).tolist()
        target = sourceNumber[17] + sourceNumber[99]
        expectedResult = [17,99]
        # Act
        result = solution.twoSum(self,nums=sourceNumber, target=target)
        # Assert
        assert result == expectedResult

    def test_same_ints(self):
    # Arrange
        sourceNumber = [2,2,3]
        target = 4
        expectedResult = [0,1]
        # Act
        result = solution.twoSum(self,nums=sourceNumber, target=target)
        # Assert
        assert result == expectedResult

    def test_example_2(self):
    # Arrange
        sourceNumber = [3,2,4]
        target = 6
        expectedResult = [1,2]
        # Act
        result = solution.twoSum(self,nums=sourceNumber, target=target)
        # Assert
        assert result == expectedResult
        