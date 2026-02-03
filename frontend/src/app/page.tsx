'use client';

import { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';

type Message = {
  role: 'user' | 'assistant';
  content: string;
};

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: "Bonjour ! Je suis l'assistant d'**Ian'ch**. Posez-moi des questions sur :\n- Son parcours professionnel\n- Ses compétences techniques\n- Ses projets en cours\n\n🚀 C'est parti !"
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [streamingText, setStreamingText] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, streamingText]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);
    setStreamingText('');

    try {
      // const response = await fetch('https://TON-URL-RAILWAY.railway.app/chat', {
      const response = await fetch('https://portefolio-demo-production.up.railway.app/chat', {
      // const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, userMessage]
        })
      });

      const data = await response.json();
      
      // Effet de frappe progressive
      const fullText = data.response;
      let currentIndex = 0;
      
      const typingInterval = setInterval(() => {
        if (currentIndex < fullText.length) {
          // Ajouter 2-5 caractères à la fois pour effet plus naturel
          const chunkSize = Math.floor(Math.random() * 4) + 2;
          setStreamingText(fullText.slice(0, currentIndex + chunkSize));
          currentIndex += chunkSize;
        } else {
          clearInterval(typingInterval);
          setMessages(prev => [...prev, {
            role: 'assistant',
            content: fullText
          }]);
          setStreamingText('');
          setLoading(false);
        }
      }, 30); // 30ms entre chaque ajout = effet fluide

    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: "❌ Désolé, une erreur s'est produite. Réessayez !"
      }]);
      setLoading(false);
      setStreamingText('');
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <header className="bg-black/30 backdrop-blur-sm border-b border-white/10 p-4">
        <h1 className="text-2xl font-bold text-white">Ian'ch Portfolio Chat</h1>
        {/* <p className="text-gray-400 text-sm">Powered by Gemini 2.5 Flash ⚡</p> */}
      </header>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                msg.role === 'user'
                  ? 'bg-purple-600 text-white'
                  : 'bg-white/10 backdrop-blur-sm text-gray-100 border border-white/20'
              }`}
            >
              {msg.role === 'assistant' ? (
                <ReactMarkdown
                  components={{
                    // Style des éléments markdown
                    p: ({node, ...props}) => <p className="mb-2 last:mb-0" {...props} />,
                    strong: ({node, ...props}) => <strong className="font-bold text-purple-300" {...props} />,
                    ul: ({node, ...props}) => <ul className="list-disc list-inside space-y-1 my-2" {...props} />,
                    ol: ({node, ...props}) => <ol className="list-decimal list-inside space-y-1 my-2" {...props} />,
                    li: ({node, ...props}) => <li className="ml-2" {...props} />,
                    code: ({node, ...props}) => <code className="bg-purple-900/50 px-1 rounded text-purple-200" {...props} />,
                  }}
                >
                  {msg.content}
                </ReactMarkdown>
              ) : (
                <p className="whitespace-pre-wrap">{msg.content}</p>
              )}
            </div>
          </div>
        ))}
        
        {/* Message en cours de frappe */}
        {streamingText && (
          <div className="flex justify-start">
            <div className="max-w-[80%] bg-white/10 backdrop-blur-sm border border-white/20 rounded-2xl px-4 py-3">
              <ReactMarkdown
                components={{
                  p: ({node, ...props}) => <p className="mb-2 last:mb-0" {...props} />,
                  strong: ({node, ...props}) => <strong className="font-bold text-purple-300" {...props} />,
                  ul: ({node, ...props}) => <ul className="list-disc list-inside space-y-1 my-2" {...props} />,
                  ol: ({node, ...props}) => <ol className="list-decimal list-inside space-y-1 my-2" {...props} />,
                  li: ({node, ...props}) => <li className="ml-2" {...props} />,
                  code: ({node, ...props}) => <code className="bg-purple-900/50 px-1 rounded text-purple-200" {...props} />,
                }}
              >
                {streamingText}
              </ReactMarkdown>
              <span className="inline-block w-2 h-4 bg-purple-400 animate-pulse ml-1"></span>
            </div>
          </div>
        )}
        
        {loading && !streamingText && (
          <div className="flex justify-start">
            <div className="bg-white/10 backdrop-blur-sm border border-white/20 rounded-2xl px-4 py-3">
              <div className="flex space-x-2">
                <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSubmit} className="p-4 bg-black/30 backdrop-blur-sm border-t border-white/10">
        <div className="flex gap-2 max-w-4xl mx-auto">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Posez votre question..."
            className="flex-1 rounded-full px-6 py-3 bg-white/10 backdrop-blur-sm border border-white/20 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
            disabled={loading}
          />
          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="rounded-full px-8 py-3 bg-purple-600 hover:bg-purple-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-medium transition-colors"
          >
            Envoyer
          </button>
        </div>
      </form>
    </div>
  );
}