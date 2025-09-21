# Firewall-Rule-Analyzer
Lightweight Python-based firewall rule analyzer for detecting open ports, insecure IP ranges, and misconfigured access controls

# 🔥 Firewall Rule Analyzer

A Python tool to audit firewall rules (iptables/ufw) and flag risky configurations.

## 🚀 Features
- Parses firewall rule files
- Detects open ports and IP ranges
- Flags insecure rules (e.g., open SSH to 0.0.0.0/0)
- Suggests safer alternatives

## 🛠️ Requirements
- Python 3.x

## 📦 Usage
```bash
python analyzer.py

git clone https://github.com/devsetpal9-png/Firewall-Rule-Analyzer
