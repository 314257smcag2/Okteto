# Deploy your Development Environments from your Git Repositories

## Prerequisites​

 - When you deploy a Git repository, Okteto Cloud will analyze the source code of your Git repository, looking for clues on how to deploy your application.

### Okteto will look for deployment manifests in the following order:

 - Helm Chart: if your repository has a chart, charts, helm/chart, or helm/charts directory with a Chart.yaml file in it, Okteto will detect the chart and run helm upgrade --install on it.
 - Kubernetes manifests folder: if your repository has a manifests, kubernetes, or k8s folder, Okteto will detect it and run kubectl apply on the folder.
 - Kubernetes manifests file: if your repository has a manifests.yaml, kubernetes.yaml, or k8s.yaml file, Okteto will detect it and run kubectl apply on the manifest file.
 - Okteto Stacks file: if your repository has a okteto-stack.yaml file, Okteto will detect it and run okteto stack deploy --build on this file.
 - Docker-compose file: if your repository has a docker-compose.yaml, Okteto will detect it and run okteto stack deploy --build on this file.
 - Okteto Manifest file: if your repository has an okteto.yml or .okteto/okteto.yml file, Okteto will detect it and run okteto push on the manifest file.
 
If Okteto is not able to detect how to deploy your application, or you want to have more control over it, you can setup an Okteto Pipeline by adding a okteto-pipeline.yml or .okteto/okteto-pipeline.yml file to the root of your repository.      

 ## 网页图片框选工具

 - https://fengyuanchen.github.io/cropperjs/
 - https://github.com/fengyuanchen/cropperjs
 - https://github.com/tapmodo/Jcrop
 - https://jcrop.com/
 - http://code.ciaoca.com/jquery/jcrop/demo/preview
