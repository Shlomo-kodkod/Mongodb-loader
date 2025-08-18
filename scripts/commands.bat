oc new-app mongodb/mongodb-community-server:7.0-ubi9 -e MONGODB_USER=user -e MONGODB_PASSWORD=pwd -e MONGODB_DATABASE=mongodb -e MONGODB_ADMIN_PASSWORD=rootpwd

oc get deployment

oc set volumes deployment mongodb-community-server --add --mount-path=/data --name=mongopvc --claim-name=mongopvc --read-only=false --type=persistentVolumeClaim --claim-size=1Gi

