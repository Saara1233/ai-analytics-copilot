

def calculate_total_revenue(passenger_list):
    total_revenue = 0.0
    for passenger in passenger_list:
        fare_str = passenger.get('fare', '0.0')
        if not fare_str:
            fare_str = '0.0'
        total_revenue += float(fare_str)
    return round(total_revenue, 2)

def calculate_survival_rate(passenger_list):
    if not passenger_list:
        return 0.0
    survivors = 0
    for passenger in passenger_list:
        if passenger.get('survived') == '1':
            survivors += 1
    rate = (survivors / len(passenger_list)) * 100
    return round(rate, 2)
