node {
  stage('Build') {
    openshift.withCluster() {
      openshift.withProject() {
         openshift.startBuild("tornadoapp").logs('-f')
      }
    }
  }
  stage('Test') {
     sleep 5
//     sh "curl -s http://flask:8080/health"
  }
}
