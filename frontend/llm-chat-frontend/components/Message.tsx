import React from 'react';

interface MessageProps {
  text: string;
  isUser: boolean;
}

const Message: React.FC<MessageProps> = ({ text, isUser }) => {
  return (
    <div className={`d-flex mb-2 ${isUser ? 'justify-content-end' : 'justify-content-start'}`}>
      <div className={`card ${isUser ? 'text-white' : ''}`} style={{ maxWidth: '75%', backgroundColor: isUser ? 'var(--color-primary)' : 'var(--color-card-bg)', color: isUser ? 'var(--color-text)' : 'var(--color-text)' }}>
        <div className="card-body p-2">
          {text}
        </div>
      </div>
    </div>
  );
};

export default Message;
