import React from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, BookOpen, Search, Filter, Shield, Activity, Zap, Clock } from 'lucide-react';
import './BlogView.css';
import blogBanner from '../../assets/blog_banner_1777821944062.png';

const BlogView = ({ onBack }) => {
  const posts = [
    {
      title: 'Post-Quantum Handshake Dynamics',
      tag: 'Research',
      date: 'MAY 02, 2026',
      read: '12 min',
      excerpt: 'Analyzing the entropy levels of XCIPHER CRYSTALS-Kyber implementation across distributed AI nodes in high-latency environments.',
      img: blogBanner
    },
    {
      title: 'Neural Anomaly Detection in Mesh Networks',
      tag: 'Intelligence',
      date: 'APR 28, 2026',
      read: '8 min',
      excerpt: 'How XCIPHER agents utilize federated learning to identify zero-day threat vectors without compromising local memory integrity.',
      img: 'https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1000&auto=format&fit=crop'
    },
    {
      title: 'The Sovereign Agent Identity Protocol',
      tag: 'Security',
      date: 'APR 15, 2026',
      read: '15 min',
      excerpt: 'Redefining RBAC for autonomous systems: A deep dive into XCIPHER hardware-bound identity verification modules.',
      img: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1000&auto=format&fit=crop'
    }
  ];

  return (
    <div className="blog-view premium-theme">
      <aside className="blog-sidebar">
        <div className="docs-nav-group">
          <span className="docs-nav-label">Intelligence Categories</span>
          <div className="docs-nav-link active"><Shield size={14} /> Threat Reports</div>
          <div className="docs-nav-link"><Activity size={14} /> System Research</div>
          <div className="docs-nav-link"><Zap size={14} /> Tech Briefs</div>
        </div>

        <div className="docs-nav-group" style={{ marginTop: 'auto' }}>
          <div className="docs-nav-link" onClick={onBack}>
            <ArrowLeft size={14} /> Return to Grid
          </div>
        </div>
      </aside>

      <main className="blog-content">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
          <header className="blog-header">
            <span className="blog-meta" style={{ color: 'var(--accent)' }}>[ SECURE_INTEL_FEED ]</span>
            <h1>Intelligence Briefings</h1>
          </header>

          <div className="blog-grid">
            {posts.map((post, i) => (
              <div key={i} className="blog-card">
                <div className="blog-img" style={{ backgroundImage: `url(${post.img})` }}>
                  <div className="blog-meta" style={{ position: 'absolute', bottom: '1rem', left: '1rem', zIndex: 5, color: '#fff' }}>
                    {post.tag} // {post.date}
                  </div>
                </div>
                <div className="blog-info">
                  <div className="blog-title">{post.title}</div>
                  <p className="blog-excerpt">{post.excerpt}</p>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span className="blog-tag">{post.read} READ</span>
                    <span style={{ color: 'var(--primary)', fontSize: '11px', fontFamily: 'var(--mono)', fontWeight: 600 }}>
                      ACCESS DOSSIER <ArrowLeft size={10} style={{ transform: 'rotate(180deg)' }} />
                    </span>
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

export default BlogView;
