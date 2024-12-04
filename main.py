import asyncio
import websockets
import json


async def binance_order_book():
    ws_url = "wss://stream.binance.com:9443/ws/btcusdt@depth"

    async with websockets.connect(ws_url) as websocket:
        print("Connected to Binance WebSocket for Order Book")

        while True:
            message = await websocket.recv()
            data = json.loads(message)

            highest_bid = data["b"][0]
            lowest_ask = data["a"][0]

            bid_price, bid_quantity = highest_bid
            ask_price, ask_quantity = lowest_ask

            print(f"Highest Bid: {bid_price} (Quantity: {bid_quantity})")
            print(f"Lowest Ask: {ask_price} (Quantity: {ask_quantity})")
            print("-" * 30)

if __name__ == "__main__":
    asyncio.run(binance_order_book())
