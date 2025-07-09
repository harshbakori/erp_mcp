import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const { message } = await request.json();

    if (!message) {
      return NextResponse.json({ error: 'Message is required' }, { status: 400 });
    }

    // Simulate a response from the MCP server
    const dummyResponse = `MCP received: "${message}". This is a dummy response from your MCP server.`;

    return NextResponse.json({ text: dummyResponse });
  } catch (error) {
    console.error('Error in dummy MCP API:', error);
    return NextResponse.json({ error: 'Failed to get response from dummy MCP' }, { status: 500 });
  }
}
