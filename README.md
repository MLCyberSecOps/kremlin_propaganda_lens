# Pravda Network Lens

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fmlcybersecops.github.io%2Fkremlin_propaganda_lens)](https://mlcybersecops.github.io/kremlin_propaganda_lens)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

An interactive visualization of the Pravda network infrastructure, providing insights into domain relationships, IP addresses, and network topology.

## 🌐 Live Website

Visit the interactive visualization at:  
https://mlcybersecops.github.io/kremlin_propaganda_lens

## 📊 Features

- Interactive network graph visualization
- Detailed domain and IP relationship mapping
- Responsive design for desktop and mobile
- Search and filter functionality
- Export options for analysis

## 🚀 Quick Start

### Viewing the Visualization

1. **Online**: Visit the [live website](https://mlcybersecops.github.io/kremlin_propaganda_lens)
2. **Locally**: Open `index.html` in any modern web browser

### Regenerating the Visualization

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the visualization script:
   ```bash
   python visualization/network_visualizer.py data/active_probe_output_1.csv -o visualization/pravda_network.html
   ```

## 📂 Project Structure

```
.
├── data/                           # Data files
│   └── active_probe_output_1.csv   # Raw probe data
├── docs/                           # Documentation
│   └── network_analysis_report.md  # Analysis report
├── visualization/                  # Visualization files
│   ├── network_visualizer.py       # Script to generate visualization
│   └── pravda_network.html         # Interactive network graph
├── index.html                      # Website homepage
├── 404.html                       # Custom 404 page
├── _config.yml                    # GitHub Pages config
├── .nojekyll                      # Disable Jekyll processing
└── README.md                      # This file
```

## 🔍 Data Description

The dataset includes:

- Domain relationships
- IP address mappings
- Network blocks and services
- Connection types and protocols

### Example Data Format

```
<source> (type) --> <relationship> --> <target> (type)
```

Example:
```
pravda.com.ua (FQDN) --> a_record --> 104.22.28.160 (IPAddress)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Project Link: [https://github.com/MLCyberSecOps/kremlin_propaganda_lens](https://github.com/MLCyberSecOps/kremlin_propaganda_lens)

## 🙏 Acknowledgments

- NetworkX for graph analysis
- PyVis for network visualization
- Bootstrap for responsive design
- GitHub Pages for hosting
