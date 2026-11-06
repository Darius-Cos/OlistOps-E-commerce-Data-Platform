from pathlib import Path

import kagglehub

root=Path(__file__).absolute().parents[2]

data_dir=root / "data/raw/olist"

data_dir.mkdir(parents=True,exist_ok=True)

path=kagglehub.dataset_download(
    "olistbr/brazilian-ecommerce",
    output_dir=str(data_dir)
)

print("Dataset dowloanded to:", path)

for file in sorted(data_dir.glob("*.csv")):
    print(file.name)