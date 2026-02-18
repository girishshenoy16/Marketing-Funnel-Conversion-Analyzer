import subprocess
import sys
import time

def run_step(script_name):
    print(f"\n🚀 Running {script_name}...")
    start = time.time()

    result = subprocess.run([sys.executable, f"src/{script_name}"])

    end = time.time()

    if result.returncode != 0:
        print(f"❌ Error occurred in {script_name}")
        sys.exit(1)
    else:
        print(f"✅ {script_name} completed in {round(end - start, 2)} seconds")

if __name__ == "__main__":

    print("========================================")
    print("🔁 Starting Data Engineering Pipeline")
    print("========================================")

    run_step("data_cleaning.py")
    run_step("funnel_engineering.py")
    run_step("metrics_engineering.py")

    print("\n========================================")
    print("🎉 Data Pipeline Completed Successfully")
    print("========================================")