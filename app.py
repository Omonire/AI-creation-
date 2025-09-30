from flask import Flask

app = Flask(__name__)

HTML = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Omonire Oghene-Ovie Great — Portfolio & Resume</title>

  <style>
/* ---- your theme CSS (condensed, using original variables) ---- */
:root {
  --font-size: 16px;
  --background: #0b1220; /* slightly dark for contrast on this page */
  --foreground: #e6eef6;
  --card: #0f1724;
  --primary: #06b6d4;
  --primary-foreground: #010409;
  --accent: #7c3aed;
  --accent-foreground: #ffffff;
  --muted: #94a3b8;
  --radius: 0.75rem;
  --container-max: 1100px;
}

* { box-sizing: border-box; }
html,body { height: 100%; margin:0; font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background: var(--background); color: var(--foreground); font-size: var(--font-size); -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale; }
a { color: var(--primary); text-decoration: none; }
.container { max-width: var(--container-max); margin: 0 auto; padding: 2rem; }

/* Header / nav */
.header { position: fixed; top:0; left:0; right:0; z-index:60; backdrop-filter: blur(6px); background: rgba(5,10,20,0.5); border-bottom: 1px solid rgba(255,255,255,0.03); }
.header .inner { display:flex; align-items:center; justify-content:space-between; gap:1rem; max-width: var(--container-max); margin:0 auto; padding: 0.75rem 1rem; }
.logo { display:flex; align-items:center; gap:.6rem; color:var(--primary); font-weight:700; letter-spacing:0.6px; }
.logo .icon { width:36px; height:36px; border-radius:10px; background: linear-gradient(135deg,var(--primary),var(--accent)); display:inline-flex; align-items:center; justify-content:center; color:var(--primary-foreground); font-weight:800; }

/* hero */
.hero { min-height: 88vh; display:flex; align-items:center; justify-content:center; padding-top:4.5rem; }
.hero-inner { text-align:center; padding:2rem; }
.h-name { font-size:2.5rem; font-weight:800; margin:0 0 .5rem; background:linear-gradient(90deg,var(--primary),var(--accent)); -webkit-background-clip:text; background-clip:text; color:transparent; }
.h-sub { color:var(--muted); margin:0 0 1rem; font-size:1.05rem; }
.cta-row { display:flex; gap:1rem; justify-content:center; margin-top:1.25rem; flex-wrap:wrap; }
.btn { padding:.8rem 1.3rem; border-radius: .6rem; border: none; cursor:pointer; font-weight:600; }
.btn-primary { background: linear-gradient(90deg,var(--primary),var(--accent)); color:var(--primary-foreground); box-shadow: 0 8px 30px rgba(124,58,237,0.12); }
.btn-outline { background:transparent; color:var(--primary); border:1px solid rgba(255,255,255,0.06); }

/* sections */
.section { padding:4rem 0; }
.section .title { font-size:1.5rem; font-weight:700; color:var(--primary); margin-bottom:1rem; }
.card-grid { display:grid; gap:1.25rem; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); }
.card { background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius: var(--radius); padding:1.1rem; border:1px solid rgba(255,255,255,0.03); box-shadow: 0 6px 18px rgba(2,6,23,0.6); transform: translateY(32px); opacity:0; transition: transform 0.7s cubic-bezier(.2,.9,.2,1), opacity 0.7s ease; }
.card.visible { transform: translateY(0); opacity:1; }
.card h4 { margin:0 0 .5rem; color:var(--foreground); font-size:1.05rem; }
.card p, .card li { color: var(--muted); line-height:1.45; margin:0; }

/* resume layout specifics */
.resume-grid { display:grid; gap:1rem; grid-template-columns: 1fr; }
@media(min-width:900px){ .resume-grid { grid-template-columns: 2.2fr 1fr; } .hero-inner { padding:3rem 0; } .h-name { font-size:3rem; } }

/* lists & bullets */
ul.clean { list-style: disc inside; padding-left: 0; margin:0; }
.meta { color:var(--muted); font-size:0.95rem; margin-bottom:.6rem; }

/* projects larger heading */
.projects-h { text-align:center; font-size:1.25rem; margin-bottom:1rem; color:var(--primary); }

/* contact */
.contact form { display:flex; flex-direction:column; gap:.6rem; width:100%; max-width:520px; margin:0 auto; }
.input, textarea { padding:.8rem; border-radius:.6rem; border:1px solid rgba(255,255,255,0.04); background: rgba(255,255,255,0.02); color:var(--foreground); resize:vertical; }

/* footer */
footer { text-align:center; padding:2rem 0; color:var(--muted); border-top: 1px solid rgba(255,255,255,0.02); margin-top:2rem; }

/* small helpers */
.kv { font-weight:700; color:var(--foreground); }
.section-intro { color:var(--muted); margin-bottom:1.25rem; }

