import React, { useEffect, useState } from 'react';
import { Activity, Shield, Globe, Cpu, Server, Zap, ArrowLeft, RefreshCcw } from 'lucide-react';
import './StatusView.css';

const StatusView = ({ onBack }) => {
  const [uptime, setUptime] = useState(99.9994);
  const [activeNodes, setActiveNodes] = useState(14204);

  useEffect(() => {
    const interval = setInterval(() => {
      setUptime(prev => prev + (Math.random() * 0.0001 - 0.00005));
      setActiveNodes(prev => prev + Math.floor(Math.random() * 5 - 2));
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="status-view premium-theme">
      <button className="back-btn-status" onClick={onBack}>
        <ArrowLeft size={14} style={{ marginRight: '8px' }} /> Return to Handshake
      </button>

      <div className="status-container">
        <header className="status-header">
          <div className="status-title-group">
            <span className="status-badge">Network Telemetry Active</span>
            <h1>System Status</h1>
          </div>
          <div className="status-sync">
            <RefreshCcw size={14} className="spin-slow" />
            <span style={{ fontFamily: 'var(--mono)', fontSize: '12px', color: 'var(--text3)' }}>
              LIVE SYNC: {new Date().toLocaleTimeString()}
            </span>
          </div>
        </header>

        <div className="status-stats-grid">
          <div className="stat-card">
            <span className="stat-label">Global Uptime</span>
            <div className="stat-value" style={{ color: 'var(--accent)' }}>{uptime.toFixed(4)}%</div>
          </div>
          <div className="stat-card">
            <span className="stat-label">Active Nodes</span>
            <div className="stat-value">{activeNodes.toLocaleString()}</div>
          </div>
          <div className="stat-card">
            <span className="stat-label">Threats Mitigated</span>
            <div className="stat-value">1.4M+</div>
          </div>
          <div className="stat-card">
            <span className="stat-label">PQC Latency</span>
            <div className="stat-value" style={{ color: 'var(--primary)' }}>14.2ms</div>
          </div>
        </div>

        <div className="status-visual-main">
          <div className="map-overlay"></div>
          <div className="scanning-line"></div>
          
          {/* PhD Level Visualization: Abstract Node Web */}
          <svg width="100%" height="100%" style={{ position: 'absolute', opacity: 0.4 }}>
            <defs>
              <radialGradient id="nodeGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.8" />
                <stop offset="100%" stopColor="var(--accent)" stopOpacity="0" />
              </radialGradient>
            </defs>
            {Array.from({ length: 40 }).map((_, i) => {
              const x = Math.random() * 100;
              const y = Math.random() * 100;
              return (
                <g key={i}>
                  <circle cx={`${x}%`} cy={`${y}%`} r="2" fill="var(--accent)">
                    <animate attributeName="opacity" values="0.2;1;0.2" dur={`${2 + Math.random() * 4}s`} repeatCount="indefinite" />
                  </circle>
                  <circle cx={`${x}%`} cy={`${y}%`} r="6" fill="url(#nodeGlow)">
                    <animate attributeName="r" values="4;8;4" dur={`${2 + Math.random() * 4}s`} repeatCount="indefinite" />
                  </circle>
                </g>
              );
            })}
          </svg>

          <div style={{ position: 'relative', zIndex: 5, textAlign: 'center' }}>
            <Globe size={120} className="spin-slow" style={{ color: 'var(--primary)', opacity: 0.8, filter: 'drop-shadow(0 0 30px var(--primary-glow))' }} />
            <h2 style={{ fontFamily: 'var(--display)', fontSize: '2rem', marginTop: '1rem', letterSpacing: '0.1em' }}>GLOBAL GRID NOMINAL</h2>
          </div>
        </div>

        <div className="node-grid">
          {[
            { name: 'US-EAST-01', type: 'Master Gateway', load: '14%' },
            { name: 'EU-CENTRAL-04', type: 'Kyber Relay', load: '32%' },
            { name: 'ASIA-PAC-02', type: 'Anomaly Core', load: '8%' },
            { name: 'BR-SOUTH-01', type: 'Edge Node', load: '21%' },
            { name: 'AF-WEST-03', type: 'Satellite Uplink', load: '45%' },
            { name: 'AU-EAST-01', type: 'Deep Archive', load: '2%' }
          ].map((node, i) => (
            <div className="node-card" key={i}>
              <div className="node-header">
                <div>
                  <div style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text)' }}>{node.name}</div>
                  <div style={{ fontSize: '10px', color: 'var(--text3)', fontFamily: 'var(--mono)' }}>{node.type}</div>
                </div>
                <div className="node-status"></div>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontFamily: 'var(--mono)', color: 'var(--text2)' }}>
                <span>LOAD</span>
                <span>{node.load}</span>
              </div>
              <div className="sparkline">
                {Array.from({ length: 24 }).map((_, j) => (
                  <div 
                    key={j} 
                    className="spark-bar" 
                    style={{ height: `${20 + Math.random() * 80}%` }}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default StatusView;
