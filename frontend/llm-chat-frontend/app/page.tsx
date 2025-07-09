'use client';

import React, { useState } from 'react';
import ChatWindow from '../components/ChatWindow';
import MessageInput from '../components/MessageInput';
import { useTheme } from '../context/ThemeContext';

interface Message {
  text: string;
  isUser: boolean;
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    { text: "Hello! How can I help you today?", isUser: false },
  ]);
  const { theme, toggleTheme } = useTheme();
  const [useGemini, setUseGemini] = useState(true); // true for Gemini, false for MCP

  const handleSendMessage = async (text: string) => {
    const newUserMessage: Message = { text, isUser: true };
    setMessages((prevMessages) => [...prevMessages, newUserMessage]);

    const apiEndpoint = useGemini ? '/api/gemini' : '/api/mcp';

    try {
      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: text }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const newLLMMessage: Message = { text: data.text, isUser: false };
      setMessages((prevMessages) => [...prevMessages, newLLMMessage]);
    } catch (error) {
      console.error(`Error sending message to ${useGemini ? 'Gemini' : 'MCP'} API:`, error);
      const errorMessage: Message = { text: `Error: Could not get a response from ${useGemini ? 'Gemini' : 'MCP'}.`, isUser: false };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div className="d-flex flex-column h-full" style={{ backgroundColor: 'var(--color-background)', color: 'var(--color-text)' }}>
      <div className="d-flex justify-content-between align-items-center py-3 px-4" style={{ backgroundColor: 'var(--color-primary)', color: 'var(--color-text)' }}>
        <h1 className="text-center m-0">LLM Chat Frontend</h1>
        <div>
          <button onClick={toggleTheme} className="btn btn-secondary me-2">
            Switch to {theme === 'light' ? 'Dark' : 'Light'} Mode
          </button>
          <button onClick={() => setUseGemini(!useGemini)} className="btn btn-info">
            Switch to {useGemini ? 'MCP' : 'Gemini'} Backend
          </button>
        </div>
      </div>
      <ChatWindow messages={messages} />
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
}