import requests
import json 
import gradio as gt
import os

url="http://localhost:11434/api/generate"

headers={
    
    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append(prompt)
    final_prompt="\n".join(history)
    
    data={
        "model":"Codetask",
        "prompt":final_prompt,
        "stream":False,
        
    }
    
    response=requests.post(url=url,headers=headers,data=json.dumps(data))
    
    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actural_response=data['response']
        return actural_response
    else:
        print("error:",response.text)
        
        
#thsi was complete backend now its turn of frontend

interface=gt.Interface(
    fn=generate_response,
    inputs=gt.Textbox(lines=4, placeholder="Enter your Response"),
    outputs="text"
    
)

port = int(os.environ.get("PORT", 7860))  # 7860 is default for local
interface.launch(server_name="0.0.0.0", server_port=port)
