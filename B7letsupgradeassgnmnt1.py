#list and its default function
lst=[1,-2,9,"hello",[3,6,90]]
print("list is ",lst)
print(lst[2:])
print("last element of list is",lst[-1])
lst.append(2)
print(lst)
print(lst.index("hello"))
lst.clear()
print(lst)
lst.extend("hey sai")
print(lst)
a=[1,-1,78,6]
lst=print("new list is ",a.copy())
a.sort()
print("new sorted element is",a)
print(a)
print(a.count(""))
print("minimum no is",min(a))
print("maximum no is",max(a))
print("the sum of element is",sum(a))
print(type(a))
print("#############################################")
#dictionary and its default functions
dic={"name":"ritu","from":"mfp","learning":"python language","pin":842003}
print("dictionary is ",dic)
print(dic.items())
print(dic.get("from"))
print(str(dic))
print(type(dic))
print(len(dic))
keys=["very interesting","boring"]
values=["fascinating","tedious"]
data=dict(zip(keys,values))
print(data)
print("#################################################")
#sets and its default functions
st={1,90,-1,67,"letsupgrade",4,1}
print("The set is",st)
st1={1,"letsupgrade"}
print(st1.issubset(st))
st.remove(90)
print(st)
st.add("hii")
print(st)
print(st1.isdisjoint(st))
print(st1.union(st))
print("######################################################")
#tuple and its default function
tup=("sai","Batch",7,"letsupgrade","day",2)
print("The tuple is",tup)
print(tup.index("sai"))
print(len(tup))
print(tup.count("sai"))
tuple1=(0,1,2)
print(tuple1[::-1])#slicing in tuples
print("######################################################")
#String and its default function
str="hello world"
print(str)
print(str[2:5])
print(len(str))
print(str.index("o"))
print(str.upper())
print(str.replace("h","j"))







      









      
