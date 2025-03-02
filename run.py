import subprocess

def main():
    print("Running populate.py...")
    subprocess.run(["python", "populate.py"])

    # exporting data to CSV :3
    print("Running process.py...")
    subprocess.run(["python", "process.py"])

    print("Scripts executed successfully!")

if __name__ == "__main__":
    main()