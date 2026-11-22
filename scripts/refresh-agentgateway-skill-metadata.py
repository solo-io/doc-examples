#!/usr/bin/env python3
"""Compatibility entry point for the customer skill metadata checker."""

from pathlib import Path
import runpy


runpy.run_path(str(Path(__file__).with_name("refresh-skill-metadata.py")), run_name="__main__")