/* smooth scroll behavior (also set via JS) */
html { scroll-behavior:smooth; }
  </style>

<script>
document.addEventListener("DOMContentLoaded", () => {
  // smooth scroll from hero button
  const btn = document.getElementById("view-projects");
  if(btn) btn.addEventListener("click", (e)=>{
    e.preventDefault();
    document.getElementById("projects-section").scrollIntoView({behavior:"smooth", block:"start"});
  });

  // Intersection Observer with staggered reveal
  const revealTargets = document.querySelectorAll('.card');
  const observer = new IntersectionObserver((entries) => {
    // We will gather ones that entered and reveal them with a stagger
    const entering = [];
    entries.forEach(en => {
      if(en.isIntersecting) entering.push(en.target);
    });
    if(entering.length) {
      entering.forEach((el, idx) => {
        // stagger each by 80ms
        setTimeout(() => el.classList.add('visible'), idx * 80);
      });
    }
  }, { threshold: 0.18 });

  revealTargets.forEach(t => observer.observe(t));
});
</script>

</head>
<body>
  <!-- header -->
  <header class="header" role="banner">
    <div class="inner">
      <div class="logo">
        <div class="icon">⚔️</div>
        <div>
          <div style="font-size:0.95rem; opacity:0.9;">OMONIRE OGHENE-OVIE GREAT</div>
          <div style="font-size:0.78rem; color:var(--muted)">Cybersecurity • Python • Educator</div>
        </div>
      </div>
      <nav style="display:flex; gap:1rem; align-items:center;">
        <a href="#about">About</a>
        <a href="#experience">Experience</a>
        <a href="#education">Education</a>
        <a href="#certifications">Certifications</a>
        <a href="#skills">Skills</a>
        <a href="#projects-section">Projects</a>
        <a href="#contact">Contact</a>
      </nav>
    </div>
  </header>

  <main style="padding-top:5.2rem;">
    <!-- HERO -->
    <section class="hero">
      <div class="hero-inner container">
        <h1 class="h-name">OMONIRE OGHENE-OVIE GREAT</h1>
        <p class="h-sub">Benin City, Edo State, Nigeria • +2348122229591 • <a href="mailto:omonire4@gmail.com">omonire4@gmail.com</a></p>
        <p class="section-intro">Certified Ethical Hacker and Cyber Security Analyst — dynamic Python programmer and educator focused on practical security tooling and training.</p>
        <div class="cta-row">
          <button id="view-projects" class="btn btn-primary">🚀 View My Work</button>
          <a href="#contact"><button class="btn btn-outline">✉️ Contact</button></a>
        </div>
      </div>
    </section>

    <!-- ABOUT + RESUME SUMMARY -->
    <section id="about" class="section container" aria-labelledby="about-heading">
      <div>
        <div class="resume-grid">
          <div>
            <div class="title">Professional Summary</div>
            <p class="section-intro">Certified Ethical Hacker and Cyber Security Analyst. Dynamic Python programmer with a passion for data visualization and user training, honed at Uncle Israel Online Class. Expert in developing tailored training programs and enhancing technical content, with excellent communication skills. Committed to continuous improvement and achieving impactful results in software development and IT project coordination.</p>

            <div class="title">Experience</div>

            <div class="card">
              <h4>Tutor — Class gap (Online)</h4>
              <div class="meta">Nov 2024 – Present</div>
              <ul class="clean">
                <li class="p">Taught test-taking strategies and personalized learning plans.</li>
                <li class="p">Monitored student progress and provided regular feedback.</li>
                <li class="p">Conducted one-on-one tutoring and updated training materials.</li>
              </ul>
            </div>

            <div class="card">
              <h4>Python Programmer — Uncle Israel Online Class (Benin City)</h4>
              <div class="meta">Jun 2023 – Present</div>
              <ul class="clean">
                <li class="p">Delivered classroom training and created technical training content.</li>
                <li class="p">Developed lab exercises, presentations, and course materials.</li>
                <li class="p">Customized training programs and iterated on feedback.</li>
              </ul>
            </div>

          </div>

          <aside style="padding-left:1rem;">
            <div class="card">
              <div class="kv">Contact</div>
              <div class="meta">Benin City, Edo State, Nigeria</div>
              <div class="meta"><a href="mailto:omonire4@gmail.com">omonire4@gmail.com</a></div>
              <div class="meta">+2348122229591</div>
            </div>

            <div class="card">
              <div class="kv">Languages</div>
              <div>English — Proficient (C2)</div>
            </div>

            <div class="card">
              <div class="kv">Software / Tools</div>
              <ul class="clean">
                <li>Matplotlib • Pandas • Flask • Jupyter</li>
                <li>Nmap • Wireshark • TCPdump • Kali</li>
                <li>VS Code • PyCharm • Canvas • LMMS • FL Studio</li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- EDUCATION -->
    <section id="education" class="section container">
      <div class="title">Education</div>
      <div class="card-grid">
        <div class="card">
          <h4>B.Sc. Computer Science — University of Benin</h4>
          <div class="meta">Expected 2030</div>
        </div>
        <div class="card">
          <h4>Python Programming, Data Analysis, Web Development — Complete Computer & Tech</h4>
          <div class="meta">Feb 2025</div>
        </div>
      </div>
    </section>

    <!-- CERTIFICATIONS -->
    <section id="certifications" class="section container">
      <div class="title">Certifications</div>
      <div class="card-grid">
        <div class="card"><p>Certification in Cyber security — Cisco Network Academy (Feb 2025)</p></div>
        <div class="card"><p>Certificate in Ethical Hacking (C.E.H) — Cisco Network Academy (Mar 2025)</p></div>
        <div class="card"><p>CompTIA Cyber Security Analyst (CSA) — Complete Computer & Tech (Jul 2025)</p></div>
        <div class="card"><p>Endpoint Security — Cisco Networking Academy (May 2025)</p></div>
        <div class="card"><p>Python Essentials 1 & 2 — Cisco Networking Academy (May 2025)</p></div>
        <div class="card"><p>Network Security & Defense — Cisco Networking Academy (May 2025)</p></div>
        <div class="card"><p>Certificate in Cyber Threat Monitoring — Cisco Networking Academy (May 2025)</p></div>
      </div>
    </section>

    <!-- SKILLS -->
    <section id="skills" class="section container">
      <div class="title">Skills</div>
      <div class="card-grid">
        <div class="card"><p><strong>Technical:</strong> Python, Penetration Testing, Ethical Hacking, Malware Analysis, Data Encryption</p></div>
        <div class="card"><p><strong>Security:</strong> Vulnerability Analysis, DDoS Prevention, Network Protocols, IoT Security, Risk Assessment</p></div>
        <div class="card"><p><strong>Dev:</strong> Data Visualization, OOP, Mobile App Dev, Web App Security, DB Management</p></div>
        <div class="card"><p><strong>Tools/Libraries:</strong> Matplotlib, Pandas, Flask, Jupyter Notebooks, Git</p></div>
        <div class="card"><p><strong>OS:</strong> Windows & Linux</p></div>
        <div class="card"><p><strong>Soft:</strong> Communication, Analytical Thinking, Training & Instruction</p></div>
      </div>
    </section>

    <!-- PROJECTS -->
    <section id="projects-section" class="section container">
      <div class="projects-h">Selected Projects</div>
      <div class="card-grid">
        <div class="card">
          <h4>Zero-Trace Ethical Key Logger</h4>
          <p class="p">Python-based ethical key-logger used for authorized monitoring & training scenarios. (Responsible, authorized use only)</p>
        </div>
        <div class="card">
          <h4>Zero to Hero — Python Textbook</h4>
          <p class="p">Comprehensive textbook taking a learner from basics to advanced Python topics, including exercises and labs.</p>
        </div>
        <div class="card">
          <h4>Cyber Expert Security Tool-Box</h4>
          <p class="p">Toolkit featuring a Password Strength Checker and safe testing utilities for authorized security assessments.</p>
        </div>
        <div class="card">
          <h4>Ethical Brute Force Attacker (Research)</h4>
          <p class="p">A responsible, controlled research tool used to demonstrate login hardening; distributed with mitigations and disclaimers.</p>
        </div>
        <div class="card">
          <h4>Eagle OS</h4>
          <p class="p">Prototype OS emphasizing flexible UI and hardened security primitives (research-stage).</p>
        </div>
        <div class="card">
          <h4>Great AI</h4>
          <p class="p">AI experimental projects and POCs for automation and analytics.</p>
        </div>
      </div>
    </section>

    <!-- CONTACT -->
    <section id="contact" class="section container">
      <div class="title">Contact</div>
      <p class="section-intro">I'm open to opportunities and collaborations. Use the form below to open your email client and send me a message.</p>
      <div class="card" style="max-width:800px; margin:0 auto;">
        <form action="mailto:omonire4@gmail.com" method="get" enctype="text/plain">
          <label class="meta">Your name</label>
          <input class="input" type="text" name="name" placeholder="Your name" required />
          <label class="meta">Your email</label>
          <input class="input" type="email" name="email" placeholder="you@example.com" required />
          <label class="meta">Message</label>
          <textarea class="input" name="message" rows="6" placeholder="Hi — I want to talk about..." required></textarea>
          <div style="margin-top:1rem; text-align:right;">
            <button class="btn btn-primary" type="submit">Send Email</button>
          </div>
        </form>
      </div>
    </section>

    <footer>
      © 2025 Omonire Oghene-Ovie Great • Secured & Educating
    </footer>
  </main>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML

if __name__ == "__main__":
    app.run(debug=True)
