# Data-Engineering-1

## Project Overview

This repository contains a data engineering project focusing on:
1. **Database Analysis**: SQL-based analysis of the Northwind database with star schema implementation
2. **Authentication Integration**: Supabase authentication system integration for user management

## Authentication System

### Overview
The project includes integration with a Supabase authentication system running locally on port 8000. This allows for user creation and management as part of the data engineering workflow.

### Files
- `auth_client.py` - Python client for Supabase authentication
- `auth_client.ps1` - PowerShell script for Windows users
- `auth_config.json` - Configuration file for authentication settings
- `requirements.txt` - Python dependencies

### Usage

#### Python Client
```bash
# Install dependencies
pip install -r requirements.txt

# Run the authentication client
python auth_client.py
```

#### PowerShell Script (Windows)
```powershell
# Create a user
.\auth_client.ps1 -Email "user@example.com" -Password "password123"

# Create a user with custom settings
.\auth_client.ps1 -BaseUrl "http://localhost:8000" -Email "user@example.com" -Password "password123" -EmailConfirm $true
```

#### Manual PowerShell Commands
The original working PowerShell commands (as shown in the issue):
```powershell
$headers = @{
    "Authorization" = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q"
    "apikey"        = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q"
    "Content-Type"  = "application/json"
}

$body = '{"email":"rotben3@gmail.com","password":"tadam1234","email_confirm":true}'

Invoke-WebRequest -Uri "http://localhost:8000/auth/v1/admin/users" -Method Post -Headers $headers -Body $body
```

### Configuration
Edit `auth_config.json` to customize:
- Base URL for the Supabase instance
- API key for authentication
- Default user settings

## Database Analysis (Northwind)

The project includes comprehensive SQL analysis of the Northwind database with:
- Star schema implementation
- Stored procedures for sales analysis
- Automated data refresh events
- Business intelligence views
- Regional and performance categorization

See the `Final-project` file for detailed SQL implementation.