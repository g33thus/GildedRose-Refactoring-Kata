# Tests

Two kinds of tests guard this kata.

## Unit / behaviour tests

Each file checks one item type's rules in isolation:

- `test_normal_item.py` rules and `test_cross_cutting.py` rules now live in `test_generic.py`
- `test_aged_brie.py` — quality rises, doubles past sell date
- `test_backstage_passes.py` — +1 / +2 / +3 tiers, drops to 0 after the concert
- `test_conjured.py` — degrades twice as fast
- `test_sulfuras.py` — legendary, never changes
- `test_generic.py` — normal items, plus cross-cutting checks (empty list, mixed items in one call, two-day runs)

Unit tests assert a single rule. Cross-cutting tests in `test_generic.py` assert the loop wiring: updating one item must not affect another, and state must carry between days.

## Approval / golden-master test

Lives in `tests/approval/`.

- `texttest_fixture.py` runs the shop for 30 days and prints every item each day
- `test_gilded_rose_approvals.py` captures that output and diffs it against the saved snapshot
- `approved_files/` holds the snapshot; a mismatch writes a `.received.txt` beside it
- `approvaltests_config.json` points the snapshot lookup at `approved_files/`

The approval test does not encode rules. It freezes whatever the code prints today, then fails on any future change to that output. Use it to catch unintended changes across all item types at once.

## Running

Run from the `python/` directory.

```bash
python -m pytest                                  # both kinds
python -m pytest tests --ignore=tests/approval    # unit only
python -m pytest tests/approval                   # approval only
```

The full run writes a combined HTML report to `reports/test_report.html` (configured in `pytest.ini`) containing every test from both kinds.

## Approving a deliberate output change

When you change behaviour on purpose, the approval test fails because the new output no longer matches the snapshot. To accept the new output as the baseline:

```bash
# from python/tests/approval/approved_files/
copy /Y test_gilded_rose_approvals.test_gilded_rose_approvals.received.txt ^
       test_gilded_rose_approvals.test_gilded_rose_approvals.approved.txt
```

Review the diff between `.received.txt` and `.approved.txt` before approving. Approve only when the change is intended.

## Layout

```
python/
  src/                  production code
  tests/
    test_*.py           unit / behaviour tests
    support.py          test helpers (make, tick)
    conftest.py         sys.path + reporter setup
    README.md           this file
    approval/
      texttest_fixture.py
      test_gilded_rose_approvals.py
      approvaltests_config.json
      approved_files/
```
