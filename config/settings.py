"""Configuration settings for DPD UK operations."""

import os
from dotenv import load_dotenv

load_dotenv()

# Application settings
APP_NAME = "DPD UK Operations"
APP_VERSION = "0.1.0"

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/dpd_operations"
)

# API settings
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "5000"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
