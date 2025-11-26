#!/usr/bin/env python3
"""
Process REW measurement files into JavaScript format for the ANC comparison tool.
Usage: python3 process-measurements.py <directory_with_txt_files>
"""

import sys
import re
from pathlib import Path

def parse_rew_file(filepath):
    """Parse a REW measurement file and extract frequency/SPL data."""
    data = []
    in_data_section = False
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Start reading data after the header line
            if line.startswith('* Freq(Hz)'):
                in_data_section = True
                continue
            
            if in_data_section and line and not line.startswith('*'):
                parts = line.split('\t')
                if len(parts) >= 2:
                    try:
                        freq = float(parts[0])
                        spl = float(parts[1])
                        data.append({'x': freq, 'y': spl})
                    except ValueError:
                        continue
    
    return data

def format_as_js(data, indent=4):
    """Format data as JavaScript array."""
    spaces = ' ' * indent
    lines = [f"{spaces}{{x: {d['x']}, y: {d['y']:.3f}}}" for d in data]
    return '[\n' + ',\n'.join(lines) + '\n' + ' ' * (indent-4) + ']'

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process-measurements.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"Directory not found: {directory}")
        sys.exit(1)
    
    # Process all .txt files
    files = list(directory.glob('*.txt'))
    
    print("// Generated measurement data")
    print("const measurements = {")
    
    # Find and process ENV file
    env_file = None
    for f in files:
        if f.stem.lower() == 'env':
            env_file = f
            break
    
    if env_file:
        data = parse_rew_file(env_file)
        print(f"    env: {format_as_js(data, 8)},")
        print()
    
    # Process ANC files
    anc_files = [f for f in files if 'ANC' in f.stem and f != env_file]
    if anc_files:
        print("    anc: {")
        for i, f in enumerate(anc_files):
            # Extract product name
            name = f.stem.replace('_ANC', '').replace('_', ' ')
            data = parse_rew_file(f)
            comma = ',' if i < len(anc_files) - 1 else ''
            print(f"        '{name}': {format_as_js(data, 12)}{comma}")
        print("    },")
        print()
    
    # Process Transparency files
    trans_files = [f for f in files if 'Transparency' in f.stem or 'Trans' in f.stem]
    if trans_files:
        print("    transparency: {")
        for i, f in enumerate(trans_files):
            name = f.stem.replace('_Transparency', '').replace('_Trans', '').replace('_', ' ')
            data = parse_rew_file(f)
            comma = ',' if i < len(trans_files) - 1 else ''
            print(f"        '{name}': {format_as_js(data, 12)}{comma}")
        print("    }")
    
    print("};")

if __name__ == '__main__':
    main()
