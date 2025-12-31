from fastmcp import FastMCP

app = FastMCP("this is demo mcp server")

@app.tool()
def add_two_number(n1: int, n2: int) -> int:
    """Add Two Numbers"""
    return n1 + n2
