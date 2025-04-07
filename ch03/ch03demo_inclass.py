##===================================================
## The following clears the screen before code runs
print('\033c\n')
##===================================================

# ask for the song
song_title = input("Enter the song title: ")

# ask for the sales
sales = int(input("Enter the sales: "))

print(song_title,end=" has ")
# determine and display status
if sales > 9999999:
    print("Diamond status")
elif sales > 1999999:
    print("Multi-platinum status")
elif sales > 999999:
    print("Platinum status")
elif sales > 499999:
    print("Gold status")
else:
    print("No status")