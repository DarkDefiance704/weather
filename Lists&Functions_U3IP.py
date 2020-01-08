def title(): # title function.
   print("U3IP CS119T-1904D-02 | Dolan Cherry")
#end Function

#universal values.
Hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
         "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
         "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]  # List of hours in a day
TempPerHour = []  # List of the temperatures per hour


def prompt_temp():

   t = 0  # Amount of hours in a day
   while t < 24:
      temp = (int(input("Enter in the temperature for hour " + str(t) + ": ")))  # this increases the hour value as it increases.
      if temp <= -50 and temp >= 130:  #Checking to see if value is too cold / hot for normal temps.
         while temp <= -50 and temp >= 130:  #Prompting a new answer.
            temp = (int(input("Enter in the temperature for hour " + str(t) + ": ")))
      elif temp <= -50:
         print("Error Temperature too low. Please enter a new temperature between -50F and 130F.")
         while temp <= -50 and temp >= 130:  #Prompting a new answer.
            temp = (int(input("Enter in the temperature for hour " + str(t) + ": ")))
      elif temp >= 130:
         print("Error Temperature too high. Please enter a new temperature between -50F and 130F.")
         while temp <= -50 and temp >= 130:  #Prompting a new answer.
            temp = (int(input("Enter in the temperature for hour " + str(t) + ": ")))
      else:
         TempPerHour.append((temp))  # adding temp as a number
         print("You've entered " + str(temp) + '\n')  # confirming the value provided.
         t += 1
##end function

def Layout():
   str(TempPerHour)
   print(('Time \t Temperature'))
   for (h, p) in zip(Hours, (TempPerHour)): #should print the list in two columns with a tab between.
      print(h, '\t', p)

   average_temp = (sum(TempPerHour) / len(TempPerHour))  # taking the sum of the list divided by the length of the list.

   print("The Average Temperature is: " + str(round(average_temp, 2)))  # rounds the number to the 2nd or thousandth decimal place.
   print("The Highest Temperature is: " + str(max(TempPerHour)))
   print("The Lowest Temperature is: " + str(min(TempPerHour)))
#end function

#Begin Run
title()
prompt_temp()
Layout()
