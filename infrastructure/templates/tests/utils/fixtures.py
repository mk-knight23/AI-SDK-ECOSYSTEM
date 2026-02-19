# Test fixtures for Python projects
import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI API response"""
    return {
        "choices": [{"message": {"content": "Test response"}}],
        "usage": {"total_tokens": 50}
    }


@pytest.fixture
def sample_venture_idea():
    """Sample venture idea for testing"""
    return {
        "idea": "AI-powered sustainable farming platform",
        "market": "Agriculture technology",
        "target_customers": "Small to medium farms"
    }


@pytest.fixture
def mock_chroma_db():
    """Mock ChromaDB for RAG testing"""
    mock_db = MagicMock()
    mock_db.similarity_search.return_value = [
        MagicMock(page_content="Test document 1", metadata={"source": "test1"}),
        MagicMock(page_content="Test document 2", metadata={"source": "test2"})
    ]
    return mock_db


@pytest.fixture
def sample_documents():
    """Sample documents for RAG testing"""
    return [
        "Company founded in 2020. We specialize in AI solutions.",
        "Our headquarters is in San Francisco with 50 employees.",
        "We serve enterprise customers globally."
    ]
