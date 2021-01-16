from pathlib import Path

print(Path(__file__).resolve(strict=True).parent.parent)
