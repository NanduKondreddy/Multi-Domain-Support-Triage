import os
import glob

print("=" * 80)
print("SUBMISSION PACKAGING VERIFICATION")
print("=" * 80)

print("\nTO INCLUDE IN ZIP:")
print("-" * 80)

code_files = glob.glob("code/**/*.py", recursive=True)
code_files.sort()
for f in code_files:
    print(f"  {f}")

prompts = glob.glob("code/prompts/*.txt", recursive=True)
if prompts:
    print("\nPrompt files:")
    for f in sorted(prompts):
        print(f"  {f}")

print("\n" + "-" * 80)
print("TO EXCLUDE:")
print("-" * 80)
exclude_patterns = [
    "data/",
    "support_tickets/",
    "__pycache__/",
    "*.pyc",
    "venv/",
    ".env",
    ".git/",
    ".pytest_cache/",
    "final_results.csv",
    "audit_test_cases.csv",
    "audit_results.csv",
    "*.ipynb",
]

for pattern in exclude_patterns:
    print(f"  {pattern}")

print("\n" + "=" * 80)
print("READY FILES:")
print("=" * 80)

print(f"\nfinal_results.csv exists: {os.path.exists('final_results.csv')}")
print(f"code/ folder exists: {os.path.exists('code')}")
print(f"code/main.py exists: {os.path.exists('code/main.py')}")
print(f"code/README.md exists: {os.path.exists('code/README.md')}")

print("\n" + "=" * 80)
print("SUBMISSION CHECKLIST:")
print("=" * 80)
print("[ ] final_results.csv in root")
print("[ ] code/*.py files (all production files)")
print("[ ] code/prompts/*.txt (prompt templates)")
print("[ ] .gitignore (includes .env)")
print("[ ] NO data/ folder")
print("[ ] NO support_tickets/ folder")
print("[ ] NO __pycache__/")
print("[ ] NO .env file")
