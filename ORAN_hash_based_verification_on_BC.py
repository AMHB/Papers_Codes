import hashlib

# sample device data
device_data = {
    "serial_number": "Ali123",
    "firmware_version": "1.1.2",
    "manufacturer": "ex Ericsson"
}



# Function to calculate the hash of the device data

def calculate_hash(data):
    # Convert data to a string
    data_string = str(data)
    # Create a SHA-256 hasher object- it can be changed based on the agreed Hash function in Smart Contract
    hasher = hashlib.sha256()
    # Encode the data string as bytes
    encoded_data = data_string.encode()
    # Update the hasher with the encoded data
    hasher.update(encoded_data)
    # Get the hexadecimal digest of the hash
    return hasher.hexdigest()



# Calculate the hash of the simulated device data
device_hash = calculate_hash(device_data)

# Simulated trusted hash stored on the blockchain- This is an example and must be checked with
# the stored one provided by supplier  

trusted_hash = "1234567890abcdef1234567890abcdef12345678"



# Compare the calculated hash with the trusted hash

if device_hash == trusted_hash:
    print("Device is authentic!")
else:
    print("Device is illegaly swapped or potentially tampered with!")
