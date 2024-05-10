#Multipul value listed
list_of_num =[]
list_of_num.append(1)
list_of_num.append(2)
list_of_num.append(3)
list_of_num.append("Umar")

print("list_of_num")

#Arry use listed
list_of_cloud =["aws","azure","gcp","orcal"]
list_of_evn=["dev","test","prod"]

#list Iteration

for cloud in list_of_cloud:
    if cloud =="aws":
        print("AWS is best cloud")

#dictionary
dict_of_cloud ={
    "aws":"Amazon Web Services",
    "auzre": "Micosoft Azure",
    "gcp":"Google Cloud Platfrom"
}

print(dict_of_cloud.get("azure","Not Found"))
print(dict_of_cloud ["aws"])
#add dictionary
dict_of_cloud.update({"linode":"linode cloud "})
print(dict_of_cloud)





