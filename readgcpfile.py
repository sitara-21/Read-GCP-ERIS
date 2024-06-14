import pandas as pd
import io
import subprocess

def read_bucket_file(file_path, sep="\t", comment='t', header=None):
    """
    Function to read a .bed file with no column names from a Google Cloud Storage bucket
    """
    if file_path.startswith('gs://'):
        # Use gsutil to stream the file content as pandas dataframe
        process = subprocess.Popen(['gsutil', 'cat', file_path], stdout=subprocess.PIPE)
        content = process.communicate()[0].decode('utf-8')
        buffer = io.StringIO(content)
        df = pd.read_csv(buffer, sep=sep, comment=comment, header=header)
    else:
        # Read local file
        df = pd.read_csv(file_path, sep=sep, comment=comment, header=header)
    
    return df

if __name__ == '__main__':
    # Read the labels DataFrame
    df_path = 'gs://bucket_name/file.bed'
    labels_df = read_bucket_file(df_path)
    print(labels_df.head())