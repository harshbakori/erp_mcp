run using 

'uv run main.py'

test using 

'npx @modelcontextprotocol/inspector'


new way

to connect to openweb-ui you can use folowing command when mcp server is running


```code
uvx mcpo --port 8002 --server-type "streamable_http" -- http://127.0.0.1:8000/mcp
```

step 1 start mcp server

step 2 start proxy using this

step3 connect openweb-ui with running mcp server.

make sure to add it using admi npanel settings in tools 