#!/bin/bash
# Test all AI integrations

PROJECTS=(
    "01-venture-graph:8000:/health"
    "02-omni-desk:8001:/health"
    "03-dev-squad:5173:api/review"
    "04-supply-consensus:8003:/health"
    "05-market-pulse:8080:/health"
    "06-insight-stream:3000:/api/chat"
    "07-research-synthesis:8006:/health"
    "08-trend-factory:8007:/health"
    "09-patent-iq:5009:/health"
    "10-claude-forge:8010:/health"
)

echo "Testing AI integrations..."
echo "=========================="
echo ""

for proj in "${PROJECTS[@]}"; do
    IFS=':' read -r name port endpoint <<< "$proj"
    echo -n "Testing $name... "

    response=$(curl -s -o /dev/null -w "%{http_code}" \
        "http://localhost:$port/$endpoint" 2>/dev/null || echo "000")

    if [ "$response" = "200" ] || [ "$response" = "401" ] || [ "$response" = "405" ]; then
        echo "✓ responding (HTTP $response)"
    else
        echo "✗ not responding (HTTP $response)"
    fi
done

echo ""
echo "=========================="
echo "Test complete!"
