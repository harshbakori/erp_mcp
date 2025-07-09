import React, { useState } from 'react';

interface MessageInputProps {
  onSendMessage: (message: string) => void;
}

const MessageInput: React.FC<MessageInputProps> = ({ onSendMessage }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="d-flex p-3 border-top" style={{ backgroundColor: 'var(--color-background)', borderColor: 'var(--color-secondary)' }}>
      <input
        type="text"
        className="form-control me-2" style={{ backgroundColor: 'var(--color-card-bg)', color: 'var(--color-text)', borderColor: 'var(--color-secondary)' }}
        placeholder="Type your message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button type="submit" className="btn" style={{ backgroundColor: 'var(--color-primary)', borderColor: 'var(--color-primary)', color: 'var(--color-text)' }}>
        Send
      </button>
    </form>
  );
};

export default MessageInput;
