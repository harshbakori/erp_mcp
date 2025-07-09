import React from 'react';
import Message from './Message';

interface ChatWindowProps {
  messages: { text: string; isUser: boolean }[];
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
  return (
    <div className="flex-grow-1 overflow-auto p-3" style={{ height: 'calc(100vh - 120px)', backgroundColor: 'var(--color-background)' }}>
      {messages.map((message, index) => (
        <Message key={index} text={message.text} isUser={message.isUser} />
      ))}
    </div>
  );
};

export default ChatWindow;
