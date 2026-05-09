import React from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, FileText, Book, Code, Shield, Terminal, Zap, Layers, Cpu } from 'lucide-react';
import './DocsView.css';

const DocsView = ({ onBack }) => {
  return (
    <div className="docs-view premium-theme">
      <aside className="docs-sidebar">
        <div className="docs-nav-group">
          <span className="docs-nav-label">Core Protocols</span>
          <div className="docs-nav-link active"><Layers size={14} /> Introduction</div>
          <div className="docs-nav-link"><Shield size={14} /> Zero Trust Handshake</div>
          <div className="docs-nav-link"><Zap size={14} /> PQC Implementation</div>
        </div>

        <div className="docs-nav-group">
          <span className="docs-nav-label">Developer Hub</span>
          <div className="docs-nav-link"><Code size={14} /> API Endpoints</div>
          <div className="docs-nav-link"><Terminal size={14} /> CLI Reference</div>
          <div className="docs-nav-link"><Cpu size={14} /> SDK Guide</div>
        </div>

        <div className="docs-nav-group" style={{ marginTop: 'auto' }}>
          <div className="docs-nav-link" onClick={onBack}>
            <ArrowLeft size={14} /> Back to Handshake
          </div>
        </div>
      </aside>

      <main className="docs-content">
        <motion.div 
          initial={{ opacity: 0, y: 20 }} 
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <header className="docs-header">
            <div className="docs-blueprint-bg"></div>
            <h1 style={{ color: 'var(--primary)', textShadow: '0 0 40px var(--primary-glow)' }}>Technical Docs</h1>
            <p style={{ fontSize: '18px', color: 'var(--text2)', maxWidth: '700px', lineHeight: 1.6 }}>
              Deep technical specifications for the XCIPHER autonomous defense grid. 
              Built for high-compliance engineering teams and quantum-resilient infrastructure.
            </p>
          </header>

          <div className="docs-grid">
            {[
              { 
                title: 'Quick Start', 
                icon: Zap, 
                desc: 'Initialize the XCIPHER kernel and deploy your first defense node in under 300 seconds.' 
              },
              { 
                title: 'Handshake Protocol', 
                icon: Shield, 
                desc: 'Detailed breakdown of the Kyber-1024 key encapsulation mechanism and agent identity verification.' 
              },
              { 
                title: 'API Integration', 
                icon: Code, 
                desc: 'Connect your AI agents natively via the XCIPHER GraphQL mesh and real-time telemetry hooks.' 
              },
              { 
                title: 'Global Mesh', 
                icon: Layers, 
                desc: 'How XCIPHER nodes communicate across high-latency satellite and edge network environments.' 
              }
            ].map((item, i) => (
              <div key={i} className="docs-card">
                <div className="docs-card-icon">
                  <item.icon size={24} />
                </div>
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
                <div style={{ marginTop: '1.5rem', display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--accent)', fontSize: '12px', fontFamily: 'var(--mono)', cursor: 'pointer' }}>
                  READ SPECIFICATION <Zap size={10} />
                </div>
              </div>
            ))}
          </div>

          <div style={{ marginTop: '4rem', padding: '3rem', border: '1px dashed var(--border)', background: 'rgba(142, 45, 226, 0.02)', textAlign: 'center' }}>
            <h2 style={{ fontFamily: 'var(--display)', fontSize: '2rem', marginBottom: '1rem' }}>Developer Portal Status</h2>
            <p style={{ color: 'var(--text2)', fontFamily: 'var(--mono)', fontSize: '13px' }}>
              [SYNCING_REAL_TIME_BLUEPRINTS]... 84% COMPLETE
            </p>
            <div style={{ width: '200px', height: '2px', background: 'var(--border)', margin: '1rem auto', position: 'relative', overflow: 'hidden' }}>
              <div style={{ position: 'absolute', top: 0, left: 0, height: '100%', width: '84%', background: 'var(--accent)', boxShadow: '0 0 10px var(--accent-glow)' }}></div>
            </div>
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default DocsView;
