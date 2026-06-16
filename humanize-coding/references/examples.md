# Before / After Examples

Real transformations from AI code to human code.

---

## Python: Data Processing

**AI version:**
```python
def process_user_data_and_calculate_statistics(user_data_list):
    """
    Process the user data list and calculate statistics.
    
    Args:
        user_data_list: A list of user data objects
        
    Returns:
        A dictionary containing the calculated statistics
    """
    # Initialize result dictionary
    result_dictionary = {}
    
    # Initialize total age counter
    total_age_counter = 0
    
    # Initialize count variable
    user_count = 0
    
    # Iterate through each user in the user data list
    for user_data_object in user_data_list:
        # Check if the user is active
        if user_data_object['is_active'] == True:
            # Add the age to the total age counter
            total_age_counter = total_age_counter + user_data_object['age']
            # Increment the user count
            user_count = user_count + 1
    
    # Calculate the average age
    if user_count > 0:
        average_age = total_age_counter / user_count
    else:
        average_age = 0
    
    # Store the result in the dictionary
    result_dictionary['average_age'] = average_age
    result_dictionary['total_users'] = user_count
    
    # Return the result dictionary
    return result_dictionary
```

**Human version:**
```python
def user_stats(users):
    active = [u for u in users if u['is_active']]
    if not active:
        return {'average_age': 0, 'total': 0}
    avg = sum(u['age'] for u in active) / len(active)
    return {'average_age': avg, 'total': len(active)}
```

---

## JavaScript: API Call

**AI version:**
```javascript
// Function to fetch user data from the API
async function fetchUserDataFromAPI(userId) {
    try {
        // Make the API request
        const apiResponse = await fetch(`/api/users/${userId}`);
        
        // Check if the response was successful
        if (!apiResponse.ok) {
            // Throw an error if the response was not successful
            throw new Error(`HTTP error! status: ${apiResponse.status}`);
        }
        
        // Parse the JSON response
        const userData = await apiResponse.json();
        
        // Return the user data
        return userData;
    } catch (error) {
        // Log the error to the console
        console.error(`An error occurred while fetching user data: ${error}`);
        
        // Return null to indicate failure
        return null;
    }
}
```

**Human version:**
```javascript
async function getUser(id) {
    const res = await fetch(`/api/users/${id}`)
    if (!res.ok) throw new Error(`${res.status}: failed to load user ${id}`)
    return res.json()
}
```

---

## Go: HTTP Handler

**AI version:**
```go
// HandleGetUserRequest handles the HTTP GET request for retrieving user information
func HandleGetUserRequest(responseWriter http.ResponseWriter, httpRequest *http.Request) {
    // Extract the user ID from the URL parameters
    userIDString := httpRequest.URL.Query().Get("id")
    
    // Check if the user ID is empty
    if userIDString == "" {
        // Return a bad request response if the user ID is missing
        http.Error(responseWriter, "User ID is required", http.StatusBadRequest)
        return
    }
    
    // Convert the user ID string to an integer
    userID, conversionError := strconv.Atoi(userIDString)
    if conversionError != nil {
        // Return a bad request response if the user ID is not a valid integer
        http.Error(responseWriter, "Invalid user ID format", http.StatusBadRequest)
        return
    }
    
    // Look up the user in the database
    userObject, databaseError := database.GetUserByID(userID)
    if databaseError != nil {
        // Return an internal server error if the database lookup fails
        http.Error(responseWriter, "Internal server error", http.StatusInternalServerError)
        return
    }
    
    // Encode the user object as JSON and write to the response
    encodingError := json.NewEncoder(responseWriter).Encode(userObject)
    if encodingError != nil {
        http.Error(responseWriter, "Failed to encode response", http.StatusInternalServerError)
    }
}
```

**Human version:**
```go
func (s *Server) getUser(w http.ResponseWriter, r *http.Request) {
    id, err := strconv.Atoi(r.URL.Query().Get("id"))
    if err != nil {
        http.Error(w, "invalid id", http.StatusBadRequest)
        return
    }

    u, err := s.db.GetUser(id)
    if err != nil {
        http.Error(w, "not found", http.StatusNotFound)
        return
    }

    json.NewEncoder(w).Encode(u)
}
```

