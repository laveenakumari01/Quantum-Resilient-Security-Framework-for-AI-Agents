import React from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, Cpu, Cloud, Database, Shield, Zap, Globe, Terminal, Activity, MessageSquare } from 'lucide-react';
import './IntegrationsView.css';

const IntegrationsView = ({ onBack }) => {
  const integrations = [
    { name: 'AWS Lambda', icon: Cloud, desc: 'Direct agentic deployment into serverless environments.' },
    { name: 'GitHub Actions', icon: Terminal, desc: 'Automated PQC security audits on every pull request.' },
    { name: 'PostgreSQL', icon: Database, desc: 'Quantum-encrypted data streams for high-compliance databases.' },
    { name: 'Slack Ops', icon: Activity, desc: 'Real-time threat alerts and anomaly detection feeds.' },
    { name: 'Kubernetes', icon: Cpu, desc: 'Orchestrate XCIPHER nodes across distributed clusters.' },
    { name: 'Discord', icon: MessageSquare, desc: 'Community-driven security intelligence sharing.' }
  ];

  return (
    <div className="integrations-view premium-theme">
      <aside className="integrations-sidebar">
        <div className="docs-nav-group">
          <span className="docs-nav-label">Connectivity Mesh</span>
          <div className="docs-nav-link active"><Cloud size={14} /> Cloud Platforms</div>
          <div className="docs-nav-link"><Database size={14} /> Data Streams</div>
          <div className="docs-nav-link"><Cpu size={14} /> Infrastructure</div>
        </div>

        <div className="docs-nav-group" style={{ marginTop: 'auto' }}>
          <div className="docs-nav-link" onClick={onBack}>
            <ArrowLeft size={14} /> Back to Dashboard
          </div>
        </div>
      </aside>

      <main className="integrations-content">
        <motion.div initial={{ opacity: 0, scale: 0.98 }} animate={{ opacity: 1, scale: 1 }}>
          <header className="docs-header">
            <span className="blog-meta" style={{ color: 'var(--accent)' }}>[ CONNECTIVITY_MESH_v4 ]</span>
            <h1 style={{ color: 'var(--primary)', textShadow: '0 0 40px var(--primary-glow)' }}>Integrations</h1>
            <p style={{ color: 'var(--text2)', fontSize: '18px' }}>Deploy XCIPHER natively into your existing stack in under 300 seconds.</p>
          </header>

          <div className="handshake-hub">
            <div className="hub-line"></div>
            <div className="hub-line" style={{ animationDelay: '-5s' }}></div>
            <Globe size={100} style={{ color: 'var(--accent)', filter: 'drop-shadow(0 0 20px var(--accent-glow))' }} />
            <div style={{ position: 'absolute', bottom: '2rem', fontFamily: 'var(--mono)', fontSize: '10px', color: 'var(--text3)' }}>
              CENTRAL_HANDSHAKE_HUB_ACTIVE
            </div>
          </div>

          <div className="integrations-grid">
            {integrations.map((item, i) => (
              <div key={i} className="integration-card">
                <div className="integration-icon">
                  <item.icon size={28} />
                </div>
                <div className="integration-name">{item.name}</div>
                <p className="integration-desc">{item.desc}</p>
                <div style={{ marginTop: '1.5rem', color: 'var(--primary)', fontSize: '11px', fontFamily: 'var(--mono)', cursor: 'pointer', fontWeight: 600 }}>
                  CONFIGURE NODE
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default IntegrationsView;
