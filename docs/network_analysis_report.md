# Pravda Network Analysis - Network Infrastructure Report

## Overview
This document provides a comprehensive analysis of the Pravda network infrastructure based on active probing and OSINT data collection.

## Last Updated
2025-06-24 18:58:40 PDT

## 1. Network Infrastructure Analysis

### 1.1 Domain Structure
- **Primary Domain**: `pravda.com.ua`
- **Total Subdomains Analyzed**: 92
- **Total Network Nodes**: 139

### 1.2 Key Subdomains
| Subdomain | Purpose | Status |
|-----------|---------|--------|
| commento.pravda.com.ua | Commenting system | Active |
| dostup.pravda.com.ua | Mail server | Active |
| club.pravda.com.ua | Community/Forum | Active |
| kyiv.pravda.com.ua | Regional content | Active |
| pda.pravda.com.ua | Mobile interface | Active |
| shop.pravda.com.ua | E-commerce | Active |
| tabloid.pravda.com.ua | Tabloid content | Active |

### 1.3 Network Services
- **Email**: Google Workspace (Gmail)
- **CDN/Proxy**: Cloudflare
- **Hosting Providers**:
  - Cloudflare (Primary)
  - OVH
  - Hetzner
  - FREEHOST

## 2. Technical Analysis

### 2.1 IP Address Distribution
- **Primary IP Ranges**:
  - 172.67.0.0/16 (Cloudflare)
  - 193.178.144.0/22
  - 104.22.28.0/24 (Cloudflare)
  - 188.114.96.0/22 (Cloudflare)

### 2.2 DNS Configuration
- **Nameservers**:
  - tim.ns.cloudflare.com
  - elsa.ns.cloudflare.com
- **MX Records**:
  - aspmx.l.google.com
  - alt1.aspmx.l.google.com
  - alt2.aspmx.l.google.com
  - dostup.pravda.com.ua (custom mail server)

### 2.3 Security Measures
- **DDoS Protection**: Cloudflare
- **SSL/TLS**: Enabled across all services
- **Security Headers**:
  - Strict-Transport-Security
  - X-Content-Type-Options
  - X-Frame-Options
  - Content-Security-Policy

## 3. Key Findings

### 3.1 Infrastructure Patterns
1. **Cloudflare Integration**:
   - All major services are behind Cloudflare
   - Multiple Cloudflare IP ranges in use
   - DDoS protection and CDN capabilities

2. **Email Infrastructure**:
   - Primary email through Google Workspace
   - Custom mail server (dostup.pravda.com.au) for specific services

3. **Content Delivery**:
   - Global CDN through Cloudflare
   - Multiple edge locations
   - IPv6 support enabled

### 3.2 Notable Observations
- **Commenting System**: Custom implementation at commento.pravda.com.ua
- **Mobile Optimization**: Dedicated pda.pravda.com.ua subdomain
- **Regional Presence**: Multiple regional subdomains (kyiv.pravda.com.ua, etc.)
- **E-commerce**: Active shop.pravda.com.ua subdomain

## 4. Tools and Scripts

### 4.1 Analysis Scripts
1. **parse_probe_output.py**
   - Parses active probe data
   - Generates network relationship reports
   - Output: probe_analysis_report.txt

2. **build_seed_osint.sh**
   - Collects OSINT data for domains
   - Output: pravda_osint.csv

3. **analyze_osint.py**
   - Analyzes collected OSINT data
   - Generates statistical reports
   - Output: osint_analysis_report.txt

### 4.2 Generated Reports
1. **probe_analysis_report.txt**
   - Network relationships
   - Domain mappings
   - Infrastructure details

2. **osint_analysis_report.txt**
   - Domain statistics
   - SSL certificate information
   - WHOIS data analysis

## 5. Recommendations

### 5.1 Security
1. **Monitoring**:
   - Monitor for new subdomain creation
   - Track SSL certificate expirations
   - Watch for DNS changes

2. **Hardening**:
   - Review Cloudflare security settings
   - Implement WAF rules
   - Enable DNSSEC

### 5.2 Performance
1. **Optimization**:
   - Review CDN caching rules
   - Optimize image delivery
   - Implement HTTP/3

2. **Monitoring**:
   - Track response times
   - Monitor uptime
   - Analyze traffic patterns

## 6. Next Steps
1. **Deeper Analysis**:
   - Content analysis of subdomains
   - Traffic pattern analysis
   - Security vulnerability scanning

2. **Automation**:
   - Schedule regular scans
   - Implement change detection
   - Set up alerts for critical changes

3. **Documentation**:
   - Update network diagrams
   - Document all services
   - Create runbooks for common tasks

## 7. Appendices

### 7.1 IP Address Reference
| IP | Purpose | ASN |
|----|---------|-----|
| 172.67.15.15 | Cloudflare CDN | 13335 |
| 104.22.28.160 | Cloudflare CDN | 13335 |
| 193.178.147.250 | Web Hosting | 198610 |
| 188.114.98.228 | Cloudflare | 13335 |

### 7.2 Domain Reference
| Domain | Type | Purpose |
|--------|------|---------|
| commento.pravda.com.ua | Subdomain | Commenting system |
| dostup.pravda.com.ua | Subdomain | Mail server |
| club.pravda.com.ua | Subdomain | Community/Forum |
| kyiv.pravda.com.ua | Subdomain | Regional content |
