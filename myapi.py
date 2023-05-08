from fastapi import FastAPI

app = FastAPI()

list={
    '1':{'name': 'Baking','condition':"done"},
    "2":{'name': 'Cleaning','condition': "not done"},
    "3":{'name': 'Gaming','condition': "not done"},
    "4":{'name': 'Mukbang','condition': "done"}
    }
@app.get("/")
def index():
    return {'message':'welcome to todo app list'}

@app.get("/list")
def print_list():
    return {'activity list':list}

@app.get("/filter/{status}")
def filter(condition:str):
    names = []
    if not condition == "done" and not condition == "not done":
        return "error: answer with done or not done only"
    for data in list.values():
        if data['condition'] == condition:
            names.append(data['name'])
    return {"Done list": names}

@app.post("/add_data/{todo_id}")
def add_data(name: str, condition: str):
    if not condition == "done" and not condition == "not done":
        return "error: conditoin should be done or not done only"
    
    new_id = str(len(list)+1)
    list[new_id] = {'name': name, 'condition': condition}
    return {"message" : "done added"}

@app.delete("/deletelist/{todo_id}")
def delete_list():
    global list
    list = {}

@app.delete("/deletedata/{todo_id}")
def delete_data(num: str):
    newlist={}

    if num in list:
        del list[num]
        index = 1
        for x in list:
            newlist[str(index)] = list[x]
            index+=1
        list.clear()
        list.update(newlist)
        return {'activity list':list}
    
@app.put("/update_condition/{status}")
def update_condition(name:str, condition: str):
    for x in list:
        if list[x]["name"]==name:
            if list[x]["condition"] == condition:
                    return "must input different condition"
            else:
                list[x]["condition"] = condition
                return {'activity list':list}
        
@app.put("/edit name/{todo_id}")
def change_name(name:str, new_name: str):
    for x in list:
        if list[x]["name"] == name:
            list[x]["name"] = new_name
            return {'activity list':list}

