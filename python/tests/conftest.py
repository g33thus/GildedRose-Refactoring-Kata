import os
import sys

# Put python/src on sys.path so tests can `from gilded_rose import ...`,
# and tests/approval so `from texttest_fixture import ...` still works.
HERE = os.path.abspath(os.path.dirname(__file__))
PYTHON_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(PYTHON_ROOT, "src")
APPROVAL = os.path.join(HERE, "approval")
for p in (SRC, PYTHON_ROOT, HERE, APPROVAL):
    if p not in sys.path:
        sys.path.insert(0, p)

# Configure a default reporter for approvaltests so `verify()` won't raise
try:
    import approvaltests.reporters as _reporters
    _reporters.set_default_reporter(_reporters.PythonNativeReporter())
except Exception:
    pass
