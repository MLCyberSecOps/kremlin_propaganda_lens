# Pravda Network Analysis Data

This directory contains the data and visualizations for the Pravda network infrastructure analysis.

## Directory Structure

```
pravda_network_data/
├── data/                    # Raw and processed data files
│   └── active_probe_output_1.csv  # Raw probe data
├── docs/                    # Documentation
│   └── network_analysis_report.md  # Analysis report
└── visualization/           # Network visualizations
    └── pravda_network.html  # Interactive network visualization
```

## Data Description

### `data/active_probe_output_1.csv`
This file contains the raw output from active network probing of the Pravda network infrastructure.

**Format:**
```
<source> (type) --> <relationship> --> <target> (type)
```

**Example:**
```
pravda.com.ua (FQDN) --> a_record --> 104.22.28.160 (IPAddress)
```

## Visualization

The interactive network visualization is available in the `visualization` directory:
- `pravda_network.html`: Interactive network graph showing relationships between domains, IPs, and services

To view the visualization:
1. Open `visualization/pravda_network.html` in a web browser
2. Use your mouse to zoom, pan, and interact with the network

## How to Recreate

1. Install dependencies:
   ```bash
   pip install networkx pyvis pandas
   ```

2. Run the visualization script:
   ```bash
   python visualization/network_visualizer.py data/active_probe_output_1.csv -o visualization/network.html
   ```

## Analysis Report

See `docs/network_analysis_report.md` for a detailed analysis of the network infrastructure.

## License

[Specify your license here]

## Contact

For questions about this data, please contact [Your Contact Information]
