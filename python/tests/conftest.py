import os
import sys

# Ensure the parent `python` directory is on sys.path so tests can import
# modules like `texttest_fixture` when running from the repository root.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

# Configure a default reporter for approvaltests so `verify()` won't raise
try:
	import approvaltests.reporters as _reporters
	_reporters.set_default_reporter(_reporters.PythonNativeReporter())
except Exception:
	# If approvaltests isn't available yet, tests that depend on it will fail later.
	pass
