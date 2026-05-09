import React, { useState, useEffect, useRef } from 'react';
import './DashboardView.css';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Layers, Shield, AlertCircle, 
  Terminal, BarChart, Users, Settings, 
  Search, Bell, LogOut, Globe, Cpu, 
  CheckCircle, XCircle, Plus, Activity, Lock, Eye
} from 'lucide-react';

const BASE_URL = "http://localhost:8000";

// Backend se data fetch karne ke functions
async function fetchFromBackend(endpoint) {
  const token = localStorage.getItem("token");
  try {
    const res = await fetch(`${BASE_URL}${endpoint}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    if (!res.ok) return null;
    return await res.json();
  } catch (e) {
    return null;
  }
}

const DashboardView = ({ onLogout }) => {
  const [activeTab, setActiveTab] = useState('Overview');
  const [threats, setThreats] = useState([]);
  const [logs, setLogs] = useState([]);
  const [activities, setActivities] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [showRegisterModal, setShowRegisterModal] = useState(false);
  const [stats, setStats] = useState({
    total_detections: 0,
    active_threats: 0,
    system_health: '99.9%',
    audit_requests: 0,
    security_score: 98
  });
  const [agents, setAgents] = useState([]);
  const logEndRef = useRef(null);

  // fetching real data from backend
  useEffect(() => {
    const loadBackendData = async () => {
      // fetching Stats 
      const statsData = await fetchFromBackend('/agent/stats');
      if (statsData) setStats(statsData);

      // fetching Alerts 
      const alertsData = await fetchFromBackend('/alerts');
      if (alertsData && Array.isArray(alertsData) && alertsData.length > 0) {
        const formatted = alertsData.map((a, i) => ({
          id: a.agent_id + i,
          type: a.event,
          severity: a.severity || 'Medium',
          time: new Date(a.timestamp).toLocaleTimeString(),
          ip: a.agent_id || 'Unknown-Node',
          status: 'Isolating'
        }));
        setThreats(formatted);
      } else {
        // Fallback simulation 
        setThreats([
          { id: 't1', type: 'PQC Handshake Failed', severity: 'Critical', time: new Date().toLocaleTimeString(), ip: 'Agent-Node-08', status: 'Isolating' },
          { id: 't2', type: 'Token Anomaly', severity: 'Medium', time: new Date(Date.now() - 5000).toLocaleTimeString(), ip: 'Agent-Node-99', status: 'Isolating' }
        ]);
      }

      // fetching Logs
      const logsData = await fetchFromBackend('/agent/logs');
      if (logsData && logsData.logs && logsData.logs.length > 0) {
        const formatted = logsData.logs.map(l =>
          `[${l.timestamp}] ${l.status}: ${l.agent} - ${l.action}`
        );
        setLogs(formatted);
      } else {
        setLogs([
          `[${new Date().toLocaleTimeString()}] INFO: Zero-trust heartbeat verified on Master-Node`,
          `[${new Date().toLocaleTimeString()}] SYSTEM: PQC Engine nominal. Latency 4ms.`
        ]);
      }

      // fetching Agents 
      const agentsData = await fetchFromBackend('/rbac/all-agents');
      if (agentsData && agentsData.agents) {
        const formatted = agentsData.agents.map(a => ({
          name: a.username,
          email: a.email,
          role: a.role,
          level: a.role === 'admin' ? 'Level 5 (Full)' : a.role === 'agent' ? 'Level 3 (Agent)' : 'Level 1 (View)',
          status: a.disabled ? 'Offline' : 'Active',
          time: 'Now'
        }));
        setAgents(formatted);
      }

      // fetching Agent Activity  —  from backend logs 
      const activityData = await fetchFromBackend('/logs');
      if (activityData && Array.isArray(activityData) && activityData.length > 0) {
        const formatted = activityData.map((l, i) => ({
          id: i,
          agent: l.agent_id || 'Unknown',
          action: l.event || 'Activity',
          time: new Date(l.timestamp).toLocaleTimeString(),
          status: l.level === 'ALERT' ? 'ALERT' : 'SUCCESS'
        }));
        setActivities(formatted);
      }
    };

    loadBackendData();

    // data refresh after each 10 seconds
    const refreshInterval = setInterval(loadBackendData, 10000);

    // Live simulation (frontend activity)
    const interval = setInterval(() => {
      const now = new Date().toLocaleTimeString();
      if (Math.random() > 0.7) {
        const newThreat = {
          id: Math.random().toString(36).substr(2, 9),
          type: ['Agent Desync', 'PQC Handshake Failed', 'Token Anomaly', 'Unauthorized API', 'Data Exfiltration'][Math.floor(Math.random() * 5)],
          severity: ['High', 'Critical', 'Medium'][Math.floor(Math.random() * 3)],
          time: now,
          ip: `Agent-Node-${Math.floor(Math.random()*999)}`,
          status: 'Isolating'
        };
        setThreats(prev => [newThreat, ...prev].slice(0, 8));
        const logEntry = `[${now}] ALERT: ${newThreat.type} on ${newThreat.ip} - Sev: ${newThreat.severity}`;
        setLogs(prev => [...prev, logEntry].slice(-40));
      } else if (Math.random() > 0.2) {
        const agentId = `Node-${Math.floor(Math.random()*200)}`;
        const actions = ['Verified Handshake', 'Encrypted Packet', 'Rotated Keys', 'Sync Pulse', 'Tunnel Established'];
        const newActivity = {
          id: Date.now(),
          agent: agentId,
          action: actions[Math.floor(Math.random() * actions.length)],
          time: now,
          status: 'SUCCESS'
        };
        setActivities(prev => [newActivity, ...prev].slice(0, 15));
        const standardLog = `[${now}] INFO: ${agentId} - ${newActivity.action}`;
        setLogs(prev => [...prev, standardLog].slice(-40));
      }
    }, 1500);

    return () => {
      clearInterval(interval);
      clearInterval(refreshInterval);
    };
  }, []);

  const OverviewContent = () => (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '1.5rem' }}>
        {[
          { label: 'Isolated Agents', val: String(stats.active_threats || 0), change: '+2', color: 'var(--red)' },
          { label: 'PQC Integrity', val: '100%', change: 'SECURE', color: 'var(--accent)' },
          { label: 'Anomalies Blocked', val: String(stats.total_detections || 0), change: 'LIVE', color: 'var(--primary)' },
          { label: 'Security Score', val: `${stats.security_score || 98}%`, change: stats.system_health || '99.9%', color: 'var(--blue)' }
        ].map((stat, idx) => (
          <div key={idx} className="phd-dash-module" style={{ padding: '1.5rem' }}>
            <div className="phd-dash-header">{stat.label}</div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <span className="phd-dash-stat-val">{stat.val}</span>
              <span style={{ fontSize: '9px', fontFamily: 'var(--mono)', color: stat.color, background: 'rgba(255,255,255,0.03)', padding: '2px 8px', border: `1px solid ${stat.color}40` }}>{stat.change}</span>
            </div>
            <div style={{ height: '2px', width: '100%', background: 'rgba(255,255,255,0.05)', marginTop: '1.5rem', overflow: 'hidden' }}>
              <motion.div initial={{ width: 0 }} animate={{ width: `${60 + Math.random() * 40}%` }} transition={{ duration: 1 }} style={{ height: '100%', background: stat.color, boxShadow: `0 0 10px ${stat.color}` }} />
            </div>
          </div>
        ))}
      </div>
      
      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
        <div className="phd-dash-module" style={{ padding: '2rem', height: '400px', display: 'flex', flexDirection: 'column' }}>
          <div className="phd-radar-bg"></div>
          <h3 className="phd-dash-header" style={{ position: 'relative', zIndex: 1 }}>
            <Activity size={14} /> SYSTEM PULSE [ENCRYPTED_FEED]
          </h3>
          <div style={{ flex: 1, display: 'flex', alignItems: 'flex-end', gap: '4px', overflow: 'hidden', position: 'relative', zIndex: 1 }}>
            {Array.from({ length: 40 }).map((_, i) => (
              <motion.div 
                key={i} 
                animate={{ height: `${20 + Math.random() * 60}%` }}
                transition={{ duration: 1.5, ease: "easeInOut", repeat: Infinity, repeatType: "mirror", delay: i * 0.05 }}
                className="phd-pulse-bar"
              />
            ))}
          </div>
        </div>
        
        <div className="phd-dash-module" style={{ padding: '2rem', height: '400px', display: 'flex', flexDirection: 'column' }}>
          <h3 className="phd-dash-header">
            <AlertCircle size={14} /> RECENT ISOLATIONS
          </h3>
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '8px', overflowY: 'auto', paddingRight: '4px' }}>
            <AnimatePresence initial={false}>
              {threats.map(t => (
                <motion.div 
                  key={t.id} 
                  initial={{ opacity: 0, x: 10 }} 
                  animate={{ opacity: 1, x: 0 }} 
                  style={{ padding: '12px', borderLeft: `2px solid ${t.severity === 'Critical' ? 'var(--red)' : 'var(--primary)'}`, background: 'rgba(255,255,255,0.02)', border: '1px solid var(--border)', clipPath: 'polygon(4px 0, 100% 0, 100% calc(100% - 4px), calc(100% - 4px) 100%, 0 100%, 0 4px)' }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', fontFamily: 'var(--mono)', color: 'var(--text)' }}>
                    <span>{t.type}</span>
                    <span style={{ color: 'var(--text3)' }}>{t.time}</span>
                  </div>
                  <div style={{ fontSize: '10px', fontFamily: 'var(--mono)', color: 'var(--accent)', marginTop: '4px' }}>{t.ip}</div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>
        </div>
      </div>
    </motion.div>
  );

  const ActivityContent = () => (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div className="phd-dash-module" style={{ padding: '2rem' }}>
        <h3 className="phd-dash-header"><Activity size={14} /> LIVE_ACTIVITY_STREAM</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <AnimatePresence initial={false}>
            {activities.map(act => (
              <motion.div 
                key={act.id} 
                initial={{ opacity: 0, x: -10 }} 
                animate={{ opacity: 1, x: 0 }} 
                style={{ 
                  padding: '14px 20px', 
                  background: 'rgba(255,255,255,0.02)', 
                  border: '1px solid var(--border)',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  fontFamily: 'var(--mono)',
                  fontSize: '12px',
                  clipPath: 'polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px)'
                }}
              >
                <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                  <span style={{ color: 'var(--primary)', fontWeight: 800 }}>[{act.agent}]</span>
                  <span style={{ color: 'var(--text)' }}>{act.action}</span>
                </div>
                <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
                  <span style={{ color: 'var(--accent)', fontSize: '10px' }}>{act.status}</span>
                  <span style={{ color: 'var(--text3)', fontSize: '10px' }}>{act.time}</span>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      </div>
    </motion.div>
  );

  const LogsTerminalContent = () => (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} style={{ height: '600px', display: 'flex', flexDirection: 'column' }}>
      <div className="phd-dash-module" style={{ padding: '2rem', flex: 1, color: 'var(--accent)', fontFamily: 'var(--mono)', overflowY: 'auto' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--text3)', fontSize: '10px', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '1rem' }}>
          <span>XCIPHER_TERM_v4.2</span>
          <span style={{ color: 'var(--primary)' }}>[ PQC_TUNNEL_ACTIVE ]</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {logs.map((log, i) => (
            <div key={i} style={{ fontSize: '12px', lineHeight: 1.5, color: log.includes('ALERT') ? 'var(--red)' : log.includes('SYSTEM') ? 'var(--primary)' : 'var(--text2)' }}>
              <span style={{ color: 'var(--text3)', marginRight: '8px' }}>&gt;</span> {log}
            </div>
          ))}
          <div ref={logEndRef} />
        </div>
      </div>
      <div style={{ marginTop: '1.5rem', display: 'flex', gap: '1rem' }}>
        <button className="phd-dash-btn" style={{ flex: 1 }}>PAUSE_SCAN</button>
        <button className="phd-dash-btn" style={{ flex: 1 }}>FLUSH_BUFFER</button>
        <button className="phd-dash-btn" style={{ flex: 1, background: 'var(--primary)', color: '#fff' }}>EXPORT_LEDGER</button>
      </div>
    </motion.div>
  );

  const AlertsContent = () => (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <div style={{ padding: '2rem', background: 'rgba(255, 51, 85, 0.05)', border: '1px solid var(--red)', clipPath: 'polygon(20px 0, 100% 0, 100% calc(100% - 20px), calc(100% - 20px) 100%, 0 100%, 0 20px)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
          <div>
            <h3 style={{ color: 'var(--red)', fontSize: '18px', fontFamily: 'var(--display)', margin: 0, display: 'flex', alignItems: 'center', gap: '10px' }}>
              <AlertCircle className="pulse-red" size={24} /> CRITICAL_THREAT_MONITOR
            </h3>
            <p style={{ color: 'var(--text2)', fontSize: '12px', marginTop: '5px', fontFamily: 'var(--mono)' }}>ENFORCING PROTOCOL: PQC_SHIELD_v8</p>
          </div>
          <button className="phd-dash-btn" style={{ borderColor: 'var(--red)', color: 'var(--red)' }}>ACTIVATE LOCKDOWN</button>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem' }}>
          {[
            { label: 'ACTIVE_THREATS', val: String(stats.active_threats || 0), color: 'var(--red)' },
            { label: 'AUDIT_REQUESTS', val: String(stats.audit_requests || 0), color: 'var(--amber)' },
            { label: 'TOTAL_DETECTIONS', val: String(stats.total_detections || 0), color: 'var(--accent)' }
          ].map((stat, i) => (
            <div key={i} style={{ padding: '1.5rem', background: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.05)' }}>
              <div style={{ fontSize: '9px', color: 'var(--text3)', fontFamily: 'var(--mono)', marginBottom: '8px' }}>{stat.label}</div>
              <div style={{ fontSize: '24px', color: stat.color, fontFamily: 'var(--display)' }}>{stat.val}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="phd-dash-module" style={{ padding: '2rem' }}>
        <h3 className="phd-dash-header">BREACH_ANALYSIS_LOG</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {threats.map((t, i) => (
            <div key={i} style={{ display: 'flex', gap: '20px', padding: '15px', borderBottom: '1px solid rgba(255,255,255,0.03)', fontFamily: 'var(--mono)', fontSize: '11px' }}>
              <span style={{ color: 'var(--red)' }}>[!!!]</span>
              <span style={{ color: 'var(--text)', width: '100px' }}>{t.time}</span>
              <span style={{ color: 'var(--accent)', width: '150px' }}>{t.ip}</span>
              <span style={{ color: 'var(--text2)', flex: 1 }}>{t.type} - SEVERITY: {t.severity.toUpperCase()}</span>
              <span style={{ color: 'var(--primary)' }}>[ISOLATED]</span>
            </div>
          ))}
        </div>
      </div>
    </motion.div>
  );

  const AnalyticsContent = () => (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1.5rem' }}>
        <div className="phd-dash-module" style={{ padding: '2rem', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h4 className="phd-dash-header">SECURITY_SCORE</h4>
          <div style={{ position: 'relative', width: '160px', height: '160px', marginTop: '1rem' }}>
             <svg width="160" height="160" viewBox="0 0 100 100">
               <circle cx="50" cy="50" r="45" fill="none" stroke="rgba(255,255,255,0.05)" strokeWidth="4" />
               <motion.circle cx="50" cy="50" r="45" fill="none" stroke="var(--accent)" strokeWidth="4" strokeDasharray="283" initial={{ strokeDashoffset: 283 }} animate={{ strokeDashoffset: 283 - (283 * (stats.security_score || 98) / 100) }} transition={{ duration: 2 }} strokeLinecap="square" transform="rotate(-90 50 50)" />
             </svg>
             <div style={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', fontSize: '28px', fontFamily: 'var(--display)', color: 'var(--text)' }}>{stats.security_score || 98}%</div>
          </div>
          <p style={{ fontSize: '10px', color: 'var(--text3)', marginTop: '1.5rem', fontFamily: 'var(--mono)' }}>SYSTEM_HEALTH: {stats.system_health || '99.9%'}</p>
        </div>
        <div className="phd-dash-module" style={{ padding: '2rem', gridColumn: 'span 2', position: 'relative' }}>
           <h4 className="phd-dash-header">ANOMALY_TREND_ANALYSIS</h4>
           <div style={{ height: '180px', display: 'flex', alignItems: 'flex-end', gap: '8px', marginTop: '1rem' }}>
             {[30, 45, 20, 60, 40, 80, 50, 70, 90, 60, 40, 55].map((v, i) => (
               <motion.div 
                 key={i} 
                 initial={{ height: 0 }}
                 animate={{ height: `${v}%` }}
                 transition={{ delay: i * 0.05 }}
                 style={{ flex: 1, background: 'linear-gradient(to top, var(--primary), var(--accent))', opacity: 0.7, boxShadow: '0 0 10px var(--primary-glow)' }} 
               />
             ))}
           </div>
           <div style={{ position: 'absolute', top: '2rem', right: '2rem', display: 'flex', gap: '20px' }}>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: '10px', color: 'var(--text3)', fontFamily: 'var(--mono)' }}>TOTAL_DETECTIONS</div>
                <div style={{ fontSize: '14px', color: 'var(--primary)', fontFamily: 'var(--display)' }}>{stats.total_detections || 0}</div>
              </div>
           </div>
        </div>
      </div>
    </motion.div>
  );

  const AccessControlContent = () => (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
       <div className="phd-dash-module" style={{ padding: '2.5rem' }}>
         <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2.5rem' }}>
           <h3 style={{ fontSize: '14px', fontFamily: 'var(--mono)', color: 'var(--text)', margin: 0, display: 'flex', alignItems: 'center', gap: '10px' }}><Lock size={16} color="var(--accent)" /> RBAC_CLEARANCE_MATRIX</h3>
           <button onClick={() => setShowRegisterModal(true)} className="phd-dash-btn" style={{ background: 'rgba(0,245,212,0.1)', color: 'var(--accent)', borderColor: 'var(--accent)' }}><Plus size={14} /> REGISTER_NODE</button>
         </div>
         <table style={{ width: '100%', borderCollapse: 'collapse' }}>
           <thead>
             <tr style={{ textAlign: 'left', borderBottom: '1px solid var(--border)', color: 'var(--text3)', fontSize: '10px', fontFamily: 'var(--mono)', textTransform: 'uppercase', letterSpacing: '0.1em' }}>
               <th style={{ padding: '1.25rem 1rem' }}>IDENTIFIER</th>
               <th>ROLE</th>
               <th>CLEARANCE</th>
               <th>STATUS</th>
               <th>HEARTBEAT</th>
             </tr>
           </thead>
           <tbody>
             {agents.map((u, i) => (
               <tr key={i} style={{ borderBottom: '1px solid rgba(255,255,255,0.02)', fontFamily: 'var(--mono)', fontSize: '12px' }}>
                 <td style={{ padding: '1.5rem 1rem' }}>
                   <div style={{ color: 'var(--text)', fontWeight: 700 }}>{u.name}</div>
                   <div style={{ fontSize: '10px', color: 'var(--text3)', marginTop: '4px' }}>UUID: {Math.random().toString(16).substr(2, 8)}</div>
                 </td>
                 <td><span style={{ color: 'var(--text2)' }}>{u.role}</span></td>
                 <td><span style={{ background: 'rgba(138,43,226,0.1)', padding: '4px 10px', border: '1px solid var(--primary-glow)', color: 'var(--primary)', fontSize: '10px' }}>{u.level}</span></td>
                 <td><div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: u.status === 'Active' ? 'var(--accent)' : 'var(--text3)' }}>
                   {u.status === 'Active' ? <CheckCircle size={14} /> : <XCircle size={14} />} {u.status}
                 </div></td>
                 <td style={{ color: 'var(--text3)', fontSize: '10px' }}>{u.time}</td>
               </tr>
             ))}
           </tbody>
         </table>
       </div>
    </motion.div>
  );

  const ThreatIntelContent = () => (
    <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: '1.5rem' }}>
        <div className="phd-dash-module" style={{ padding: '2rem', height: '450px', position: 'relative', overflow: 'hidden' }}>
          <div className="phd-radar-bg"></div>
          <h3 className="phd-dash-header"><Globe size={14} /> GLOBAL_MESH_TOPOLOGY [LIVE]</h3>
          <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
             <motion.div animate={{ rotate: 360 }} transition={{ duration: 60, repeat: Infinity, ease: "linear" }} style={{ opacity: 0.15 }}>
               <Globe size={280} color="var(--primary)" />
             </motion.div>
             {[
               { top: '30%', left: '40%' }, { top: '50%', left: '60%' }, 
               { top: '20%', left: '70%' }, { top: '65%', left: '35%' },
               { top: '45%', left: '25%' }
             ].map((pt, i) => (
               <motion.div key={i} animate={{ scale: [1, 1.5, 1], opacity: [1, 0, 1] }} transition={{ repeat: Infinity, duration: 3, delay: i * 0.6 }} style={{ position: 'absolute', top: pt.top, left: pt.left, width: '8px', height: '8px', background: 'var(--accent)', borderRadius: '50%', boxShadow: '0 0 15px var(--accent-glow)' }} />
             ))}
             <div style={{ position: 'absolute', bottom: '0', left: '0', background: 'rgba(0,0,0,0.6)', padding: '1.5rem', borderTop: '1px solid var(--border)', borderRight: '1px solid var(--border)', fontFamily: 'var(--mono)', fontSize: '10px' }}>
                <div style={{ color: 'var(--accent)', marginBottom: '8px' }}>[STATUS] // SYSTEM_NOMINAL</div>
                <div style={{ color: 'var(--text2)' }}>ACTIVE_NODES: 1,204</div>
             </div>
          </div>
        </div>
        <div className="phd-dash-module" style={{ padding: '2rem', display: 'flex', flexDirection: 'column' }}>
          <h3 className="phd-dash-header"><Shield size={14} /> THREAT_VECTOR_LEDGER</h3>
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '15px', overflowY: 'auto' }}>
            {threats.map((t, i) => (
              <div key={i} style={{ padding: '12px', border: '1px solid rgba(255,255,255,0.03)', background: 'rgba(255,255,255,0.01)', position: 'relative', borderLeft: '2px solid var(--red)' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
                  <span style={{ fontSize: '10px', color: 'var(--red)', fontFamily: 'var(--mono)' }}>[ HIGH_SEV ]</span>
                  <span style={{ fontSize: '10px', color: 'var(--text3)', fontFamily: 'var(--mono)' }}>{t.time}</span>
                </div>
                <div style={{ fontSize: '12px', color: 'var(--text)', fontWeight: 600 }}>{t.type}</div>
                <div style={{ fontSize: '10px', color: 'var(--text3)', marginTop: '4px', fontFamily: 'var(--mono)' }}>SOURCE: {t.ip}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className="phd-dash-module" style={{ padding: '2rem' }}>
        <h3 className="phd-dash-header"><Activity size={14} /> NODE_HEALTH_TELEMETRY</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '1.5rem' }}>
          {['US-EAST', 'EU-WEST', 'ASIA-PAC', 'SA-SOUTH', 'AF-NORTH'].map((region, i) => (
            <div key={i} style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: 'var(--text3)', fontFamily: 'var(--mono)', marginBottom: '10px' }}>{region}</div>
              <div style={{ height: '4px', background: 'rgba(255,255,255,0.05)', overflow: 'hidden' }}>
                 <motion.div initial={{ width: 0 }} animate={{ width: `${85 + Math.random() * 15}%` }} style={{ height: '100%', background: 'var(--accent)', boxShadow: '0 0 10px var(--accent-glow)' }} />
              </div>
              <div style={{ fontSize: '11px', color: 'var(--accent)', marginTop: '8px', fontWeight: 800 }}>99.9%</div>
            </div>
          ))}
        </div>
      </div>
    </motion.div>
  );

  const SettingsContent = () => (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="phd-dash-module" style={{ padding: '3rem' }}>
       <h3 className="phd-dash-header"><Settings size={14} /> SYSTEM_PARAMETERS</h3>
       <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem', maxWidth: '500px' }}>
          {[
            { label: 'Quantum Resilient Tunneling', desc: 'Enforce NIST-standard PQC handshake for all nodes.' },
            { label: 'Zero-Trust Heartbeat', desc: 'Verify agent identity every 500ms.' },
            { label: 'Neural Threat Detection', desc: 'Enable AI-driven anomaly recognition.' }
          ].map((s, i) => (
            <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid rgba(255,255,255,0.05)', paddingBottom: '1.5rem' }}>
               <div>
                  <div style={{ fontSize: '14px', color: 'var(--text)', fontFamily: 'var(--display)' }}>{s.label}</div>
                  <div style={{ fontSize: '11px', color: 'var(--text3)', marginTop: '4px' }}>{s.desc}</div>
               </div>
               <div style={{ width: '40px', height: '20px', background: 'var(--primary)', borderRadius: '20px', position: 'relative', cursor: 'pointer' }}>
                  <div style={{ position: 'absolute', right: '4px', top: '4px', width: '12px', height: '12px', background: '#fff', borderRadius: '50%' }} />
               </div>
            </div>
          ))}
       </div>
    </motion.div>
  );

  const renderContent = () => {
    switch (activeTab) {
      case 'Overview': return OverviewContent();
      case 'Agent Activity': return ActivityContent();
      case 'Security Alerts': return AlertsContent();
      case 'Threat Intelligence': return ThreatIntelContent();
      case 'Logs Terminal': return LogsTerminalContent();
      case 'Analytics': return AnalyticsContent();
      case 'Access Control': return AccessControlContent();
      case 'Settings': return SettingsContent();
      default: return OverviewContent();
    }
  };

  return (
    <div className="premium-theme dashboard-container" style={{ display: 'flex', minHeight: '100vh', background: 'var(--bg)', position: 'relative', zIndex: 10 }}>
      {/* Sidebar */}
      <aside className="phd-dash-sidebar" style={{ width: '280px', margin: '1.5rem', height: 'calc(100vh - 3rem)', position: 'sticky', top: '1.5rem', display: 'flex', flexDirection: 'column' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '0 24px', marginBottom: '2rem' }}>
          <Shield size={20} color="var(--primary)" />
          <span style={{ fontSize: '18px', fontFamily: 'var(--display)', color: 'var(--text)', letterSpacing: '0.15em', fontWeight: 900 }}>XCIPHER</span>
        </div>

        <nav style={{ display: 'flex', flexDirection: 'column', width: '100%', gap: '2px' }}>
          {[
            { label: 'Overview', icon: Layers },
            { label: 'Agent Activity', icon: Activity },
            { label: 'Security Alerts', icon: AlertCircle },
            { label: 'Threat Intelligence', icon: Globe },
            { label: 'Logs Terminal', icon: Terminal },
            { label: 'Analytics', icon: BarChart },
            { label: 'Access Control', icon: Users },
            { label: 'Settings', icon: Settings },
          ].map((item, idx) => (
            <div 
              key={idx}
              className={`phd-dash-nav-item ${activeTab === item.label ? 'active' : ''}`}
              onClick={() => setActiveTab(item.label)}
            >
              <item.icon size={14} />
              {item.label}
            </div>
          ))}
        </nav>

        <div style={{ marginTop: 'auto', paddingTop: '1.5rem', borderTop: '1px solid var(--border)', padding: '0 20px 0 20px' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(255,51,85,0.02)', border: '1px solid rgba(255,51,85,0.15)', marginBottom: '1rem', borderRadius: '4px', clipPath: 'polygon(4px 0, 100% 0, 100% calc(100% - 4px), calc(100% - 4px) 100%, 0 100%, 0 4px)' }}>
            <div style={{ fontSize: '8px', color: 'var(--red)', fontFamily: 'var(--mono)', marginBottom: '4px', letterSpacing: '0.1em', opacity: 0.8 }}>SESSION_ENCRYPTION</div>
            <div style={{ fontSize: '10px', color: 'var(--text)', fontFamily: 'var(--mono)', letterSpacing: '0.05em' }}>AES-256-GCM [ACTIVE]</div>
          </div>
          <button className="phd-dash-btn" onClick={onLogout} style={{ width: '100%', borderColor: 'rgba(255,51,85,0.4)', color: 'var(--red)', fontSize: '10px', padding: '10px 0' }}>
            [ TERMINATE SESSION ]
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main style={{ flex: 1, padding: '2rem 2.5rem 2rem 1rem', display: 'flex', flexDirection: 'column', gap: '2rem' }}>
        <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(10,20,40,0.4)', padding: '1rem 2rem', borderRadius: '20px', border: '1px solid var(--border)', backdropFilter: 'blur(20px)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
            <div style={{ fontFamily: 'var(--mono)', fontSize: '11px', color: 'var(--text3)', letterSpacing: '0.2em', whiteSpace: 'nowrap' }}>
              <span style={{ color: 'var(--primary)', fontWeight: 800 }}>XCIPHER</span> // {activeTab.toUpperCase()}
            </div>
            <div style={{ position: 'relative', width: '300px' }}>
              <Search size={14} style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text3)' }} />
              <input placeholder="SEARCH_ENCRYPTED_NODES..." value={searchQuery} onChange={e => setSearchQuery(e.target.value)} style={{ width: '100%', padding: '10px 12px 10px 42px', borderRadius: '100px', border: '1px solid var(--border)', background: 'rgba(0,0,0,0.2)', color: 'var(--text)', outline: 'none', fontSize: '12px', fontFamily: 'var(--mono)' }} />
            </div>
          </div>
          
          <div style={{ display: 'flex', gap: '1.5rem', alignItems: 'center' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text)' }}>ADMIN_SEC_OP</div>
                <div style={{ fontSize: '9px', fontFamily: 'var(--mono)', color: 'var(--accent)', background: 'rgba(0,245,212,0.05)', padding: '2px 8px', border: '1px solid var(--accent-glow)' }}>LEVEL 5 ACCESS</div>
              </div>
              <div style={{ width: '40px', height: '40px', background: 'var(--primary)', border: '1px solid var(--primary-glow)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 800, color: '#fff', fontFamily: 'var(--mono)', fontSize: '14px', clipPath: 'polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px)' }}>AD</div>
            </div>
          </div>
        </header>

        <AnimatePresence mode="wait">
          <motion.div key={activeTab} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -10 }} transition={{ duration: 0.3 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '2rem' }}>
              <h2 style={{ fontSize: '32px', fontFamily: 'var(--display)', letterSpacing: '0.04em', color: 'var(--text)', margin: 0 }}>{activeTab}</h2>
              <div style={{ height: '1px', flex: 1, background: 'linear-gradient(90deg, var(--border), transparent)' }}></div>
            </div>
            {renderContent()}
          </motion.div>
        </AnimatePresence>
      </main>
    </div>
  );
};

export default DashboardView;