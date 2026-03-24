import asyncio
import websockets
import json

async def test_connection():
    uri = "wss://InsuranceVoiceAgents-backend-2ewjgqzoja-uc.a.run.app/ws/test-user/test-session"
    try:
        async with websockets.connect(uri) as websocket:
            print("Connected!")
            # Send a simple config or just wait
            # In main.py, it expects a map with "setup" or "client_content" maybe?
            # Let's just wait for a bit to see if it closes
            try:
                msg = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                print(f"Received: {msg}")
            except asyncio.TimeoutError:
                print("No initial message received (expected if no input)")
            
            # Keep open for a bit
            await asyncio.sleep(2)
            print("Connection maintained for 2s")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())
