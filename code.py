import requests
ip_data = []
for ip in final_df["c-ip"].unique():
response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json() response["c-ip"] = ip
response["cs-username"] = final_df.loc[final_df['c-ip'] == ip]['cs-username').values[0]
ip_data.append(response.values())
ip_final = []
for ip in ip_data: ip_final.append(list(ip))                                                              
ip_final[0]
len(ip_final)
ip_columns = list(response.keys())
print(ip_columns)
#creating another dataframe just with "cs-username" and "s-ip" for geolocation purpose
ip_df = pd.DataFrame(np.array(ip_final),columns= ip_columns)
ip_df.head()
#creating table and uploading dataframe to mysql 
tableName = "geolocation"
sqlEngine = create engine('mysql+pymysql://root:@127.0.0.1/http_request', pool_recycle=3600)
dbConnection = sqlEngine.connect()
try:
  frame = ip_df.to_sql(tableName, dbConnection, if_exists='fail');
except ValueError as vx:
  print(vx)
