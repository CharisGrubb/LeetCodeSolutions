#   group_farmland_coordinates=[]
#         all_farmland_coordinates=[]
#         m = 0
#         while m < len(land):
#             n = 0 
#             while n<len(land[m]):
#                 if land[m][n]:
#                     all_farmland_coordinates.append((m,n))
#                 n+=1

#             m+=1
#         print('ALL FARMLAND',all_farmland_coordinates)

#         i = 0
#         while i<len(all_farmland_coordinates):
#             start_coor = all_farmland_coordinates[i]
#             j = 0
#             last_coor = all_farmland_coordinates.pop(i)
#             last_removed = None
#             while j< len(all_farmland_coordinates):
#                 if all_farmland_coordinates[j][0]== last_coor[0] or all_farmland_coordinates[j][1]==last_coor[1]:
#                     if all_farmland_coordinates[j][1]-last_coor[1] >1:
#                         print('Ignore ', all_farmland_coordinates[j])
#                         j+=1
#                         continue
#                     elif (all_farmland_coordinates[j][0] -last_coor[0]) >1:
#                         print('Ignore ', all_farmland_coordinates[j])
#                         j+=1
#                         continue
#                     last_coor = all_farmland_coordinates.pop(j)
#                     print('New last coor', last_coor, ' for ', start_coor)
#                 elif all_farmland_coordinates[j][0]==start_coor[0]: 
#                     last_removed = all_farmland_coordinates.pop(j) #Remove middle man
#                     print('REMOVE ', last_removed)
#                 elif all_farmland_coordinates[j][1]==start_coor[1] and abs(all_farmland_coordinates[j][1]-last_coor[1])<2:
#                     last_removed = all_farmland_coordinates.pop(j) #Remove middle man
#                     print('REMOVE ', last_removed)
#                 elif last_removed is not None and (all_farmland_coordinates[j][0]==last_removed[0]  or all_farmland_coordinates[j][1]==last_removed[1]):
#                     last_removed = all_farmland_coordinates.pop(j)
#                     print('Matches previous removed', last_removed)
#                 elif abs(all_farmland_coordinates[j][1]-last_coor[1])>1 and abs(all_farmland_coordinates[j][0]-last_coor[0])>1:
#                     print('Break the loop',all_farmland_coordinates[j])
#                     break
#                 else:
#                     print('Moving on')
#                     j+=1
#             print('COORDINATES',start_coor, last_coor)
#             group_farmland_coordinates.append([start_coor[0],start_coor[1],last_coor[0],last_coor[1]])
#             #i+=1
#         print(group_farmland_coordinates)

#         return group_farmland_coordinates
            
