#!/usr/bin/env python3
"""
Process REW measurements and calculate ANC/Transparency as reduction from ENV baseline.
Shows actual dB reduction/passthrough instead of raw SPL.
"""

import sys
from pathlib import Path
import math

def parse_rew_file(filepath):
    """Parse a REW measurement file and extract frequency/SPL data."""
    data = []
    in_data_section = False
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            
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

def logarithmic_sample(data, target_points=100):
    """Sample data logarithmically."""
    if len(data) <= target_points or not data:
        return data
    
    sampled = []
    min_freq = data[0]['x']
    max_freq = data[-1]['x']
    
    log_min = math.log10(min_freq)
    log_max = math.log10(max_freq)
    
    for i in range(target_points):
        log_freq = log_min + (log_max - log_min) * i / (target_points - 1)
        target_freq = 10 ** log_freq
        
        closest = min(data, key=lambda p: abs(p['x'] - target_freq))
        if closest not in sampled:
            sampled.append(closest)
    
    return sorted(sampled, key=lambda p: p['x'])

def calculate_reduction(env_data, measured_data):
    """Calculate dB reduction from ENV baseline."""
    # Create frequency->SPL lookup for ENV
    env_lookup = {p['x']: p['y'] for p in env_data}
    
    reduction = []
    for point in measured_data:
        freq = point['x']
        measured_spl = point['y']
        
        # Find closest ENV frequency
        closest_env_freq = min(env_lookup.keys(), key=lambda f: abs(f - freq))
        env_spl = env_lookup[closest_env_freq]
        
        # Calculate reduction (negative = noise reduced, positive = amplified)
        reduction_db = measured_spl - env_spl
        
        reduction.append({'x': freq, 'y': reduction_db})
    
    return reduction

def format_as_js(data, indent=4):
    """Format data as JavaScript array."""
    spaces = ' ' * indent
    lines = [f"{spaces}{{x: {d['x']:.1f}, y: {d['y']:.2f}}}" for d in data]
    return '[\n' + ',\n'.join(lines) + '\n' + ' ' * (indent-4) + ']'

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process-measurements-reduction.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"Directory not found: {directory}")
        sys.exit(1)
    
    files = list(directory.glob('*.txt'))
    
    # Find and process ENV file
    env_file = None
    for f in files:
        if f.stem.lower() == 'env':
            env_file = f
            break
    
    if not env_file:
        print("Error: ENV.txt file not found!")
        sys.exit(1)
    
    env_data = parse_rew_file(env_file)
    env_data = logarithmic_sample(env_data, 100)
    
    print("// ANC/Transparency data as dB reduction from ENV baseline")
    print("const measurements = {")
    
    # Process ANC files
    anc_files = [f for f in files if 'ANC' in f.stem and f != env_file]
    if anc_files:
        print("    anc: {")
        for i, f in enumerate(anc_files):
            name = f.stem.replace('_ANC', '').replace('_', ' ')
            data = parse_rew_file(f)
            data = logarithmic_sample(data, 100)
            reduction = calculate_reduction(env_data, data)
            comma = ',' if i < len(anc_files) - 1 else ''
            print(f"        '{name}': {format_as_js(reduction, 12)}{comma}")
        print("    },")
        print()
    
    # Process Transparency files
    trans_files = [f for f in files if 'Transparency' in f.stem]
    if trans_files:
        print("    transparency: {")
        for i, f in enumerate(trans_files):
            name = f.stem.replace('_Transparency', '').replace('_', ' ')
            data = parse_rew_file(f)
            data = logarithmic_sample(data, 100)
            reduction = calculate_reduction(env_data, data)
            comma = ',' if i < len(trans_files) - 1 else ''
            print(f"        '{name}': {format_as_js(reduction, 12)}{comma}")
        print("    }")
    
    print("};")

if __name__ == '__main__':
    main()
