import unittest
import os
from file_searcher import search_files

class TestFileSearcher(unittest.TestCase):

    def setUp(self):
        """
        Set up a temporary directory and files for testing.
        This method is called before each individual test.
        """
        # Create a temporary directory for testing
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create test files
        with open(os.path.join(self.test_dir, "testfile1.txt"), 'w') as f:
            f.write("This is test file 1.")
        with open(os.path.join(self.test_dir, "testfile2.txt"), 'w') as f:
            f.write("This is test file 2.")
        with open(os.path.join(self.test_dir, "TESTFILE1.TXT"), 'w') as f:
            f.write("This is another version of test file 1.")

    def tearDown(self):
        """
        Clean up the temporary directory and its contents after each test.
        This method is called after each individual test.
        """
        # Remove the directory and its contents
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_multiple_files_found_case_sensitive(self):
        """
        Test case to check if multiple files are found with case sensitivity.
        """
        results = search_files(self.test_dir, ["testfile1.txt", "testfile2.txt"], True)
        self.assertEqual(len(results["testfile1.txt"]), 1)
        self.assertEqual(len(results["testfile2.txt"]), 1)

    def test_multiple_files_found_case_insensitive(self):
        """
        Test case to check if multiple files are found with case insensitivity.
        """
        results = search_files(self.test_dir, ["testfile1.txt", "TESTFILE1.TXT"], False)
        self.assertEqual(len(results["testfile1.txt"]), 1)
        self.assertEqual(len(results["TESTFILE1.TXT"]), 1)

    def test_file_not_found(self):
        """
        Test case to check that a non-existing file returns no results.
        """
        results = search_files(self.test_dir, ["nonexistent.txt"], True)
        self.assertEqual(len(results["nonexistent.txt"]), 0)

    def test_case_sensitive_not_found(self):
        """
        Test case to check that a case-sensitive search returns no results if the case doesn't match.
        """
        results = search_files(self.test_dir, ["TESTFILE1.TXT"], True)
        self.assertEqual(len(results["TESTFILE1.TXT"]), 0)

    def test_count_occurrences(self):
        """
        Test case to check the count of occurrences for a specific file.
        """
        results = search_files(self.test_dir, ["testfile1.txt", "TESTFILE1.TXT"], False)
        self.assertEqual(len(results["testfile1.txt"]), 1)  # Should find it once
        self.assertEqual(len(results["TESTFILE1.TXT"]), 1)  # Should find it once

if __name__ == "__main__":
    unittest.main()
