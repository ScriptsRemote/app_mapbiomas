import geopandas as gpd

# Caminho para o arquivo Shapefile
shapefile_path = 'asset\BR_Municipios_2022.shp'

# Carregar o Shapefile como um GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Caminho para salvar o arquivo GeoJSON
geojson_path = 'asset\municipios_br.geojson'

# Salvar o GeoDataFrame como um arquivo GeoJSON
gdf.to_file(geojson_path, driver='GeoJSON')

print("Arquivo GeoJSON criado com sucesso!")