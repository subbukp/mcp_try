from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Flight Booking Server")

def get_airports():
    """Get list of available airports"""
    return {
        "LAX": {"name": "Los Angeles International", "city": "Los Angeles"},
        "JFK": {"name": "John F. Kennedy International", "city": "New York"},
        "LHR": {"name": "London Heathrow", "city": "London"}
    }

if __name__ == "__main__":
    mcp.run() 