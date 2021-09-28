#see if  a student is pass or fail on basis of 3 subject marks , minimum score of avg 40% and atleast 33% individually
sub1 = int(input("Write the first subject name\n"))
sub2 = int(input("Write the second subject name\n"))
sub3 = int(input("Write the third subject name\n"))
a = (sub1 + sub2 + sub3)/3
if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed")
elif(a>40): 
    print("you are passed")

    