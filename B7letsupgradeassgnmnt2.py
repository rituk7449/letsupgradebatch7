altitude=int(input("Enter the height of a plane:"))
#condition for landing a plane
if altitude==1000:
    print("safe to land")
elif altitude<5000:
    print("bring down to 1000")
else:
    print("turn around and try later")
print("thank you")

          
