import React from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, Terminal, Cpu, Network, Lock } from 'lucide-react';

const ExecutionPlanView = ({ onBack }) => {
  return (
    <div className="premium-theme" style={{ minHeight: '100vh', background: 'var(--bg)', color: 'var(--text)', fontFamily: 'var(--body)', padding: '2rem' }}>
      <button 
        onClick={onBack}
        className="interactive"
        style={{
          background: 'rgba(255,255,255,0.03)', border: '1px solid var(--border)',
          display: 'flex', alignItems: 'center', gap: '8px',
          fontWeight: 500, cursor: 'pointer', color: 'var(--text2)',
          padding: '10px 16px', borderRadius: '100px',
          fontSize: '13px', transition: 'all 0.3s',
          marginBottom: '2rem'
        }}
        onMouseEnter={(e) => { e.currentTarget.style.color = 'var(--text)'; e.currentTarget.style.background = 'rgba(255,255,255,0.06)'; }}
        onMouseLeave={(e) => { e.currentTarget.style.color = 'var(--text2)'; e.currentTarget.style.background = 'rgba(255,255,255,0.03)'; }}
      >
        <ArrowLeft size={16} /> Back
      </button>

      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} style={{ maxWidth: '900px', margin: '0 auto' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '2rem' }}>
          <div style={{ background: 'rgba(0, 102, 255, 0.1)', padding: '16px', borderRadius: '20px', border: '1px solid rgba(0, 102, 255, 0.2)' }}>
            <Terminal size={32} color="var(--blue)" />
          </div>
          <h1 style={{ fontSize: '48px', fontFamily: 'var(--display)', letterSpacing: '0.04em' }}>Quantum Execution Plan</h1>
        </div>

        <div style={{ background: 'var(--surface)', padding: '3rem', borderRadius: '24px', border: '1px solid var(--border)', marginBottom: '3rem' }}>
          <h2 style={{ fontSize: '24px', marginBottom: '1.5rem', color: 'var(--cyan)' }}>Phase 1: Agent Initialization</h2>
          <p style={{ color: 'var(--text2)', lineHeight: 1.6, marginBottom: '2rem' }}>
            Upon deployment, the XCIPHER architecture establishes a zero-trust handshake utilizing CRYSTALS-Kyber key encapsulation. This ensures that the initial connection vector is entirely resistant to Shor's algorithm and future quantum decryption attacks.
          </p>
          
          <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
            <div style={{ flex: 1, background: 'var(--surface2)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border)' }}>
              <Cpu size={24} color="var(--cyan)" style={{ marginBottom: '1rem' }} />
              <h4 style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Hardware Integrity</h4>
              <p style={{ fontSize: '13px', color: 'var(--text3)' }}>Validating underlying compute instances for physical tampering or memory leaks.</p>
            </div>
            <div style={{ flex: 1, background: 'var(--surface2)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border)' }}>
              <Network size={24} color="var(--blue)" style={{ marginBottom: '1rem' }} />
              <h4 style={{ fontWeight: 600, marginBottom: '0.5rem' }}>Mesh Networking</h4>
              <p style={{ fontSize: '13px', color: 'var(--text3)' }}>Establishing secure P2P mesh routes between isolated agent nodes.</p>
            </div>
            <div style={{ flex: 1, background: 'var(--surface2)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border)' }}>
              <Lock size={24} color="var(--red)" style={{ marginBottom: '1rem' }} />
              <h4 style={{ fontWeight: 600, marginBottom: '0.5rem' }}>JWT Minting</h4>
              <p style={{ fontSize: '13px', color: 'var(--text3)' }}>Issuing strict, time-limited JWTs signed with post-quantum algorithms.</p>
            </div>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default ExecutionPlanView;
