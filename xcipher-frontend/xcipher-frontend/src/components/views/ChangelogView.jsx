import React from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, GitCommit, Shield, Zap, Terminal } from 'lucide-react';
import './ChangelogView.css';
import changelogHero from '../../assets/changelog_hero_1777821960909.png';

const ChangelogView = ({ onBack }) => {
  const logs = [
    {
      version: 'v4.2.0',
      date: 'MAY 01, 2026',
      title: 'Quantum Mesh Expansion',
      impact: 'Major',
      items: [
        'Implemented CRYSTALS-Kyber Level 5 encryption for all regional gateways.',
        'New "Neural Handshake" protocol reduces identity verification latency by 42%.',
        'Added support for satellite-based edge nodes in high-entropy zones.'
      ]
    },
    {
      version: 'v4.1.2',
      date: 'APR 20, 2026',
      title: 'Agentic Core Optimization',
      impact: 'Stable',
      items: [
        'Refined memory sandbox for autonomous AI agents.',
        'Fixed race condition in cross-border telemetry sync.',
        'Enhanced RBAC granularity for Level 4 security clearing.'
      ]
    },
    {
      version: 'v4.0.0',
      date: 'APR 05, 2026',
      title: 'XCIPHER Rebrand & PQC Launch',
      impact: 'Critical',
      items: [
        'Complete platform migration to the XCIPHER Post-Quantum architecture.',
        'Legacy AES wrapping replaced with hybrid Kyber-AES-256 encapsulation.',
        'Launch of the Global Defense Command Center (NOC).'
      ]
    }
  ];

  return (
    <div className="changelog-view premium-theme">
      <main className="changelog-content">
        <button className="back-btn-docs" onClick={onBack} style={{ marginBottom: '4rem' }}>
          <ArrowLeft size={14} /> Back to Dashboard
        </button>

        <motion.div initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }}>
          <header className="docs-header" style={{ marginBottom: '6rem', textAlign: 'center' }}>
            <span className="blog-meta" style={{ color: 'var(--accent)' }}>[ SYSTEM_LEDGER_ACTIVE ]</span>
            <h1 style={{ color: 'var(--primary)', textShadow: '0 0 40px var(--primary-glow)' }}>Changelog</h1>
            <p style={{ color: 'var(--text2)', fontSize: '18px', maxWidth: '800px', margin: '0 auto' }}>Tracking the evolution of autonomous security protocols.</p>
            
            <img src={changelogHero} alt="Changelog Visual" style={{ width: '100%', marginTop: '3rem', borderRadius: '24px', border: '1px solid var(--border)', opacity: 0.8 }} />
          </header>

          <div className="changelog-timeline">
            {logs.map((log, i) => (
              <div key={i} className="changelog-entry">
                <div className="changelog-meta">
                  <span className="version-tag">{log.version}</span>
                  <span className="date-tag">{log.date}</span>
                  <span className="impact-badge">{log.impact}</span>
                </div>
                <div className="changelog-card">
                  <h3 className="changelog-title">{log.title}</h3>
                  <ul className="changelog-list">
                    {log.items.map((item, j) => (
                      <li key={j} className="changelog-item">{item}</li>
                    ))}
                  </ul>
                  <div style={{ marginTop: '2rem', display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text3)', fontSize: '11px', fontFamily: 'var(--mono)' }}>
                    <GitCommit size={12} /> COMMIT_HASH: {Math.random().toString(16).substring(2, 10).toUpperCase()}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      </main>
    </div>
  );
};

export default ChangelogView;
