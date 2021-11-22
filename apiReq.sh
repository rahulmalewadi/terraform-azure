curl -XPOST -u "rahulmalewadi:${{secrets.PAT_TOKEN}}" -H "Accept: application/vnd.github.everest-preview+json" -H "Content-Type: application/json" https://api.github.com/repos/rahulmalewadi/terraform-azure/dispatches --data '{"event_type": "deploy_workflow"}'
     
      

      

 

      

  
