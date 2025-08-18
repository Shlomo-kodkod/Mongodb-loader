# Data server project 
- A service that returns to GET request all the information that exists in the collection.


## Project Features
- Mongodb database using OpenShift.
- Access layer to DB.
- FastAPI server - Accesses mongodb and returns the  data to a dedicated endpoint.

## Project structure
```
data-loader/
├── services/
│ └── data_loader.py # Data loading service
| └── app.py #End point service
├── scripts/ #  OS scripts
├── infrastructure/
│ └── k8s/ # Kubernetes manifests (YAMLs)
├── Dockerfile
├── requirements.txt
└── README.md
```