import streamlit as st

def main():
    st.title("Fraud Detection System (Simple Rule-Based)")

    # Input fields
    st.header("Enter Transaction Details")
    amount = st.number_input("Amount", value=0.0)
    oldbalanceOrg = st.number_input("Old Balance Origin", value=0.0)
    newbalanceOrig = st.number_input("New Balance Origin", value=0.0)
    oldbalanceDest = st.number_input("Old Balance Destination", value=0.0)
    newbalanceDest = st.number_input("New Balance Destination", value=0.0)
    hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, value=0)
    transaction_type = st.selectbox("Transaction Type", ['CASH-IN', 'CASH-OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'])
    transactions_per_account = st.number_input("Transactions per Account", value=1)
    transactions_per_hour = st.number_input("Transactions per Hour", value=1)
    avg_transaction_amount = st.number_input("Average Transaction Amount", value=0.0)
    is_new_account = st.selectbox("Is New Account", [0, 1])
    transactions_per_destination = st.number_input("Transactions per Destination", value=1)
    change_in_transaction_pattern = st.number_input("Change in Transaction Pattern", value=0.0)

    # Create the transaction dictionary
    transaction = {
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'hour': hour,
        'type': transaction_type,
        'transactions_per_account': transactions_per_account,
        'transactions_per_hour': transactions_per_hour,
        'avg_transaction_amount': avg_transaction_amount,
        'is_new_account': is_new_account,
        'transactions_per_destination': transactions_per_destination,
        'change_in_transaction_pattern': change_in_transaction_pattern
    }

    # Calculate the difference and check for fraud
    difference = abs(transaction['oldbalanceOrg'] - transaction['newbalanceOrig'])
    st.write("Transaction Details:", transaction)
    st.write("Difference Between Old and New Balance Origin:", difference)

    if difference > 100000:
        st.write("Prediction: Fraud")
    else:
        st.write("Prediction: Not Fraud")

if __name__ == "__main__":
    main()
