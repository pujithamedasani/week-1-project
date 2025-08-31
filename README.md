# Week-1-project
# EduNet Green Skills & AI - Renewable Energy Project

This project is part of the EduNet Green Skills & AI initiative.  
It uses renewable energy datasets from Kaggle to analyze, clean, and generate insights about global renewable energy adoption.

## 📂 Repository Structure
```
edunet-green-skills-ai/
│ renewable_energy_clean.csv   # cleaned dataset (sample included)
│ renewable_energy_ai.ipynb    # Jupyter notebook
│ renewable_energy_ai.py       # Python script version
│── README.md
```

## 🚀 How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/edunet-green-skills-ai.git
   cd edunet-green-skills-ai
   ```

2. Set up Kaggle API:
   - Create a Kaggle account and download `kaggle.json` from [Kaggle Account Settings](https://www.kaggle.com/account).
   - Place it in:  
     - Linux/Mac: `~/.kaggle/kaggle.json`  
     - Windows: `C:\Users\<username>\.kaggle\kaggle.json`

3. Download dataset:
   ```bash
   kaggle datasets download -d sudalairajkumar/renewable-energy -p ./data --unzip
   ```

4. Run the notebook or script:
   ```bash
   jupyter notebook notebooks/renewable_energy_ai.ipynb
   # or
   python renewable_energy_ai.py
   ```

5. The cleaned dataset will be saved to:
   ```
   data/renewable_energy_clean.csv
   ```

## Features
- Loads renewable energy dataset from Kaggle
- Cleans and processes missing values & units
- Calculates renewable share of total energy
- Estimates yearly growth trends
- Saves cleaned dataset for analysis

##  Requirements
- Python 3.8+
- pandas, numpy, matplotlib, seaborn, scikit-learn

Install with:
```bash
pip install -r requirements.txt
```

## Credits
- Dataset: [Kaggle - Renewable Energy](https://www.kaggle.com/datasets/sudalairajkumar/renewable-energy)
- Developed as part of EduNet Green Skills & AI project

