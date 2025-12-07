import asyncio
from core import SynapseExecutionModule

# Mock payload data
test_payload = {
    "id": "SYN-X99",
    "media": "video_file.mp4",
    "captions": "AI generated content",
    "metadata": {"privacy": "public"},
    "target": "tech_enthusiasts"
}

async def main():
    system = SynapseExecutionModule(strategy_id="STRAT-001")
    await system.execute_autonomous_cycle(test_payload)

if __name__ == "__main__":
    asyncio.run(main())
