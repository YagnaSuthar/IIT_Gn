#!/usr/bin/env python3
"""
Heroku startup script for FarmXpert
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

def main():
    """Start the application with Gunicorn for Heroku"""
    port = int(os.environ.get('PORT', 8000))
    
    # Import after adding to path
    try:
        from farmxpert.interfaces.api.main import app
    except ImportError as e:
        print(f"Error importing app: {e}")
        sys.exit(1)
    
    # Start with gunicorn
    import subprocess
    cmd = [
        'gunicorn',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '3',
        '--timeout', '120',
        '--keep-alive', '5',
        '--max-requests', '1000',
        '--max-requests-jitter', '100',
        'farmxpert.interfaces.api.main:app'
    ]
    
    print(f"Starting FarmXpert on port {port}...")
    subprocess.run(cmd)

if __name__ == '__main__':
    main()
