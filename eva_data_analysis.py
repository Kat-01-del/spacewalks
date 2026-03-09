import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    '''
    Reads a JSON file and converts it to a Pandas dataframe. 
    Drops any rows where duration or date is missing.

    Args:        
        input_file (str): The path to the JSON file containing the data
    
    Returns:     
        eva_df (pd.DataFrame): A Pandas dataframe containing the data from the JSON file
    '''
    print(f'Reading JSON file {input_file}')
    
    # Read the data from a JSON file into a Pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any rows where duration is missing
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    '''
    Writes a pandas dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The dataframe to be written to a CSV file

    Returns:
        None
    '''
    print(f'Saving to CSV file {output_file}')
    # Save dataframe to CSV file for later analysis
    df.to_csv(output_file, index=False, encoding='utf-8')

def plot_cumulative_time(df, graph_file):
    '''
    calculates the cumulative time spent in space and plots it against the date, saving the graph to a file.
    Args:
        df (pd.DataFrame): The dataframe containing the EVA data, including 'duration' and 'date' columns
        graph_file (str): The path to the file where the graph will be saved

    Returns:
        None
    '''
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()
    
# Main code

print("--START--")

input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv', 'w', encoding='utf-8')

graph_file = './cumulative_eva_graph.png'
# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)

# Sort dataframe by date ready to be plotted (date values are on x-axis)
eva_data.sort_values('date', inplace=True)

# Plot cumulative time spent in space over years
#print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
plot_cumulative_time(eva_data, graph_file)

# eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
# eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()

# plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
# plt.xlabel('Year')
# plt.ylabel('Total time spent in space to date (hours)')
# plt.tight_layout()
# plt.savefig(graph_file)
# plt.show()

print("--END--")
