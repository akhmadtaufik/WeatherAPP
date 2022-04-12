import json
from pandas import json_normalize
from IPython.display import display

def getCityIDByCountry(jsonFile, kodeNegara = 'ID'):
    '''
    jsonFile dapat diunduh di http://bulk.openweathermap.org/sample/
    Parameter default kodeNegara menggunakan Negara Indonesia atau 'ID'
    '''
    with open(jsonFile, 'r', encoding='utf-8') as readFile:
        data = json.load(readFile)
        
    rawData = json_normalize(data)
    df = rawData.loc[rawData['country'] == kodeNegara].copy()
    del df['state']
    df.rename(columns={'name':'namaKota', 'country':'negara', 'coord.lon':'longitude', 'coord.lat':'latitude'},
              inplace=True)
    df.loc[:,'id'] = df['id'].astype(int)
    df.reset_index(drop=True, inplace=True)
    return df

def saveToCsv(data, kodeNegara = 'ID'):
    # Kode Negara Default Indonesia / ID
    data = getCityIDByCountry(data, kodeNegara)
    country = data.negara.iloc[1]
    return data.to_csv('ListCity-{}.csv'.format(country), index=False)