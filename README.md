### Prerequisites

To use this sample:

- Install [Python 3.6](https://www.python.org/downloads/)
- Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) version 2.x or later.
- Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) version 2.2.70 or later (requires .NET Core 2.x SDK).

### Download the sample

In a terminal window, run the following commands to clone the sample application to your local machine, and navigate to the directory with the sample code.

```bash
git clone https://github.com/asavaritayal/dog-classification.git
cd dog-classification
```

### Create and activate a virtual environment

To work with an Python Azure Function project, it is required that you work in a Python 3.6 virtual environment. Run the following commands to create and activate a virtual environment named .env.

```bash
# In Bash
python3.6 -m venv .env
source .env/bin/activate

# In PowerShell
py -3.6 -m venv .env
.env\scripts\activate
```

### Install dependencies

The names and versions of the required packages are already listed in the `requirements.txt` file. Use the following command to install these dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Test

Use the following command to run the Functions host locally.

```bash
func host start
```

Trigger the function from the command line using curl in a new terminal window:

```bash
curl -w '\n' http://localhost:7071/api/classify?img=<image_url>
```

### Publish to Azure

Using the Azure Functions Core Tools, run the following command. Replace <APP_NAME> with the name of your Linux Function App.

```bash
func azure functionapp publish <APP_NAME> --build-native-deps
```