# Read GCP Files
## Google Cloud SDK
This script utilizes gsutil tool that is part of the Google Cloud SDK and is used for accessing Google Cloud Storage. You need to install Google Cloud SDK using the link: https://cloud.google.com/sdk/docs/install and installing in Desktop. Or if you want to install using terminal, navigate to project directory and install SDK by following this:
curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-367.0.0-darwin-x86_64.tar.gz
tar -xf google-cloud-sdk-367.0.0-darwin-x86_64.tar.gz
./google-cloud-sdk/install.sh
./google-cloud-sdk/bin/gcloud init
To include SDK path in base path: export PATH=$PATH:/path/to/google-cloud-sdk/bin, for me: export PATH=$PATH:./google-cloud-sdk/bin
To ensure all paths and environment variables are setup correctly, run: gsutil --version
Make sure you have the correct bucket gsutil url: gsutil ls gs://bucket_name/ 

## Stream file for downstream processing
Once you have SDK and gsutil setup, it should be pretty straightforward. This script uses subprocesses package from python to read and store the files parsed in from gsutil. It is then later stored as a pandas dataframe. Feel free to manipulate this function as needed. I have created a very basic function to read in .bed files as pandas dataframe. 
