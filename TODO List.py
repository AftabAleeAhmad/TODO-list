# ----------TODO Handler---------- #
import json
collection={}
file_name = 'E:\Python\\assignments\\todo_by_dict\Data_file(todo).json'
with open(file_name,'r',encoding='utf-8') as get_previous_data:
    collection = dict (json.load(get_previous_data))
# with open(file_name,'w',encoding='utf-8') as save_previous_data:
#     json.dump(data,save_previous_data)
#     collection = dict(save_previous_data)

# collection = {}


def save_function(key,data):
    # print("save funtion is called...")
    with open (file_name,'w+',encoding='utf-8') as save_file:
        collection.update({key:data})
        json.dump(collection,save_file)
        print("file saved")


def delete_function(remo):
    # print("delete function is called...")
    with open (file_name,'r+',encoding='utf-8') as delete_file:
        collect = dict (json.load(delete_file))
        if remo in collect:
            del collect[remo]
            print(collect)
            delete_file.seek(0)
            # with open (file_name,'w',encoding='utf-8') as delete_file:
            json.dump(collect,delete_file)
            delete_file.truncate()
        # delete_file.close()
        else:
            print("No task found ERROR 404")



def search_function(data_to_find):
    # print("Search function is called...")
    with open (file_name,'r',encoding='utf-8') as search_file:
        search = dict (json.load(search_file))
        if data_to_find in search:
            print("\t\t.....Data found.....")
            print(f"Task name: {data_to_find}\nTask Status: {search[data_to_find]}")
        else:
            print("\t\t.....data not found.....")
        # print("data is printed")




def view_function():
    # print("View function is called...")
    with open (file_name,'r',encoding='utf-8') as view_file:
        for dictionary in view_file:
            print('\n')
            print(f'{dictionary} \n')
        print("data is printed")


def exit_function():
    print("Exit function is called...")


while True:
    choice = ''
    print("""
            Please make a choice in....
            1: to Save task...
            2: to Delete task...
            3: to Search saved task...
            4: to View saved task...
            5: to Exit from TODO manager...""")
    choice = input()
    if choice == '1':
        print("\t\t\t-----You choosed Save-----")
        print("Enter task name: ")
        task = input(str())
        print("Enter status of task: ")
        status  = input(str())
        #  data = {task:status}
        save_function(task,status)
    elif choice == '2':
        print("\t\t\t-----You choosed Delete-----")
        print("Enter task name: ")
        dele = input(str())
        delete_function(dele)
    elif choice == '3':
        print("\t\t\t-----You choosed Search-----")
        print("Enter task name: ")
        sear = input(str())
        search_function(sear)
    elif choice == '4':
        print("\t\t\t-----You choosed View-----")
        view_function()
    elif choice == '5':
        exit_function()
        break
    else:
        print("please make a right choice...")