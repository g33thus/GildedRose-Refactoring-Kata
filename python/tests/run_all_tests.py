import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(ROOT, "src")
for p in (SRC, ROOT, HERE):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    import approvaltests.reporters as _reporters
    _reporters.set_default_reporter(_reporters.PythonNativeReporter())
except Exception:
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().discover(start_dir=HERE, pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
