# D3 JS

## Load the data from S3

1. Make the JSON file public
2. Update CORS settings on the bucket

```xml
<CORSConfiguration>
 <CORSRule>
   <AllowedOrigin>*</AllowedOrigin>

   <AllowedMethod>GET</AllowedMethod>
   <AllowedMethod>PUT</AllowedMethod>
   <AllowedMethod>POST</AllowedMethod>
   <AllowedMethod>DELETE</AllowedMethod>

   <AllowedHeader>*</AllowedHeader>
 </CORSRule>
</CORSConfiguration>
```

3. Modify the location of the data in the html files