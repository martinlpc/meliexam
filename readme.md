# MercadoLibre Exam

## Mutant DNA detector

Python app to detect mutant DNA samples.

Instructions to run the API web server:

1 - Create a virtual environment and activate it:

    py -m venv .venv
    .venv/scritps/activate.ps1

2 - Install FastAPI:

    pip install "fastapi[standard]"

3 - Run the server:

    fastapi dev main.py

Now that te server is running, you can send POST requests to the endpoint:

    http://<YourIPAddress>:<port>/mutant

Include the DNA sequence into the body of the request to examinate with the following JSON format:

    {
        "dna":[
            "AAGTTA",
            "TTACTT",
            "CTAACC",
            "GATTGG",
            "AGTCAG",
            "TGACGC"
        ]
    }

If a mutant DNA sequence is detected, the server will respond a status code 200 (OK)

Otherwise, if the sequence does not contain mutant traces, it will respond a status code 403 (Forbidden)

If the format of the sequence is invalid, you will get a status code 422 (Unprocessable entity)
