# https://console.cloud.google.com/security/secret-manager/secret/E88/versions?project=site-exceptions-and-mop-prod
# https://cloud.google.com/secret-manager/docs/configuring-secret-manager
# https://cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python

# This is the guide to get started
# https://codelabs.developers.google.com/codelabs/secret-manager-python#0

# This code creates a secret in Secret Manager
# https://console.cloud.google.com/security/secret-manager?orgonly=true&project=site-exceptions-and-mop-prod&supportedpurview=organizationId

# Import the Secret Manager client library.
from google.cloud import secretmanager

PROJECT_ID = "site-exceptions-and-mop-prod"


def create_secret(secret_id):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project.
    parent = f"projects/{PROJECT_ID}"

    # Build a dict of settings for the secret
    secret = {"replication":
        {"user_managed":
            {"replicas":
                [
                    {"location": "europe-west1"}
                ]
            }
        }
    }

    # Create the secret
    response = client.create_secret(secret_id=secret_id, parent=parent, secret=secret)

    # Print the new secret name.
    print(f'Created secret: {response.name}')


if __name__ == "__main__":
    create_secret("my_secret_value")
