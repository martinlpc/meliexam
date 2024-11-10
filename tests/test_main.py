import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from main import app

client = TestClient(app)


def test_mutant_dna():
    # Positive Mutant DNA => Must return Status = 200

    response = client.post(
        "/mutant",
        json={
            "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        },
    )

    assert response.status_code == 200


def test_non_mutant_dna():
    # Negative Mutant DNA => Must return Status = 403
    response = client.post(
        "/mutant",
        json={
            "dna": ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
        },
    )
    assert response.status_code == 403
