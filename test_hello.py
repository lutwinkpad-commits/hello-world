import subprocess
import sys
import unittest
from pathlib import Path


class HelloWorldTests(unittest.TestCase):
    def test_script_prints_greeting(self):
        script = Path(__file__).with_name("hello.py")
        result = subprocess.run(
            [sys.executable, str(script)],
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.stdout, "Hello, world!\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()