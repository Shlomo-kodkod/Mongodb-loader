oc new-app mongodb/mongodb-community-server:7.0-ubi9 MONGO_INITDB_ROOT_USERNAME=admin MONGO_INITDB_ROOT_PASSWORD=pass

oc get deployment

oc set volumes deployment mongodb-community-server --add --mount-path=/data --name=mongopvc --claim-name=mongopvc --read-only=false --type=persistentVolumeClaim --claim-size=1Gi

oc get pods

oc rsh mongodb-community-server-67c4c6b457-jb69z

mongosh -u admin -p pass

use mongodb

db.students.insertMany([{name: 'shlomo'},{name: 'dany'}])


