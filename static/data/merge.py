import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('ga_georgia_zip_codes_geo.min.json') # geojson file
pdf = pd.read_csv('Zip_code.csv') # CSV file
cd = pd.read_csv('census_data.csv')
df = pd.DataFrame(pdf)
df_cd = pd.DataFrame(cd)
df['ZCTA5CE10'] = df.ZCTA5CE10.astype(str)
joined_gdf = gdf.merge(df,on="ZCTA5CE10" )
df_cd['ZCTA5CE10'] = df_cd.ZCTA5CE10.astype(str)
joined_gdf = joined_gdf.merge(df_cd, on="ZCTA5CE10" )
joined_gdf.to_file('ga_merge.json', driver="GeoJSON")