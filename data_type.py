        

## type casting (changing the type of data)
        #int
        #float
        #complex
        #str
        #bool
        #bytes
        #NoneType
    ## Non primitive(collection type)
        #list
        #tuple
        #range
        #set
        #frozenset
        #dict
        #bytearray

# j=4
# i=10
# i=12.9
# i=3+1j
# i='python'
# i=False
# i=b'python'
# i=None

### Type casting(changing the type of data)

# i=10.87
# print(int(i))
# print(float(i))
# print(complex(i))
# print(bool(i))
# print(str(i))   #'10'
# print(bytes(i))   #error

# i=4+8j    #0+0j

# print(int(i))
# print(float(i))
# print(bool(i))
# print(str(i))   
# print(bytes(i)) 

# i=True

# print(int(i))
# print(float(i))
# print(bool(i))
# print(str(i))   
# print(bytes(i))

# s="1234"

# print(int(s))
# print(float(s))
# print(bool(s))
# print(str(s))   
# print(bytes(s,encoding="utf8"))


# print(type(i))

##ASCII Values ---American standard code for information Interchange

## Non primitive type(collection type)

#list
      # l=[12,34,65,"python",[1,2,"ducat"]]
      #l[1]=96
      # print(l)

## tuple

             #t=[12,34,65,"python",[1,2,"ducat"]]
             #t[1]=96
             #print(t[3])

## range

        #r=range(1,101,2)
        #r=range(100,0,-1)
        #print(tuple(r))

## set

      #s={23,67,76,"python",(34,98+7j),23}
      #print(s)

## frozenset

       #s={23,67,76,"python",(34,98+7j),23}
       #print(frozenset(s))


### dictionary(dict)

         #d={'a':"apple",'b':"ball",3:"apple"}
         
         #print(d['a'])
         #d['a']="aeroplane"
         #print(d)



###bytearray

           #b=b'python'
           #ba=bytearray(b)
           
           #print(b[4])
           #ba[2]=105
           
           #print(ba)


a=input("enter a number:")
b=input("enter another number")

#print(type(a),type(b))

print("Addition of user input data:",int(a)+int(b))