\# CCSDS 121.0-B-3 & ISO 15887 Spacecraft Lossless Data Compression Specification

\#\# 1\. Scope & Space Flight History  
The \*\*Consultative Committee for Space Data Systems (CCSDS)\*\* Recommendation \*\*CCSDS 121.0-B-3\*\* (and international standard \*\*ISO 15887\*\*) establishes the mathematical specification for \*\*Lossless Data Compression\*\*, commonly referred to as the \*\*Rice Algorithm\*\*.

Conceived by Robert F. Rice at NASA JPL, this algorithm has flown on scores of historic and active deep-space and Earth observation missions (including NASA Voyager, Galileo, Cassini, Mars Pathfinder, Curiosity, Perseverance, New Horizons, and JWST).

\---

\#\# 2\. Functional Architecture  
The compressor operates on sequences of digital data samples (from science instruments, attitude sensors, or engineering telemetry) and comprises two sequential stages:  
1\. \*\*Adaptive Preprocessor\*\*:  
   \- Takes input samples \$s\_i\$ with resolution \$n\$ bits (\$4 \\le n \\le 32\$).  
   \- Calculates predictive unit differences \$\\Delta\_i \= s\_i \- s\_{i-1}\$.  
   \- Applies a reversible non-negative integer mapping producing \$\\delta\_i \\in \[0, 2^n \- 1\]\$.  
2\. \*\*Adaptive Entropy Coder\*\*:  
   \- Partitions samples into blocks of length \$J=16\$.  
   \- Evaluates split-sample coding options (\$k \= 0, 1, 2, \\dots, n-2\$), the zero-block option, the second-extension option, and the uncompressed fallback.  
   \- Dynamically selects the option \$k^\*\$ producing the minimum bitlength for that block.  
   \- Emits a compact option identifier followed by split-sample code bits.

\---

\#\# 3\. Normative Bitstream Framing  
\- \*\*Reference Sample\*\*: \$s\_0\$ is transmitted uncompressed (or pre-shared).  
\- \*\*Block Formatting\*\*: Each block of \$J=16\$ samples begins with an option selection code (typically 4 bits) followed by the concatenated coded bits.  
\- \*\*Octet Alignment\*\*: Output bitstreams are packed into standard 8-bit octets for transmission across space data links.  
