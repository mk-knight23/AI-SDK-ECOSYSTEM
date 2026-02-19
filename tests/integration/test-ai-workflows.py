# Integration tests for AI workflows
import pytest
import requests

BASE_URLS = {
    "venture-graph": "http://localhost:8000",
    "omni-desk": "http://localhost:8001",
    "dev-squad": "http://localhost:5173",
    "supply-consensus": "http://localhost:8003",
    "market-pulse": "http://localhost:8080",
    "insight-stream": "http://localhost:3000",
    "research-synthesis": "http://localhost:8006",
    "trend-factory": "http://localhost:8007",
    "patent-iq": "http://localhost:5009",
    "claude-forge": "http://localhost:8010"
}


class TestHealthEndpoints:
    """Test all health endpoints"""

    def test_venture_graph_health(self):
        response = requests.get(f"{BASE_URLS['venture-graph']}/health", timeout=5)
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_omni_desk_health(self):
        response = requests.get(f"{BASE_URLS['omni-desk']}/health", timeout=5)
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


class TestAIWorkflows:
    """Test AI workflow integrations"""

    @pytest.mark.integration
    def test_venture_graph_plan(self):
        """Test venture planning workflow end-to-end"""
        response = requests.post(
            f"{BASE_URLS['venture-graph']}/plan",
            json={"idea": "AI productivity tool"},
            timeout=30
        )
        assert response.status_code == 200
        data = response.json()
        assert "market_analysis" in data
        assert "business_model" in data
        assert "pitch_deck" in data

    @pytest.mark.integration
    def test_omni_desk_rag(self):
        """Test RAG document query workflow"""
        # Add documents
        requests.post(
            f"{BASE_URLS['omni-desk']}/documents",
            json={"documents": ["Company founded in 2020", "HQ in San Francisco"]},
            timeout=10
        )

        # Query
        response = requests.post(
            f"{BASE_URLS['omni-desk']}/query",
            json={"question": "When was the company founded?"},
            timeout=10
        )
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert "sources" in data
