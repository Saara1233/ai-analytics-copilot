# main.py
from src.ingestion import load_passenger_data
from src.analytics import calculate_total_revenue, calculate_survival_rate

def run_pipeline():
    print("=" * 50)
    print("🚢 AI ANALYTICS COPILOT - INITIALIZING ENGINE 🚢")
    print("=" * 50)
    
    data_path = "data/titanic_sample.csv"
    print(f"🔄 Ingesting logs from: {data_path}...")
    passengers = load_passenger_data(data_path)
    
    if not passengers:
        print("❌ Pipeline halted: No data loaded.")
        return
        
    print(f"✅ Successfully processed {len(passengers)} records.")
    print("\n📊 RUNNING CORE METRICS SYSTEM...")
    
    revenue = calculate_total_revenue(passengers)
    survival_pct = calculate_survival_rate(passengers)
    
    print("-" * 50)
    print(f"💰 Total Revenue Collected : ${revenue:,}")
    print(f"🧬 Fleet Survival Rate     : {survival_pct}%")
    print("-" * 50)
    print("🎉 Execution Complete. Architecture Stable.")

if __name__ == "__main__":
    run_pipeline()