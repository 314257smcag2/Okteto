### tensorflow jupyter notebook

 services:   
  tf:   
    image: jupyter/tensorflow-notebook     
    ports:    
      - 8888:8888      
      
### jupyter notebook

 services:     
  jupyter:      
    image: jupyter/datascience-notebook
    ports:    
      - 8888:8888     
      
### nginx

 services:   
  nginx:   
    image: nginx    
    restart : always     
    ports:    
      - 8080:8080    
      - 80:80      