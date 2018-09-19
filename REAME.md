# Requirements

- Python3.6.x
- Azure Functions Core Tools version 2.0.1.38 or later

# Create and activate a virtual environment

Run the following commands to create and activate a virtual environment named `env`.

```bash
# In Bash
python3.6 -m venv env
source env/bin/activate

# In PowerShell
py -3.6 -m venv env
env\scripts\activate
```

# Setup your app

```bash
git clone https://github.com/asavaritayal/predict-shark-demo.git
cd predict-shark-demo
pip install -r requirements.txt
func host start
```