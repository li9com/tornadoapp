# tornadoapp
Sample Dockefile application written in Python


##  OpenShift build


```

cat > bc_tornadoapp.yaml <<EOF
apiVersion: v1
kind: BuildConfig
metadata:
  name: tornadoapp
spec:
  strategy:
    type: JenkinsPipeline
    jenkinsPipelineStrategy:
      jenkinsfilePath: Jenkinsfile
  source:
    git:
      uri: "https://github.com/li9com/tornadoapp.git"
      ref: master
EOF

oc create -f bc_tornadoapp.yaml
```
