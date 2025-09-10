#!/usr/bin/env python3
"""
Data Engineering Workflow with Authentication Integration

This example demonstrates how to integrate Supabase authentication
with a data engineering workflow.
"""

import json
import sys
import os
from typing import Dict, Any

# Import our authentication client
from auth_client import SupabaseAuthClient


class DataEngineeringWorkflow:
    """
    Example class showing how to integrate authentication
    with data engineering processes.
    """
    
    def __init__(self, config_file: str = 'auth_config.json'):
        """Initialize the workflow with authentication configuration."""
        self.config = self._load_config(config_file)
        self.auth_client = SupabaseAuthClient(
            base_url=self.config['supabase']['base_url'],
            api_key=self.config['supabase']['api_key']
        )
        
    def _load_config(self, config_file: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Configuration file '{config_file}' not found")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in configuration file: {e}")
            sys.exit(1)
    
    def setup_user_for_data_access(self, email: str, password: str) -> Dict[str, Any]:
        """
        Create a user account for data access.
        This would typically be part of onboarding process.
        """
        print(f"🔐 Setting up user for data access: {email}")
        
        result = self.auth_client.create_user(
            email=email,
            password=password,
            email_confirm=True
        )
        
        if result['success']:
            user_id = result['data']['id']
            print(f"✅ User created successfully with ID: {user_id}")
            
            # In a real workflow, you might:
            # 1. Grant database permissions
            # 2. Create user-specific schemas
            # 3. Set up data access policies
            # 4. Initialize user workspace
            
            return {
                'user_id': user_id,
                'email': email,
                'status': 'ready_for_data_access'
            }
        else:
            print(f"❌ Failed to create user: {result['error']}")
            return {
                'error': result['error'],
                'status': 'setup_failed'
            }
    
    def simulate_data_operations(self, user_id: str):
        """
        Simulate data engineering operations for an authenticated user.
        """
        print(f"📊 Simulating data operations for user: {user_id}")
        
        # In a real implementation, these would be actual database operations
        operations = [
            "Creating user-specific data schema",
            "Setting up sales analysis views",
            "Configuring automated reports",
            "Initializing data quality checks",
            "Setting up monitoring alerts"
        ]
        
        for i, operation in enumerate(operations, 1):
            print(f"  {i}. {operation}... ✅")
        
        print("📈 Data operations completed successfully!")
        
        # Return some mock results
        return {
            'schemas_created': 1,
            'views_configured': 5,  # As per the SQL in Final-project
            'procedures_setup': 1,  # Create_Rep_Sales_Store
            'events_scheduled': 1,  # Monthly data refresh
            'status': 'operational'
        }
    
    def demonstrate_workflow(self):
        """
        Demonstrate the complete workflow integration.
        """
        print("=== Data Engineering Workflow with Authentication ===")
        print("This demonstrates integration of user management with data processes.")
        print()
        
        # Use the default user from config for demonstration
        default_user = self.config['default_user']
        email = default_user['email']
        password = default_user['password']
        
        # Step 1: Set up user
        user_setup = self.setup_user_for_data_access(email, password)
        
        if user_setup.get('status') == 'ready_for_data_access':
            user_id = user_setup['user_id']
            
            # Step 2: Perform data operations
            print()
            data_results = self.simulate_data_operations(user_id)
            
            # Step 3: Summary
            print()
            print("=== Workflow Summary ===")
            print(f"User ID: {user_id}")
            print(f"Email: {email}")
            print(f"Schemas created: {data_results['schemas_created']}")
            print(f"Views configured: {data_results['views_configured']}")
            print(f"Procedures setup: {data_results['procedures_setup']}")
            print(f"Events scheduled: {data_results['events_scheduled']}")
            print(f"Status: {data_results['status']}")
            
            print()
            print("🎉 Workflow completed successfully!")
            
            # Step 4: Show connection to existing SQL work
            print()
            print("=== Connection to Northwind Analysis ===")
            print("The user is now ready to access:")
            print("- Sales analysis stored procedures (Create_Rep_Sales_Store)")
            print("- Business intelligence views (Europe_view, Germany_view, etc.)")
            print("- Automated monthly data refresh events")
            print("- Regional and performance categorization reports")
            
        else:
            print("💥 Workflow failed during user setup!")
            return False
        
        return True


def main():
    """Main function to run the demonstration."""
    try:
        workflow = DataEngineeringWorkflow()
        success = workflow.demonstrate_workflow()
        
        if success:
            print("\n📝 Note: This is a demonstration showing how authentication")
            print("   can be integrated with data engineering workflows.")
            print("   In production, you would connect this to actual databases")
            print("   and implement proper security measures.")
        
        return success
        
    except Exception as e:
        print(f"❌ Workflow failed with error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)