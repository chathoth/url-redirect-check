import csv
import requests

def check_redirect(source_path, destination_path, domain_name):
    source_url = domain_name + source_path
    response = requests.get(source_url, allow_redirects=True)
    
    print(f"Checking redirect from {source_url} to {destination_path}:")
    print("Initial Status Code:", response.status_code)
    print("Initial URL:", response.url)
    
    redirect_chain = [(response.status_code, response.url)]
    
    while response.history:
        redirect = response.history.pop(0)
        redirect_chain.append((redirect.status_code, redirect.url))
        print("Redirected to:", redirect.url)
        print("Status Code:", redirect.status_code)
        
    final_status_code = response.status_code
    final_url = response.url
    
    if final_url.endswith(destination_path):
        print("Redirect successful to destination.")
    else:
        print("Redirect unsuccessful.")
    
    return redirect_chain

def main(csv_file, domain_name):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            source_path, destination_path = row
            redirect_chain = check_redirect(source_path, destination_path)
            print("Redirect Chain:")
            for idx, (status_code, url) in enumerate(redirect_chain, start=1):
                print(f"{idx}. Status Code: {status_code}, URL: {url}")
            print("\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <domain_name>")
        sys.exit(1)
    
    domain_name = sys.argv[1]
    csv_file = "redirect_data.csv"  # Change this to your CSV file path
    main(csv_file, domain_name)
