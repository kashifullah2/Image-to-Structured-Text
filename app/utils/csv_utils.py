import pandas as pd

def save_to_csv(data, filename="output.csv"):
    """Save extracted data (list or dict) to CSV file."""
    df = pd.DataFrame([data]) if isinstance(data, dict) else pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return filename

def read_csv(filename="output.csv"):
    """Read and display saved CSV file."""
    df = pd.read_csv(filename)
    return df
