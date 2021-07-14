
import json
b = []
user_input=input("enter what you want..login or signup--")
if user_input=="signup":
    username=input("enter user name--")
    def mainfun():
        password1=input("enter your first password--")
        password2=input("conform your password--")
        for num in password1:
            if num.isdigit():
                break
        if password1==password2:
            if len(password1)>=8 or len(password1)<=16:
                print("your password are same")
                if num in password1:
                    if "#" in password1 or "@" in password1 or "$" in password1:
                        print("valid password")                 
                        my_file=open("neha.json","r")
                        a = json.load(my_file)
                        print(a)
                        my_file.close()
                        # b = a["user"]
                        c=a["user"]
                        i=0
                        print(len(c[i]))
                        while i<len(c[i]):
                            if c[i]["username1"]==username or c[i]["password1"]==password1 :
                                print(username,password1,"you already signed up")
                                break
                            i=i+1
                        else:
                            description=input("enter what you like---")
                            Dob=input("enter your date of birth---")
                            Gender=input("enter your gender--")
                            Hobbies=input("enter tour Hobbies--")
                            list1=["Description","Dob","Gender","Hobbies"]
                            new_list=[]
                            new_list.append(description)
                            new_list.append(Dob)
                            new_list.append(Gender)
                            new_list.append(Hobbies)
                            profile={}
                            i=0
                            while i<len(list1):
                                profile.update({list1[i]:new_list[i]})
                                i=i+1
                            print(profile,"iytrdewserytuioiuytre")

                            b = a["user"]
                            f = b
                            dic={}
                            dic["username1"]=username
                            dic["password1"]=password1
                            dic["profile"] = profile
                            # dic["profile"]=list1
                            f.append(dic)
                            d = {"user" :f}
                            print("okey....")
                            my_file1=open("neha.json","w")
                            json.dump(d,my_file1,indent=3)
                            
                    else:
                        print("At least password should contain one special character")
                else:
                    print("At least password should contain one number")
            else:
                print("your password is not valid")
        else:
            print("both password are not same")
            mainfun()
    mainfun()


else:
    username=input("enter user name--")
    password1=input("enter your first password--")
    my_file=open("neha.json","r")
    a = json.load(my_file)
    my_file.close()
    c=a["user"]
    i=0
    while i<len(c[i]):
        if c[i]["username1"]==username and c[i]["password1"]==password1:
            print("you already logged in")
            break
        i=i+1
    else:
        print("invalid password...")





