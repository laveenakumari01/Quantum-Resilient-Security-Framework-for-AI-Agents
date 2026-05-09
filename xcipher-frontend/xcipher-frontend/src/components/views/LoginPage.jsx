import { loginUser } from '../../api.js';
import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Shield, ArrowLeft, Mail, Lock, Eye, EyeOff, Globe, User } from 'lucide-react';
import './LoginPage.css';

const BASE_URL = "http://localhost:8000";

const LoginPage = ({ onBack, onLogin }) => {
  const [showPass, setShowPass] = useState(false);
  const [mode, setMode] = useState('login'); // 'login' or 'register'
  const [formData, setFormData] = useState({ email: '', password: '', fullName: '' });
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await loginUser(formData.email, formData.password);
      setLoading(false);
      onLogin();
    } catch (err) {
      setLoading(false);
      alert("Login failed: incorrect email or password");
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`${BASE_URL}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
          full_name: formData.fullName || formData.email.split("@")[0],
        }),
      });
      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || "Registration failed");
      }
      const data = await res.json();
      localStorage.setItem("token", data.access_token);
      sessionStorage.setItem("token", data.access_token);
      setLoading(false);
      onLogin();
    } catch (err) {
      setLoading(false);
      alert(err.message || "Registration failed");
    }
  };

  const handleEnterpriseLogin = async () => {
    setLoading(true);
    try {
      await loginUser("john.doe", "secret");
      setLoading(false);
      onLogin();
    } catch (err) {
      setLoading(false);
      alert("Enterprise login failed");
    }
  };

  return (
    <div className="login-view premium-theme">
      <div className="login-grid-bg"></div>
      <div className="login-scanner"></div>

      <button onClick={onBack} className="login-back-btn interactive">
        <ArrowLeft size={14} /> [ RETURN_TO_PROTOCOL ]
      </button>

      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="login-card"
      >
        <div className="login-logo-container">
          <Shield size={32} />
        </div>

        <div className="login-header">
          <h1>NODE <span className="text-glow">AUTH</span></h1>
          <p>{mode === 'login' ? 'Establish Quantum Handshake' : 'Register New Node'}</p>
        </div>

        {/* Toggle Login / Register */}
        <div style={{ display: 'flex', marginBottom: '2rem', border: '1px solid var(--border)', padding: '4px', gap: '4px' }}>
          <button
            type="button"
            onClick={() => setMode('login')}
            style={{
              flex: 1, padding: '8px', background: mode === 'login' ? 'var(--primary)' : 'transparent',
              color: mode === 'login' ? '#fff' : 'var(--text3)', border: 'none', cursor: 'pointer',
              fontFamily: 'var(--mono)', fontSize: '10px', letterSpacing: '0.1em', transition: 'all 0.3s'
            }}
          >
            LOGIN
          </button>
          <button
            type="button"
            onClick={() => setMode('register')}
            style={{
              flex: 1, padding: '8px', background: mode === 'register' ? 'var(--primary)' : 'transparent',
              color: mode === 'register' ? '#fff' : 'var(--text3)', border: 'none', cursor: 'pointer',
              fontFamily: 'var(--mono)', fontSize: '10px', letterSpacing: '0.1em', transition: 'all 0.3s'
            }}
          >
            REGISTER
          </button>
        </div>

        <AnimatePresence mode="wait">
          {mode === 'login' ? (
            <motion.form key="login" initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 10 }} onSubmit={handleSubmit}>
              <div className="login-field">
                <label>Email Address</label>
                <div className="login-input-wrapper">
                  <Mail className="login-input-icon" size={16} />
                  <input
                    type="text"
                    required
                    className="login-input"
                    placeholder="your@email.com"
                    value={formData.email}
                    onChange={e => setFormData({ ...formData, email: e.target.value })}
                  />
                </div>
              </div>

              <div className="login-field">
                <label>Password</label>
                <div className="login-input-wrapper">
                  <Lock className="login-input-icon" size={16} />
                  <input
                    type={showPass ? 'text' : 'password'}
                    required
                    className="login-input"
                    placeholder="••••••••••••••••"
                    value={formData.password}
                    onChange={e => setFormData({ ...formData, password: e.target.value })}
                  />
                  <button type="button" onClick={() => setShowPass(!showPass)}
                    style={{ position: 'absolute', right: '14px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text3)' }}>
                    {showPass ? <EyeOff size={16} /> : <Eye size={16} />}
                  </button>
                </div>
              </div>

              <button type="submit" className="login-submit-btn" disabled={loading}>
                {loading ? 'AUTHENTICATING...' : 'AUTHENTICATE NODE'}
              </button>

              <div style={{ display: 'flex', alignItems: 'center', gap: '15px', margin: '2rem 0' }}>
                <div style={{ flex: 1, height: '1px', background: 'var(--border)' }}></div>
                <span style={{ fontSize: '9px', fontFamily: 'var(--mono)', color: 'var(--text3)', letterSpacing: '0.1em' }}>FEDERATED_CORE</span>
                <div style={{ flex: 1, height: '1px', background: 'var(--border)' }}></div>
              </div>

              <button type="button" onClick={handleEnterpriseLogin} className="interactive"
                style={{ width: '100%', padding: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px', background: 'transparent', border: '1px solid var(--border)', color: 'var(--text2)', fontFamily: 'var(--mono)', fontSize: '11px', cursor: 'pointer', transition: 'all 0.3s' }}>
                <Globe size={14} /> ENTER VIA ENTERPRISE_SSO
              </button>
            </motion.form>
          ) : (
            <motion.form key="register" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: -10 }} onSubmit={handleRegister}>
              <div className="login-field">
                <label>Full Name (optional)</label>
                <div className="login-input-wrapper">
                  <User className="login-input-icon" size={16} />
                  <input
                    type="text"
                    className="login-input"
                    placeholder="Your Name"
                    value={formData.fullName}
                    onChange={e => setFormData({ ...formData, fullName: e.target.value })}
                  />
                </div>
              </div>

              <div className="login-field">
                <label>Email Address</label>
                <div className="login-input-wrapper">
                  <Mail className="login-input-icon" size={16} />
                  <input
                    type="text"
                    required
                    className="login-input"
                    placeholder="your@email.com"
                    value={formData.email}
                    onChange={e => setFormData({ ...formData, email: e.target.value })}
                  />
                </div>
              </div>

              <div className="login-field">
                <label>Password</label>
                <div className="login-input-wrapper">
                  <Lock className="login-input-icon" size={16} />
                  <input
                    type={showPass ? 'text' : 'password'}
                    required
                    className="login-input"
                    placeholder="••••••••••••••••"
                    value={formData.password}
                    onChange={e => setFormData({ ...formData, password: e.target.value })}
                  />
                  <button type="button" onClick={() => setShowPass(!showPass)}
                    style={{ position: 'absolute', right: '14px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text3)' }}>
                    {showPass ? <EyeOff size={16} /> : <Eye size={16} />}
                  </button>
                </div>
              </div>

              <button type="submit" className="login-submit-btn" disabled={loading}>
                {loading ? 'REGISTERING...' : 'REGISTER NODE'}
              </button>
            </motion.form>
          )}
        </AnimatePresence>

        <div style={{ marginTop: '2rem', textAlign: 'center', fontSize: '10px', color: 'var(--text3)', fontFamily: 'var(--mono)' }}>
          SECURE_NODE_V4.2 // PQC_ENABLED
        </div>
      </motion.div>
    </div>
  );
};

export default LoginPage;