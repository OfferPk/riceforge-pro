\# RiceForge Pro (v1.0.0)  
\#\#\# CCSDS 121.0-B-3 & ISO 15887 Spacecraft Lossless Data Compression Studio & Adaptive Rice Coding Engine

RiceForge Pro is an aerospace-grade developer studio, adaptive Rice coding engine, predictive differencing preprocessor, split-sample block optimizer (\$J=16\$), and 10-point normative compliance auditor designed for spacecraft science instruments, star trackers, magnetometers, and satellite telemetry streams.

\---

\#\# 🌟 Key Capabilities  
\- \*\*Official CCSDS Rice Algorithm\*\*: Implements full CCSDS 121.0-B-3 and ISO 15887 specifications with adaptive split-sample entropy coding.  
\- \*\*Bijective Difference Preprocessor\*\*: Reversible mapping of signed sample differences into compact non-negative integer deltas.  
\- \*\*Adaptive Block Optimization (\$J=16\$)\*\*: Dynamically evaluates split-sample options (\$k \= 0..14\$), zero-block codes, second-extension pairs, and uncompressed fallback to select the minimum bitlength per 16-sample block.  
\- \*\*Exact Lossless Reconstruction\*\*: Bit-by-bit identical inverse decoding with mathematical proof of zero distortion (\$	ext{RMSE} \= 0.000\$, \$	ext{PSNR} \= \\infty\$).  
\- \*\*Telemetry Downlink Bandwidth Savings\*\*: Achieves \$2:1\$ to \$4:1\$ lossless telemetry reduction with ultra-low computational complexity suitable for flight microprocessors (LEON, ARM, RAD750).  
\- \*\*10-Point Normative Auditor\*\*: Automated verification engine enforcing rules \`LDC-001\` through \`LDC-010\` per official CCSDS Blue Book standards.

\---

\#\# 📂 Project Structure  
\`\`\`text  
rice-forge-pro/  
├── source-code/  
│   ├── rice-engine.js           \# Core Rice algorithm, difference mapper & optimizer  
│   ├── rice-auditor.js          \# 10-point normative compliance auditor  
│   ├── rice\_cli.py              \# Python 3 CLI executable  
│   ├── rice-cli.py              \# Python 3 CLI alias  
│   ├── test\_runner.py           \# 10-suite unit test runner  
│   └── index.html               \# Interactive Mission Control operations console  
├── build/  
│   └── rice-forge-pro-v1.0.0.zip \# Standalone production bundle  
├── documentation/  
│   ├── CCSDS\_RICE\_SPECIFICATION.md \# Normative protocol specification  
│   └── RICE\_COMPLIANCE\_MATRIX.md   \# 10-point requirement traceability  
└── screenshots/  
    ├── architecture-diagram.svg    \# System architecture diagram  
    └── rice-studio-preview.svg     \# Operations studio interface preview  
\`\`\`

\---

\#\# 🚀 Quick Start

\#\#\# Running Automated Tests  
\`\`\`bash  
python3 source-code/test\_runner.py \-v  
\`\`\`

\#\#\# Command Line Interface  
\`\`\`bash  
\# Compress magnetometer telemetry signal  
python3 source-code/rice\_cli.py \--mode compress \--signal magnetometer \--length 64

\# Compress thermal housekeeping telemetry signal  
python3 source-code/rice\_cli.py \--mode compress \--signal thermal \--length 128

\# Run 10-Point Normative Compliance Audit  
python3 source-code/rice\_cli.py \--mode audit  
\`\`\`

\#\#\# Launching the Web Operations Console  
Open \`source-code/index.html\` in any modern web browser to access live telemetry signal generation, block-by-block split-sample option visualization, waveform plotting, and compliance auditing.  
