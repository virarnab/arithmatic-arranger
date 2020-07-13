def arithmetic_arranger(problems, att = None):
    if att == True:
    #if len(signature(arithmetic_arranger).parameters)==2 and list(signature(arithmetic_arranger))[1]==True:
      if len(problems)>5:
        print("Error: Too many problems.")
      else:
        for x in problems:
            if  "+" in x:
                x = "".join(x.split())
                a = x.find("+")
                if x[:a].isdigit()==True and x[(a+1):].isdigit()==True:
                    b = int(x[:a])
                    c = int(x[(a+1):])
                    d = max(len(str(c)),len(str(b)))
                    k = d+2
                    if len(str(c))>4 or len(str(b))>4:
                        print("Error: Numbers cannot be more than four digits.")
                    else:
                        txt1 = "{:>%d}" %k
                        txt2 = "{:>%d}" %d

                        print(txt1.format(x[:a]))
                        print("+",txt2.format(x[(a+1):]))
                        print("-"*(d+2))
                        e = b+c
                        print(txt1.format(e))

                else:
                    print("Error: Numbers must only contain digits.")

            elif  "-" in x:
                x = "".join(x.split())
                a = x.find("-")
                if x[:a].isdigit()==True and x[(a+1):].isdigit()==True:
                    b = int(x[:a])
                    c = int(x[(a+1):])
                    d = max(len(str(c)),len(str(b)))
                    k = d+2
                    if len(str(c))>4 or len(str(b))>4:
                        print("Error: Numbers cannot be more than four digits.")
                    else:
                        txt1 = "{:>%d}" %k
                        txt2 = "{:>%d}" %d
                        print(txt1.format(x[:a]))
                        print("-",txt2.format(x[(a+1):]))
                        print("-"*(d+2))
                        e = b - c
                        print(txt1.format(e))
                else:
                    print("Error: Numbers must only contain digits.")
            else:
                print("Error: Operator must be '+' or '-'.")
    else:
         if len(problems)>5:
             print("Error: Too many problems.")
         else:
           for x in problems:
               if  "+" in x:
                   x = "".join(x.split())
                   a = x.find("+")
                   if x[:a].isdigit()==True and x[(a+1):].isdigit()==True:
                       b = int(x[:a])
                       c = int(x[(a+1):])
                       d = max(len(str(c)),len(str(b)))
                       k = d+2
                       if len(str(c))>4 or len(str(b))>4:
                           print("Error: Numbers cannot be more than four digits.")
                       else:
                           txt1 = "{:>%d}" %k
                           txt2 = "{:>%d}" %d

                           print(txt1.format(x[:a]))
                           print("+",txt2.format(x[(a+1):]))
                           print("-"*(d+2))
                           #e = b+c
                           #print(txt1.format(e))

                   else:
                       print("Error: Numbers must only contain digits.")

               elif  "-" in x:
                   x = "".join(x.split())
                   a = x.find("-")
                   if x[:a].isdigit()==True and x[(a+1):].isdigit()==True:
                       b = int(x[:a])
                       c = int(x[(a+1):])
                       d = max(len(str(c)),len(str(b)))
                       k = d+2
                       if len(str(c))>4 or len(str(b))>4:
                           print("Error: Numbers cannot be more than four digits.")
                       else:
                           txt1 = "{:>%d}" %k
                           txt2 = "{:>%d}" %d
                           print(txt1.format(x[:a]))
                           print("-",txt2.format(x[(a+1):]))
                           print("-"*(d+2))
                           #e = b - c
                           #print(txt1.format(e))
                   else:
                       print("Error: Numbers must only contain digits.")
               else:
                   print("Error: Operator must be '+' or '-'.")
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"],True)
#arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
