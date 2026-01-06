import pandas as pd

def find_mean(df):  
    midpoints = (df['Lower'] + df['Upper']) / 2
    fixi = (midpoints * df['Freq']).sum()
    fi = df['Freq'].sum()
    return fixi/fi
   

def find_median(df):
    n = df['Freq'].sum()
    median_idx = n/2
    cum_sum = 0
    for idx, row in df.iterrows():
        cum_sum += row['Freq']
        if cum_sum >= median_idx:
            L = row['Lower']
            B = cum_sum - row['Freq']
            G = row['Freq']
            w = row['Upper'] - row['Lower'] + 1

            median = L + ((median_idx - B)/G)*w
            break
        
    return median


def find_mode(df):
    modal_idx = df['Freq'].idxmax()
    L = df.loc[modal_idx,'Lower']
    f1 = df.loc[modal_idx,'Freq']
    f0 = df.loc[modal_idx - 1,'Freq'] if modal_idx > 0 else 0
    f2 = df.loc[modal_idx + 1,'Freq'] if modal_idx < len(df)-1 else 0
    w = df.loc[modal_idx,'Upper'] - df.loc[modal_idx,'Lower'] + 1
    mode = L + ((f1 - f0)/((f1-f0) + (f1 - f2)))*w
    
    return mode


data = [
    [50,59,4],
    [60,69,5],
    [70,79,6],
    [80,89,9],
    [90,99,7]
]

df = pd.DataFrame(data,columns = ['Lower','Upper','Freq'])

print("Average:",round(find_mean(df),2))
print("Median:",round(find_median(df),2))
print("Mode:",round(find_mode(df),2))