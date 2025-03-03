import subprocess

# module to get secrets from 1Password
## setup module by: 


class SecretsManager:

   # Function to get secrets from 1Password
   def get_secret(item_name, field_name, vault="API_Keys"):
      try:
         # Run the 1Password CLI command to get the secret
         result = subprocess.run(
               ["op", "item", "get", item_name, "--field", field_name, "--vault", vault],
               capture_output=True, 
               text=True, 
               check=True
         )
         return result.stdout.strip()
      except subprocess.CalledProcessError as e:
         print(f"Error retrieving secret: {e}")
         return None
      


