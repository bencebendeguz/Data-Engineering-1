# Supabase Authentication PowerShell Script
# Equivalent to the manual PowerShell commands shown in the issue

param(
    [Parameter(Mandatory=$false)]
    [string]$BaseUrl = "http://localhost:8000",
    
    [Parameter(Mandatory=$false)]
    [string]$ApiKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q",
    
    [Parameter(Mandatory=$true)]
    [string]$Email,
    
    [Parameter(Mandatory=$true)]
    [string]$Password,
    
    [Parameter(Mandatory=$false)]
    [bool]$EmailConfirm = $true
)

function New-SupabaseUser {
    param(
        [string]$BaseUrl,
        [string]$ApiKey,
        [string]$Email,
        [string]$Password,
        [bool]$EmailConfirm
    )
    
    # Setup headers exactly as shown in the working example
    $headers = @{
        "Authorization" = "Bearer $ApiKey"
        "apikey"        = $ApiKey
        "Content-Type"  = "application/json"
    }
    
    # Setup body exactly as shown in the working example
    $body = @{
        email = $Email
        password = $Password
        email_confirm = $EmailConfirm
    } | ConvertTo-Json
    
    # Construct the URL
    $uri = "$BaseUrl/auth/v1/admin/users"
    
    try {
        Write-Host "Creating user with email: $Email" -ForegroundColor Yellow
        Write-Host "Using endpoint: $uri" -ForegroundColor Gray
        
        # Make the request
        $response = Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $body
        
        # Parse the response
        $responseData = $response.Content | ConvertFrom-Json
        
        # Display results
        Write-Host "✅ User created successfully!" -ForegroundColor Green
        Write-Host "Status Code: $($response.StatusCode)" -ForegroundColor Green
        Write-Host "User ID: $($responseData.id)" -ForegroundColor Cyan
        Write-Host "Email: $($responseData.email)" -ForegroundColor Cyan
        Write-Host "Email Confirmed At: $($responseData.email_confirmed_at)" -ForegroundColor Cyan
        Write-Host "Role: $($responseData.role)" -ForegroundColor Cyan
        
        return @{
            Success = $true
            StatusCode = $response.StatusCode
            Data = $responseData
            RawResponse = $response
        }
    }
    catch {
        Write-Host "❌ Failed to create user!" -ForegroundColor Red
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        
        if ($_.Exception.Response) {
            Write-Host "Status Code: $($_.Exception.Response.StatusCode.value__)" -ForegroundColor Red
        }
        
        return @{
            Success = $false
            Error = $_.Exception.Message
            StatusCode = $_.Exception.Response.StatusCode.value__
        }
    }
}

function Get-SupabaseUser {
    param(
        [string]$BaseUrl,
        [string]$ApiKey,
        [string]$UserId
    )
    
    $headers = @{
        "Authorization" = "Bearer $ApiKey"
        "apikey"        = $ApiKey
        "Content-Type"  = "application/json"
    }
    
    $uri = "$BaseUrl/auth/v1/admin/users/$UserId"
    
    try {
        Write-Host "Fetching user info for ID: $UserId" -ForegroundColor Yellow
        
        $response = Invoke-WebRequest -Uri $uri -Method Get -Headers $headers
        $responseData = $response.Content | ConvertFrom-Json
        
        Write-Host "✅ User info retrieved successfully!" -ForegroundColor Green
        Write-Host "User Data:" -ForegroundColor Cyan
        $responseData | Format-List
        
        return @{
            Success = $true
            StatusCode = $response.StatusCode
            Data = $responseData
        }
    }
    catch {
        Write-Host "❌ Failed to get user info!" -ForegroundColor Red
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        
        return @{
            Success = $false
            Error = $_.Exception.Message
        }
    }
}

# Main execution
Write-Host "=== Supabase Authentication Script ===" -ForegroundColor Magenta
Write-Host "This script replicates the PowerShell commands from the issue." -ForegroundColor Gray
Write-Host ""

# Create the user
$result = New-SupabaseUser -BaseUrl $BaseUrl -ApiKey $ApiKey -Email $Email -Password $Password -EmailConfirm $EmailConfirm

if ($result.Success -and $result.Data.id) {
    Write-Host ""
    Write-Host "Would you like to fetch the user info? (y/n): " -NoNewline -ForegroundColor Yellow
    $choice = Read-Host
    
    if ($choice -eq 'y' -or $choice -eq 'Y') {
        Get-SupabaseUser -BaseUrl $BaseUrl -ApiKey $ApiKey -UserId $result.Data.id
    }
}

Write-Host ""
Write-Host "Script completed." -ForegroundColor Magenta