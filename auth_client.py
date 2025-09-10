#!/usr/bin/env python3
"""
Supabase Authentication Client
Equivalent to the PowerShell command for user creation in Supabase.

This script provides functionality to create users in a Supabase authentication system
running locally on port 8000.
"""

import json
import requests
from typing import Dict, Any, Optional


class SupabaseAuthClient:
    """Client for interacting with Supabase authentication API."""
    
    def __init__(self, base_url: str = "http://localhost:8000", api_key: str = None):
        """
        Initialize the Supabase authentication client.
        
        Args:
            base_url: The base URL of the Supabase instance
            api_key: The API key for authentication
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q"
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "apikey": self.api_key,
            "Content-Type": "application/json"
        }
    
    def create_user(self, email: str, password: str, email_confirm: bool = True) -> Dict[str, Any]:
        """
        Create a new user in the Supabase authentication system.
        
        This is equivalent to the PowerShell command:
        Invoke-WebRequest -Uri "http://localhost:8000/auth/v1/admin/users" -Method Post -Headers $headers -Body $body
        
        Args:
            email: User's email address
            password: User's password
            email_confirm: Whether to automatically confirm the email
            
        Returns:
            Dict containing the API response
            
        Raises:
            requests.RequestException: If the API request fails
        """
        url = f"{self.base_url}/auth/v1/admin/users"
        
        payload = {
            "email": email,
            "password": password,
            "email_confirm": email_confirm
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                data=json.dumps(payload),
                timeout=30
            )
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            return {
                "status_code": response.status_code,
                "data": response.json(),
                "success": True
            }
            
        except requests.RequestException as e:
            return {
                "status_code": getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None,
                "error": str(e),
                "success": False
            }
    
    def get_user_info(self, user_id: str) -> Dict[str, Any]:
        """
        Get information about a specific user.
        
        Args:
            user_id: The ID of the user to retrieve
            
        Returns:
            Dict containing the user information
        """
        url = f"{self.base_url}/auth/v1/admin/users/{user_id}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            return {
                "status_code": response.status_code,
                "data": response.json(),
                "success": True
            }
            
        except requests.RequestException as e:
            return {
                "status_code": getattr(e.response, 'status_code', None) if hasattr(e, 'response') else None,
                "error": str(e),
                "success": False
            }


def main():
    """
    Example usage of the SupabaseAuthClient.
    Replicates the functionality shown in the PowerShell command.
    """
    # Initialize the client
    client = SupabaseAuthClient()
    
    # Create a user (equivalent to the PowerShell example)
    print("Creating user with email: rotben3@gmail.com")
    result = client.create_user(
        email="rotben3@gmail.com",
        password="tadam1234",
        email_confirm=True
    )
    
    if result["success"]:
        print(f"✅ User created successfully!")
        print(f"Status Code: {result['status_code']}")
        print(f"User ID: {result['data'].get('id', 'N/A')}")
        print(f"Email: {result['data'].get('email', 'N/A')}")
        print(f"Email Confirmed At: {result['data'].get('email_confirmed_at', 'N/A')}")
        
        # Example of getting user info
        user_id = result['data'].get('id')
        if user_id:
            print(f"\nFetching user info for ID: {user_id}")
            user_info = client.get_user_info(user_id)
            if user_info["success"]:
                print(f"✅ User info retrieved successfully!")
            else:
                print(f"❌ Failed to get user info: {user_info['error']}")
    else:
        print(f"❌ Failed to create user: {result['error']}")
        if result.get('status_code'):
            print(f"Status Code: {result['status_code']}")


if __name__ == "__main__":
    main()