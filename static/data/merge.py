import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('fl_florida_zip_codes_geo.min.json') # geojson file
pdf = pd.read_csv('Zip_code.csv') # CSV file
df = pd.DataFrame(pdf)
df['ZCTA5CE10'] = df.ZCTA5CE10.astype(str)
joined_gdf = gdf.merge(df,on="ZCTA5CE10" )
joined_gdf.to_file('fl_merge.json', driver="GeoJSON")