"""
Example of a (slighly pointless) test.
    It will be run every time you push thanks to .github/workflows/test_workflow.yml
If a test fails you will get an AssertionError and output would be something like:

======================================= test session starts =======================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /home/iva/projects/gemeente/InternshipAmsterdam/InternshipAmsterdamGeneral
collected 2 items

tests/example_tests.py .F                                                                   [100%]

============================================ FAILURES =============================================
_______________________________________ test_that_will_fail _______________________________________

    def test_that_will_fail():
>       assert 0 == 1
E       assert 0 == 1

tests/example_tests.py:57: AssertionError
===================================== short test summary info =====================================
FAILED tests/example_tests.py::test_that_will_fail - assert 0 == 1
=================================== 1 failed, 1 passed in 0.11s ===================================
"""

import numpy as np


def test_that_will_pass():
    """
    Describe what's the purpose of this test.
    This test shows that np.nan_to_num (unsurprisingly) works as expected,
    however, you can (and should) import stuffs from your own modules to test here.

    """

    input_data = np.array(
        [[0.75, np.nan, np.nan],
         [np.nan, 0, 0.0],
         [np.nan, np.nan, 0.99],
         [np.nan, np.nan, 0.42],
        ]
    )

    expected_output = np.array(
        [[0.75, 0, 0],
         [0, 0, 0],
         [0, 0, 0.99],
         [0, 0, 0.42],
        ]
    )

    calculated_output = np.nan_to_num(input_data)

    assert np.array_equal(expected_output, calculated_output)