---

## TypeScript: React Component

**AI version:**
```tsx
// UserProfileComponent displays the user profile information
const UserProfileComponent: React.FC<UserProfileComponentProps> = ({ 
    userProfileData,
    onUserProfileUpdateCallback 
}) => {
    // State for managing loading status
    const [isLoadingState, setIsLoadingState] = useState<boolean>(false);
    
    // Handler function for when the user clicks the update button
    const handleUpdateButtonClickEvent = async () => {
        // Set loading state to true
        setIsLoadingState(true);
        
        try {
            // Call the update callback function
            await onUserProfileUpdateCallback(userProfileData);
        } catch (caughtError) {
            // Log the error to the console
            console.error('An error occurred during update:', caughtError);
        } finally {
            // Set loading state back to false
            setIsLoadingState(false);
        }
    };
    
    // Render the component
    return (
        <div className="user-profile-container">
            <h1>{userProfileData.name}</h1>
            <button 
                onClick={handleUpdateButtonClickEvent}
                disabled={isLoadingState}
            >
                {isLoadingState ? 'Updating...' : 'Update Profile'}
            </button>
        </div>
    );
};
```

**Human version:**
```tsx
const UserProfile = ({ user, onUpdate }: Props) => {
    const [loading, setLoading] = useState(false)

    const save = async () => {
        setLoading(true)
        try {
            await onUpdate(user)
        } catch (e) {
            console.error('update failed', e)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="user-profile">
            <h1>{user.name}</h1>
            <button onClick={save} disabled={loading}>
                {loading ? 'Saving...' : 'Save'}
            </button>
        </div>
    )
}
```

---

## Rust: File Reader

**AI version:**
```rust
/// Function to read the contents of a file at the specified file path
/// and return them as a String
fn read_file_contents_from_path(file_path: &str) -> Result<String, std::io::Error> {
    // Create a new File object by opening the file at the specified path
    let file_object = std::fs::File::open(file_path)?;
    
    // Create a buffered reader for efficient reading
    let mut buffered_reader = std::io::BufReader::new(file_object);
    
    // Initialize an empty string to store the file contents
    let mut file_contents_string = String::new();
    
    // Read all contents into the string
    std::io::Read::read_to_string(&mut buffered_reader, &mut file_contents_string)?;
    
    // Return the file contents
    Ok(file_contents_string)
}
```

**Human version:**
```rust
fn read_file(path: &str) -> Result<String, io::Error> {
    fs::read_to_string(path)
}
```

---

## Bash: Deployment Script

**AI version:**
```bash
#!/bin/bash

# This script deploys the application to the production server

# Define the server hostname variable
SERVER_HOSTNAME="prod-server-01"

# Define the deployment directory variable
DEPLOYMENT_DIRECTORY="/var/www/app"

# Define the backup directory variable
BACKUP_DIRECTORY="/var/backups/app"

# Check if the deployment directory exists
if [ -d "$DEPLOYMENT_DIRECTORY" ]; then
    # Create a backup of the existing deployment
    echo "Creating backup of existing deployment..."
    cp -r "$DEPLOYMENT_DIRECTORY" "$BACKUP_DIRECTORY/backup_$(date +%Y%m%d_%H%M%S)"
    echo "Backup created successfully."
fi

# Copy new files to the deployment directory
echo "Copying new files to deployment directory..."
rsync -avz ./dist/ "$SERVER_HOSTNAME:$DEPLOYMENT_DIRECTORY/"
echo "Files copied successfully."
```

**Human version:**
```bash
#!/usr/bin/env bash
set -euo pipefail

HOST="prod-server-01"
DEPLOY="/var/www/app"
BACKUP="/var/backups/app"

[[ -d "$DEPLOY" ]] && cp -r "$DEPLOY" "$BACKUP/$(date +%Y%m%d_%H%M%S)"

rsync -az ./dist/ "$HOST:$DEPLOY/"
echo "deployed"
```
