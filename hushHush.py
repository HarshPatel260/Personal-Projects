import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import PySimpleGUI as sg
import ssl
import smtplib
from email.message import EmailMessage
from updated_email import sendInvite

# Create a dictionary that maps country codes to full names
country_codes = {
    'USA': 'United States',
    'UK': 'United Kingdom',
    'IN': 'India',
    # Add more mappings as needed
}

# Load the data from the CSV file
df = pd.read_csv('Top_Users_data.csv')

# Replace country codes with full names
df['Location'] = df['Location'].map(country_codes).fillna(df['Location'])

# Define the features and target
features = ['Bronze Badges', 'Silver Badges', 'Gold Badges']
target = 'good'

# Define the layout for the GUI
layout = [
    [sg.Text('Location: '), sg.Input(key='location')],
    [sg.Text('Number of Top Users: '), sg.Input(key='num_top_users')],
    [sg.Button('Show Result'), sg.Button('Send Email') ,sg.Button('Exit')],
    [sg.Output(size=(70, 20))]
]

# Create the window
window = sg.Window('Hus Hus Recruiter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    # Filter the data based on the location and select the relevant columns
    location_filtered_df = df[df['Location'] == values['location']]

    if event== 'Send Email':
        emails= [i for i in top_users['email']]
        sendInvite(emails)

        

    if location_filtered_df.empty:
        print('No candidates found that meet the criteria')
    else:
        # # Create a new target variable that indicates whether a user is good or bad based on their average reputation and badge count
        # avg_reputation = df['Reputation'].mean()
        # avg_bronze = df['Bronze Badges'].mean()
        # avg_silver = df['Silver Badges'].mean()
        # avg_gold = df['Gold Badges'].mean()
        
        # location_filtered_df['good'] = ((location_filtered_df['Reputation'] + location_filtered_df['Bronze Badges'] + location_filtered_df['Silver Badges'] + location_filtered_df['Gold Badges']) / 4 >= (avg_reputation + avg_bronze + avg_silver + avg_gold) / 4).astype(int)

        # # Create a logistic regression model and fit it to the data
        # model = LogisticRegression()
        # model.fit(location_filtered_df[features], location_filtered_df[target])

        # # Calculate the accuracy of the model
        # y_pred = model.predict(location_filtered_df[features])
        # accuracy = accuracy_score(location_filtered_df[target], y_pred)
        # print(f"Model accuracy: {accuracy:.2f}")

        # Select the top users based on their reputation
        top_users = location_filtered_df.nlargest(int(values['num_top_users']), 'Reputation')

        # Print the details of the top users
        print(top_users)

        # Save the output to a CSV file
        output_file_path = 'output.csv'
        top_users.to_csv(output_file_path, index=False)
        print(f"Output saved to {output_file_path}")

# Close the window
window.close()
