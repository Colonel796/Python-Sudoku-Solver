import Sudoku
import tkinter
import array as arr
import time


list = []
list.append(Sudoku.Sudoku(1, 1, 1, '', [1,2,3,4,5,6,7,8,9]))


#Solver Function
def solve():
   

    #Intiating Sudoku Class
    s1 = Sudoku.Sudoku(1, 1, 1, 0, [1,2,3,4,5,6,7,8,9])
    s2 = Sudoku.Sudoku(2, 1, 1, 0, [1,2,3,4,5,6,7,8,9])
    s3 = Sudoku.Sudoku(3, 1, 1, 0, [1,2,3,4,5,6,7,8,9])
    s4 = Sudoku.Sudoku(4, 1, 2, 0, [1,2,3,4,5,6,7,8,9])
    s5 = Sudoku.Sudoku(5, 1, 2, 0, [1,2,3,4,5,6,7,8,9])
    s6 = Sudoku.Sudoku(6, 1, 2, 0, [1,2,3,4,5,6,7,8,9])
    s7 = Sudoku.Sudoku(7, 1, 3, 0, [1,2,3,4,5,6,7,8,9])
    s8 = Sudoku.Sudoku(8, 1, 3, 0, [1,2,3,4,5,6,7,8,9])
    s9 = Sudoku.Sudoku(9, 1, 3, 0, [1,2,3,4,5,6,7,8,9])
    s21 = Sudoku.Sudoku(1, 2, 1, 0, [1,2,3,4,5,6,7,8,9])
    s22 = Sudoku.Sudoku(2, 2, 1, 0, [1,2,3,4,5,6,7,8,9])
    s23 = Sudoku.Sudoku(3, 2, 1, 0, [1,2,3,4,5,6,7,8,9])
    s24 = Sudoku.Sudoku(4, 2, 2, 0, [1,2,3,4,5,6,7,8,9])
    s25 = Sudoku.Sudoku(5, 2, 2, 0, [1,2,3,4,5,6,7,8,9])
    s26 = Sudoku.Sudoku(6, 2, 2, 0, [1,2,3,4,5,6,7,8,9])
    s27 = Sudoku.Sudoku(7, 2, 3, 0, [1,2,3,4,5,6,7,8,9])
    s28 = Sudoku.Sudoku(8, 2, 3, 0, [1,2,3,4,5,6,7,8,9])
    s29 = Sudoku.Sudoku(9, 2, 3, 0, [1,2,3,4,5,6,7,8,9])
    s31 = Sudoku.Sudoku(1, 3, 1, 0, [1,2,3,4,5,6,7,8,9])
    s32 = Sudoku.Sudoku(2, 3, 1, 0, [1,2,3,4,5,6,7,8,9])
    s33 = Sudoku.Sudoku(3, 3, 1, 0, [1,2,3,4,5,6,7,8,9])
    s34 = Sudoku.Sudoku(4, 3, 2, 0, [1,2,3,4,5,6,7,8,9])
    s35 = Sudoku.Sudoku(5, 3, 2, 0, [1,2,3,4,5,6,7,8,9])
    s36 = Sudoku.Sudoku(6, 3, 2, 0, [1,2,3,4,5,6,7,8,9])
    s37 = Sudoku.Sudoku(7, 3, 3, 0, [1,2,3,4,5,6,7,8,9])
    s38 = Sudoku.Sudoku(8, 3, 3, 0, [1,2,3,4,5,6,7,8,9])
    s39 = Sudoku.Sudoku(9, 3, 3, 0, [1,2,3,4,5,6,7,8,9])
    s41 = Sudoku.Sudoku(1, 4, 4, 0, [1,2,3,4,5,6,7,8,9])
    s42 = Sudoku.Sudoku(2, 4, 4, 0, [1,2,3,4,5,6,7,8,9])
    s43 = Sudoku.Sudoku(3, 4, 4, 0, [1,2,3,4,5,6,7,8,9])
    s44 = Sudoku.Sudoku(4, 4, 5, 0, [1,2,3,4,5,6,7,8,9])
    s45 = Sudoku.Sudoku(5, 4, 5, 0, [1,2,3,4,5,6,7,8,9])
    s46 = Sudoku.Sudoku(6, 4, 5, 0, [1,2,3,4,5,6,7,8,9])
    s47 = Sudoku.Sudoku(7, 4, 6, 0, [1,2,3,4,5,6,7,8,9])
    s48 = Sudoku.Sudoku(8, 4, 6, 0, [1,2,3,4,5,6,7,8,9])
    s49 = Sudoku.Sudoku(9, 4, 6, 0, [1,2,3,4,5,6,7,8,9])
    s51 = Sudoku.Sudoku(1, 5, 4, 0, [1,2,3,4,5,6,7,8,9])
    s52 = Sudoku.Sudoku(2, 5, 4, 0, [1,2,3,4,5,6,7,8,9])
    s53 = Sudoku.Sudoku(3, 5, 4, 0, [1,2,3,4,5,6,7,8,9])
    s54 = Sudoku.Sudoku(4, 5, 5, 0, [1,2,3,4,5,6,7,8,9])
    s55 = Sudoku.Sudoku(5, 5, 5, 0, [1,2,3,4,5,6,7,8,9])
    s56 = Sudoku.Sudoku(6, 5, 5, 0, [1,2,3,4,5,6,7,8,9])
    s57 = Sudoku.Sudoku(7, 5, 6, 0, [1,2,3,4,5,6,7,8,9])
    s58 = Sudoku.Sudoku(8, 5, 6, 0, [1,2,3,4,5,6,7,8,9])
    s59 = Sudoku.Sudoku(9, 5, 6, 0, [1,2,3,4,5,6,7,8,9])
    s61 = Sudoku.Sudoku(1, 6, 4, 0, [1,2,3,4,5,6,7,8,9])
    s62 = Sudoku.Sudoku(2, 6, 4, 0, [1,2,3,4,5,6,7,8,9])
    s63 = Sudoku.Sudoku(3, 6, 4, 0, [1,2,3,4,5,6,7,8,9])
    s64 = Sudoku.Sudoku(4, 6, 5, 0, [1,2,3,4,5,6,7,8,9])
    s65 = Sudoku.Sudoku(5, 6, 5, 0, [1,2,3,4,5,6,7,8,9])
    s66 = Sudoku.Sudoku(6, 6, 5, 0, [1,2,3,4,5,6,7,8,9])
    s67 = Sudoku.Sudoku(7, 6, 6, 0, [1,2,3,4,5,6,7,8,9])
    s68 = Sudoku.Sudoku(8, 6, 6, 0, [1,2,3,4,5,6,7,8,9])
    s69 = Sudoku.Sudoku(9, 6, 6, 0, [1,2,3,4,5,6,7,8,9])
    s71 = Sudoku.Sudoku(1, 7, 7, 0, [1,2,3,4,5,6,7,8,9])
    s72 = Sudoku.Sudoku(2, 7, 7, 0, [1,2,3,4,5,6,7,8,9])
    s73 = Sudoku.Sudoku(3, 7, 7, 0, [1,2,3,4,5,6,7,8,9])
    s74 = Sudoku.Sudoku(4, 7, 8, 0, [1,2,3,4,5,6,7,8,9])
    s75 = Sudoku.Sudoku(5, 7, 8, 0, [1,2,3,4,5,6,7,8,9])
    s76 = Sudoku.Sudoku(6, 7, 8, 0, [1,2,3,4,5,6,7,8,9])
    s77 = Sudoku.Sudoku(7, 7, 9, 0, [1,2,3,4,5,6,7,8,9])
    s78 = Sudoku.Sudoku(8, 7, 9, 0, [1,2,3,4,5,6,7,8,9])
    s79 = Sudoku.Sudoku(9, 7, 9, 0, [1,2,3,4,5,6,7,8,9])
    s81 = Sudoku.Sudoku(1, 8, 7, 0, [1,2,3,4,5,6,7,8,9])
    s82 = Sudoku.Sudoku(2, 8, 7, 0, [1,2,3,4,5,6,7,8,9])
    s83 = Sudoku.Sudoku(3, 8, 7, 0, [1,2,3,4,5,6,7,8,9])
    s84 = Sudoku.Sudoku(4, 8, 8, 0, [1,2,3,4,5,6,7,8,9])
    s85 = Sudoku.Sudoku(5, 8, 8, 0, [1,2,3,4,5,6,7,8,9])
    s86 = Sudoku.Sudoku(6, 8, 8, 0, [1,2,3,4,5,6,7,8,9])
    s87 = Sudoku.Sudoku(7, 8, 9, 0, [1,2,3,4,5,6,7,8,9])
    s88 = Sudoku.Sudoku(8, 8, 9, 0, [1,2,3,4,5,6,7,8,9])
    s89 = Sudoku.Sudoku(9, 8, 9, 0, [1,2,3,4,5,6,7,8,9])
    s91 = Sudoku.Sudoku(1, 9, 7, 0, [1,2,3,4,5,6,7,8,9])
    s92 = Sudoku.Sudoku(2, 9, 7, 0, [1,2,3,4,5,6,7,8,9])
    s93 = Sudoku.Sudoku(3, 9, 7, 0, [1,2,3,4,5,6,7,8,9])
    s94 = Sudoku.Sudoku(4, 9, 8, 0, [1,2,3,4,5,6,7,8,9])
    s95 = Sudoku.Sudoku(5, 9, 8, 0, [1,2,3,4,5,6,7,8,9])
    s96 = Sudoku.Sudoku(6, 9, 8, 0, [1,2,3,4,5,6,7,8,9])
    s97 = Sudoku.Sudoku(7, 9, 9, 0, [1,2,3,4,5,6,7,8,9])
    s98 = Sudoku.Sudoku(8, 9, 9, 0, [1,2,3,4,5,6,7,8,9])
    s99 = Sudoku.Sudoku(9, 9, 9, 0, [1,2,3,4,5,6,7,8,9])



    s1.number = e1.get()
    s2.number = e2.get()
    s3.number = e3.get()
    s4.number = e4.get()
    s5.number = e5.get()
    s6.number = e6.get()
    s7.number = e7.get()
    s8.number = e8.get()
    s9.number = e9.get()
    s21.number = e21.get()
    s22.number = e22.get()
    s23.number = e23.get()
    s24.number = e24.get()
    s25.number = e25.get()
    s26.number = e26.get()
    s27.number = e27.get()
    s28.number = e28.get()
    s29.number = e29.get()
    s31.number = e31.get()
    s32.number = e32.get()
    s33.number = e33.get()
    s34.number = e34.get()
    s35.number = e35.get()
    s36.number = e36.get()
    s37.number = e37.get()
    s38.number = e38.get()
    s39.number = e39.get()
    s41.number = e41.get()
    s42.number = e42.get()
    s43.number = e43.get()
    s44.number = e44.get()
    s45.number = e45.get()
    s46.number = e46.get()
    s47.number = e47.get()
    s48.number = e48.get()
    s49.number = e49.get()
    s51.number = e51.get()
    s52.number = e52.get()
    s53.number = e53.get()
    s54.number = e54.get()
    s55.number = e55.get()
    s56.number = e56.get()
    s57.number = e57.get()
    s58.number = e58.get()
    s59.number = e59.get()
    s61.number = e61.get()
    s62.number = e62.get()
    s63.number = e63.get()
    s64.number = e64.get()
    s65.number = e65.get()
    s66.number = e66.get()
    s67.number = e67.get()
    s68.number = e68.get()
    s69.number = e69.get()
    s71.number = e71.get()
    s72.number = e72.get()
    s73.number = e73.get()
    s74.number = e74.get()
    s75.number = e75.get()
    s76.number = e76.get()
    s77.number = e77.get()
    s78.number = e78.get()
    s79.number = e79.get()
    s81.number = e81.get()
    s82.number = e82.get()
    s83.number = e83.get()
    s84.number = e84.get()
    s85.number = e85.get()
    s86.number = e86.get()
    s87.number = e87.get()
    s88.number = e88.get()
    s89.number = e89.get()
    s91.number = e91.get()
    s92.number = e92.get()
    s93.number = e93.get()
    s94.number = e94.get()
    s95.number = e95.get()
    s96.number = e96.get()
    s97.number = e97.get()
    s98.number = e98.get()
    s99.number = e99.get()


    #Creating the list of Sudoku Values
    if(isinstance(list[0].number, str)):

        list[0] = s1
        list.append(s2)
        list.append(s3)
        list.append(s4)
        list.append(s5)
        list.append(s6)
        list.append(s7)
        list.append(s8)
        list.append(s9)
        list.append(s21)
        list.append(s22)
        list.append(s23)
        list.append(s24)
        list.append(s25)
        list.append(s26)
        list.append(s27)
        list.append(s28)
        list.append(s29)
        list.append(s31)
        list.append(s32)
        list.append(s33)
        list.append(s34)
        list.append(s35)
        list.append(s36)
        list.append(s37)
        list.append(s38)
        list.append(s39)
        list.append(s41)
        list.append(s42)
        list.append(s43)
        list.append(s44)
        list.append(s45)
        list.append(s46)
        list.append(s47)
        list.append(s48)
        list.append(s49)
        list.append(s51)
        list.append(s52)
        list.append(s53)
        list.append(s54)
        list.append(s55)
        list.append(s56)
        list.append(s57)
        list.append(s58)
        list.append(s59)
        list.append(s61)
        list.append(s62)
        list.append(s63)
        list.append(s64)
        list.append(s65)
        list.append(s66)
        list.append(s67)
        list.append(s68)
        list.append(s69)
        list.append(s71)
        list.append(s72)
        list.append(s73)
        list.append(s74)
        list.append(s75)
        list.append(s76)
        list.append(s77)
        list.append(s78)
        list.append(s79)
        list.append(s81)
        list.append(s82)
        list.append(s83)
        list.append(s84)
        list.append(s85)
        list.append(s86)
        list.append(s87)
        list.append(s88)
        list.append(s89)
        list.append(s91)
        list.append(s92)
        list.append(s93)
        list.append(s94)
        list.append(s95)
        list.append(s96)
        list.append(s97)
        list.append(s98)
        list.append(s99)

    else:

        list[0] = s1 
        list[1] = s2
        list[2] = s3
        list[3] = s4
        list[4] = s5
        list[5] = s6
        list[6] = s7
        list[7] = s8
        list[8] = s9
        list[9] = s21
        list[10] = s22
        list[11] = s23
        list[12] = s24
        list[13] = s25
        list[14] = s26
        list[15] = s27
        list[16] = s28
        list[17] = s29
        list[18] = s31
        list[19] = s32
        list[20] = s33 
        list[21] = s34
        list[22] = s35
        list[23] = s36
        list[24] = s37
        list[25] = s38
        list[26] = s39
        list[27] = s41
        list[28] = s42
        list[29] = s43
        list[30] = s44
        list[31] = s45
        list[32] = s46
        list[33] = s47
        list[34] = s48
        list[35] = s49
        list[36] = s51
        list[37] = s52
        list[38] = s53
        list[39] = s54
        list[40] = s55
        list[41] = s56
        list[42] = s57 
        list[43] = s58
        list[44] = s59
        list[45] = s61
        list[46] = s62
        list[47] = s63
        list[48] = s64
        list[49] = s65
        list[50] = s66
        list[51] = s67
        list[52] = s68
        list[53] = s69
        list[54] = s71
        list[55] = s72
        list[56] = s73
        list[57] = s74
        list[58] = s75
        list[59] = s76
        list[60] = s77
        list[61] = s78
        list[62] = s79
        list[63] = s81
        list[64] = s82
        list[65] = s83 
        list[66] = s84
        list[67] = s85
        list[68] = s86
        list[69] = s87
        list[70] = s88
        list[71] = s89
        list[72] = s91
        list[73] = s92
        list[74] = s93
        list[75] = s94
        list[76] = s95
        list[77] = s96
        list[78] = s97
        list[79] = s98
        list[80] = s99



    #Make sure the numbers are 0
    for x in range(81):

        if(list[x].number == '' ):

            list[x].number = 0

        else:

            list[x].number = int(list[x].number)
            list[x].possible = []

    #Clear possibles with numbers that are not zero
    for x in range(81):

        if(list[x].number > 0):

            list[x].possible = []
  
    #Checks possible against rules
    def findPossible(current):
        
        if(current.number > 0):

            return current.possible

        else:
            column = current.column
            row = current.row
            quad = current.quad

            possible = current.possible

            for x in range(81):

                if(list[x].number == 0):
            
                    list[x]
             
                elif(list[x].column == column and ( 1 <= possible.count(list[x].number))):
            
                    possible.remove(list[x].number)

                elif(list[x].row == row and ( 1 <= possible.count(list[x].number))):

                    possible.remove(list[x].number)

                elif(list[x].quad == quad and ( 1 <= possible.count(list[x].number))):

                    possible.remove(list[x].number)
    
            return possible


    #find all current possibles
    def CurrentPossible():
        
        for y in range(81):

            if(list[y].number > 0):

                list[y].possible = []

            else:

                list[y].possible = findPossible(list[y])


    #Solves the initial parts of the problem
    def initialSolve():

        CurrentPossible()

        checkVar = 1

        while checkVar > 0:

                checkVar = 0

                for z in range(81):

                    if(list[z].number > 0):

                        list[z].possible = []

                    if(list[z].possible == []):

                        checkVar

                    elif(len(list[z].possible) == 1):

                        list[z].number = list[z].possible[0]
                        list[z].possible = []
                        checkVar = checkVar + 1

                CurrentPossible()



    def ruleCheck(check):

        if(check.number > 0):

                for x in range(81):

                    if((check.column == list[x].column and check.row == list[x].row and check.quad == list[x].quad)):

                        check.number

                    elif(check.column == list[x].column or check.row == list[x].row or check.quad == list[x].quad):

                        if(check.number == list[x].number):
     
                                return False
        return True

    orgList = []

    def resetPossible():

            for x in range(81):

                list[x].possible = orgList[x].copy()


    #Backtracking part:
    def backTracking():

        completed = []

        for x in range(81):

            orgList.append([1,2,3,4,5,6,7,8,9])    
            orgList[x] = list[x].possible.copy()
    
    
        y = 0 
        while y < 81:

            if(list[y].possible == [] and list[y].number == 0):

                list[y].possible = orgList[y].copy()
                y = completed.pop()
                list[y].possible.remove(list[y].number)

                if(list[y].number > 0 and list[y].possible == []):

                    list[y].number = 0

                else:
                    temp = 0
                    while temp < 1:
              
                       list[y].number = list[y].possible[temp]

                       if(ruleCheck(list[y])):

                            completed.append(y)
                            list[y].number = list[y].possible[0]
                            y = y + 1
                            temp = 1

                       else:

                           list[y].possible.remove(list[y].number)

                           if(list[y].possible == []):

                               list[y].number = 0
                               temp = 1
                               y = y



            elif(list[y].number == 0):

                temp = 0
                while temp < 1:

              
                   list[y].number = list[y].possible[temp]

                   if(ruleCheck(list[y])):

                        completed.append(y)
                        list[y].number = list[y].possible[0]
                        y = y + 1
                        temp = 1

                   else:

                       list[y].possible.remove(list[y].number)

                       if(list[y].possible == []):

                           list[y].number = 0
                           temp = 1
                           y = y


            else:

                y = y + 1
    
    
    t0 = time.clock()

    initialSolve()

    #check if initialSolve solves the problem.
    temp = 0
    for x in range(81):

        if(list[x].number == 0):

            temp = 1

    if(temp == 1 and x >= 80):

        backTracking()
        tkinter.Label(m, text= 'Solved with Backtracking').grid(row=22, column=1,  columnspan = 10)

    if(temp == 0):

         tkinter.Label(m, text= 'Solved without Backtracking').grid(row=22, column=1,  columnspan = 10)

    t1 = time.clock()
    total = t1 - t0
    total = round(total, 5)

    tkinter.Label(m, text= 'Time to solve:').grid(row=23, column=1,  columnspan = 4)
    tkinter.Label(m, text= total).grid(row=23, column=5,  columnspan = 3)
    tkinter.Label(m, text= 'seconds').grid(row=23, column=8,  columnspan = 3)


    tkinter.Label(m, text= list[0].number, bg = 'grey', width = 2).grid(row=12, column=1)
    tkinter.Label(m, text= list[1].number, bg = 'grey', width = 2).grid(row=13, column=1)
    tkinter.Label(m, text= list[2].number, bg = 'grey', width = 2).grid(row=14, column=1)
    tkinter.Label(m, text= list[3].number).grid(row=15, column=1)
    tkinter.Label(m, text= list[4].number).grid(row=16, column=1)
    tkinter.Label(m, text= list[5].number).grid(row=17, column=1)
    tkinter.Label(m, text= list[6].number, bg = 'grey', width = 2).grid(row=18, column=1)
    tkinter.Label(m, text= list[7].number, bg = 'grey', width = 2).grid(row=19, column=1)
    tkinter.Label(m, text= list[8].number, bg = 'grey', width = 2).grid(row=20, column=1)
    tkinter.Label(m, text= list[9].number, bg = 'grey', width = 2).grid(row=12, column=2)
    tkinter.Label(m, text= list[10].number, bg = 'grey', width = 2).grid(row=13, column=2)
    tkinter.Label(m, text= list[11].number, bg = 'grey', width = 2).grid(row=14, column=2)
    tkinter.Label(m, text= list[12].number).grid(row=15, column=2)
    tkinter.Label(m, text= list[13].number).grid(row=16, column=2)
    tkinter.Label(m, text= list[14].number).grid(row=17, column=2)
    tkinter.Label(m, text= list[15].number, bg = 'grey', width = 2).grid(row=18, column=2)
    tkinter.Label(m, text= list[16].number, bg = 'grey', width = 2).grid(row=19, column=2)
    tkinter.Label(m, text= list[17].number, bg = 'grey', width = 2).grid(row=20, column=2)
    tkinter.Label(m, text= list[18].number, bg = 'grey', width = 2).grid(row=12, column=3)
    tkinter.Label(m, text= list[19].number, bg = 'grey', width = 2).grid(row=13, column=3)
    tkinter.Label(m, text= list[20].number, bg = 'grey', width = 2).grid(row=14, column=3)
    tkinter.Label(m, text= list[21].number).grid(row=15, column=3)
    tkinter.Label(m, text= list[22].number).grid(row=16, column=3)
    tkinter.Label(m, text= list[23].number).grid(row=17, column=3)
    tkinter.Label(m, text= list[24].number, bg = 'grey', width = 2).grid(row=18, column=3)
    tkinter.Label(m, text= list[25].number, bg = 'grey', width = 2).grid(row=19, column=3)
    tkinter.Label(m, text= list[26].number, bg = 'grey', width = 2).grid(row=20, column=3)
    tkinter.Label(m, text= list[27].number).grid(row=12, column=4)
    tkinter.Label(m, text= list[28].number).grid(row=13, column=4)
    tkinter.Label(m, text= list[29].number).grid(row=14, column=4)
    tkinter.Label(m, text= list[30].number, bg = 'grey', width = 2).grid(row=15, column=4)
    tkinter.Label(m, text= list[31].number, bg = 'grey', width = 2).grid(row=16, column=4)
    tkinter.Label(m, text= list[32].number, bg = 'grey', width = 2).grid(row=17, column=4)
    tkinter.Label(m, text= list[33].number).grid(row=18, column=4)
    tkinter.Label(m, text= list[34].number).grid(row=19, column=4)
    tkinter.Label(m, text= list[35].number).grid(row=20, column=4)
    tkinter.Label(m, text= list[36].number).grid(row=12, column=5)
    tkinter.Label(m, text= list[37].number).grid(row=13, column=5)
    tkinter.Label(m, text= list[38].number).grid(row=14, column=5)
    tkinter.Label(m, text= list[39].number, bg = 'grey', width = 2).grid(row=15, column=5)
    tkinter.Label(m, text= list[40].number, bg = 'grey', width = 2).grid(row=16, column=5)
    tkinter.Label(m, text= list[41].number, bg = 'grey', width = 2).grid(row=17, column=5)
    tkinter.Label(m, text= list[42].number).grid(row=18, column=5)
    tkinter.Label(m, text= list[43].number).grid(row=19, column=5)
    tkinter.Label(m, text= list[44].number).grid(row=20, column=5)
    tkinter.Label(m, text= list[45].number).grid(row=12, column=6)
    tkinter.Label(m, text= list[46].number).grid(row=13, column=6)
    tkinter.Label(m, text= list[47].number).grid(row=14, column=6)
    tkinter.Label(m, text= list[48].number, bg = 'grey', width = 2).grid(row=15, column=6)
    tkinter.Label(m, text= list[49].number, bg = 'grey', width = 2).grid(row=16, column=6)
    tkinter.Label(m, text= list[50].number, bg = 'grey', width = 2).grid(row=17, column=6)
    tkinter.Label(m, text= list[51].number).grid(row=18, column=6)
    tkinter.Label(m, text= list[52].number).grid(row=19, column=6)
    tkinter.Label(m, text= list[53].number).grid(row=20, column=6)
    tkinter.Label(m, text= list[54].number, bg = 'grey', width = 2).grid(row=12, column=7)
    tkinter.Label(m, text= list[55].number, bg = 'grey', width = 2).grid(row=13, column=7)
    tkinter.Label(m, text= list[56].number, bg = 'grey', width = 2).grid(row=14, column=7)
    tkinter.Label(m, text= list[57].number).grid(row=15, column=7)
    tkinter.Label(m, text= list[58].number).grid(row=16, column=7)
    tkinter.Label(m, text= list[59].number).grid(row=17, column=7)
    tkinter.Label(m, text= list[60].number, bg = 'grey', width = 2).grid(row=18, column=7)
    tkinter.Label(m, text= list[61].number, bg = 'grey', width = 2).grid(row=19, column=7)
    tkinter.Label(m, text= list[62].number, bg = 'grey', width = 2).grid(row=20, column=7)
    tkinter.Label(m, text= list[63].number, bg = 'grey', width = 2).grid(row=12, column=8)
    tkinter.Label(m, text= list[64].number, bg = 'grey', width = 2).grid(row=13, column=8)
    tkinter.Label(m, text= list[65].number, bg = 'grey', width = 2).grid(row=14, column=8)
    tkinter.Label(m, text= list[66].number).grid(row=15, column=8)
    tkinter.Label(m, text= list[67].number).grid(row=16, column=8)
    tkinter.Label(m, text= list[68].number).grid(row=17, column=8)
    tkinter.Label(m, text= list[69].number, bg = 'grey', width = 2).grid(row=18, column=8)
    tkinter.Label(m, text= list[70].number, bg = 'grey', width = 2).grid(row=19, column=8)
    tkinter.Label(m, text= list[71].number, bg = 'grey', width = 2).grid(row=20, column=8)
    tkinter.Label(m, text= list[72].number, bg = 'grey', width = 2).grid(row=12, column=9)
    tkinter.Label(m, text= list[73].number, bg = 'grey', width = 2).grid(row=13, column=9)
    tkinter.Label(m, text= list[74].number, bg = 'grey', width = 2).grid(row=14, column=9)
    tkinter.Label(m, text= list[75].number).grid(row=15, column=9)
    tkinter.Label(m, text= list[76].number).grid(row=16, column=9)
    tkinter.Label(m, text= list[77].number).grid(row=17, column=9)
    tkinter.Label(m, text= list[78].number, bg = 'grey', width = 2).grid(row=18, column=9)
    tkinter.Label(m, text= list[79].number, bg = 'grey', width = 2).grid(row=19, column=9)
    tkinter.Label(m, text= list[80].number, bg = 'grey', width = 2).grid(row=20, column=9)


   


#GUI Code
#########
m = tkinter.Tk() 

m.title('Sudoku Solver') 
button = tkinter.Button(m, text='Stop', width=10, command=m.destroy) 
button.grid( column = 6, columnspan = 5, row = 10) 
 
button = tkinter.Button(m, text='Slove', width=10, command=solve) 
button.grid(column = 1, columnspan = 5, row = 10) 


#Row Labels
tkinter.Label(m, text='1').grid(row=1) 
tkinter.Label(m, text='2').grid(row=2) 
tkinter.Label(m, text='3').grid(row=3) 
tkinter.Label(m, text='4').grid(row=4) 
tkinter.Label(m, text='5').grid(row=5) 
tkinter.Label(m, text='6').grid(row=6) 
tkinter.Label(m, text='7').grid(row=7) 
tkinter.Label(m, text='8').grid(row=8)
tkinter.Label(m, text='9').grid(row=9) 

#Column Labels
tkinter.Label(m, text='1').grid(row=0, column=1) 
tkinter.Label(m, text='2').grid(row=0, column=2) 
tkinter.Label(m, text='3').grid(row=0, column=3) 
tkinter.Label(m, text='4').grid(row=0, column=4) 
tkinter.Label(m, text='5').grid(row=0, column=5) 
tkinter.Label(m, text='6').grid(row=0, column=6) 
tkinter.Label(m, text='7').grid(row=0,column=7) 
tkinter.Label(m, text='8').grid(row=0,column=8)
tkinter.Label(m, text='9').grid(row=0,column=9) 

#Column Spacer
tkinter.Label(m, text='  ').grid(row=0, column=10) 
tkinter.Label(m, text='  ').grid(row=1, column=10) 
tkinter.Label(m, text='  ').grid(row=2, column=10) 
tkinter.Label(m, text='  ').grid(row=3, column=10) 
tkinter.Label(m, text='  ').grid(row=4, column=10) 
tkinter.Label(m, text='  ').grid(row=5, column=10) 
tkinter.Label(m, text='  ').grid(row=6,column=10) 
tkinter.Label(m, text='  ').grid(row=7,column=10)
tkinter.Label(m, text='  ').grid(row=8,column=10) 


#First column
e1 = tkinter.Entry(m) 
e2 = tkinter.Entry(m)
e3 = tkinter.Entry(m) 
e4 = tkinter.Entry(m)
e5 = tkinter.Entry(m) 
e6 = tkinter.Entry(m)
e7 = tkinter.Entry(m) 
e8 = tkinter.Entry(m)
e9 = tkinter.Entry(m) 
e1.grid(row=1, column=1) 
e2.grid(row=2, column=1)
e3.grid(row=3, column=1) 
e4.grid(row=4, column=1)
e5.grid(row=5, column=1) 
e6.grid(row=6, column=1)
e7.grid(row=7, column=1) 
e8.grid(row=8, column=1)
e9.grid(row=9, column=1) 

e1.config(width = 3)
e2.config(width = 3)
e3.config(width = 3) 
e4.config(width = 3)
e5.config(width = 3)
e6.config(width = 3)
e7.config(width = 3)
e8.config(width = 3)
e9.config(width = 3) 


e1.configure(bg = 'Grey')
e2.configure(bg = 'Grey')
e3.configure(bg = 'Grey')
e7.configure(bg = 'Grey')
e8.configure(bg = 'Grey')
e9.configure(bg = 'Grey')



#Second Column
e21 = tkinter.Entry(m) 
e22 = tkinter.Entry(m)
e23 = tkinter.Entry(m) 
e24 = tkinter.Entry(m)
e25 = tkinter.Entry(m) 
e26 = tkinter.Entry(m)
e27 = tkinter.Entry(m) 
e28 = tkinter.Entry(m)
e29 = tkinter.Entry(m) 
e21.grid(row=1, column=2) 
e22.grid(row=2, column=2)
e23.grid(row=3, column=2) 
e24.grid(row=4, column=2)
e25.grid(row=5, column=2) 
e26.grid(row=6, column=2)
e27.grid(row=7, column=2) 
e28.grid(row=8, column=2)
e29.grid(row=9, column=2) 


e21.config(width = 3)
e22.config(width = 3)
e23.config(width = 3) 
e24.config(width = 3)
e25.config(width = 3)
e26.config(width = 3)
e27.config(width = 3)
e28.config(width = 3)
e29.config(width = 3) 


e21.configure(bg = 'Grey')
e22.configure(bg = 'Grey')
e23.configure(bg = 'Grey')
e27.configure(bg = 'Grey')
e28.configure(bg = 'Grey')
e29.configure(bg = 'Grey')



#Thirdy Column
e31 = tkinter.Entry(m) 
e32 = tkinter.Entry(m)
e33 = tkinter.Entry(m) 
e34 = tkinter.Entry(m)
e35 = tkinter.Entry(m) 
e36 = tkinter.Entry(m)
e37 = tkinter.Entry(m) 
e38 = tkinter.Entry(m)
e39 = tkinter.Entry(m) 
e31.grid(row=1, column=3) 
e32.grid(row=2, column=3)
e33.grid(row=3, column=3) 
e34.grid(row=4, column=3)
e35.grid(row=5, column=3) 
e36.grid(row=6, column=3)
e37.grid(row=7, column=3) 
e38.grid(row=8, column=3)
e39.grid(row=9, column=3) 


e31.config(width = 3)
e32.config(width = 3)
e33.config(width = 3) 
e34.config(width = 3)
e35.config(width = 3)
e36.config(width = 3)
e37.config(width = 3)
e38.config(width = 3)
e39.config(width = 3) 


e31.configure(bg = 'Grey')
e32.configure(bg = 'Grey')
e33.configure(bg = 'Grey')
e37.configure(bg = 'Grey')
e38.configure(bg = 'Grey')
e39.configure(bg = 'Grey')



#Fourth Column
e41 = tkinter.Entry(m) 
e42 = tkinter.Entry(m)
e43 = tkinter.Entry(m) 
e44 = tkinter.Entry(m)
e45 = tkinter.Entry(m) 
e46 = tkinter.Entry(m)
e47 = tkinter.Entry(m) 
e48 = tkinter.Entry(m)
e49 = tkinter.Entry(m) 
e41.grid(row=1, column=4) 
e42.grid(row=2, column=4)
e43.grid(row=3, column=4) 
e44.grid(row=4, column=4)
e45.grid(row=5, column=4) 
e46.grid(row=6, column=4)
e47.grid(row=7, column=4) 
e48.grid(row=8, column=4)
e49.grid(row=9, column=4) 


e41.config(width = 3)
e42.config(width = 3)
e43.config(width = 3) 
e44.config(width = 3)
e45.config(width = 3)
e46.config(width = 3)
e47.config(width = 3)
e48.config(width = 3)
e49.config(width = 3) 

e44.configure(bg = 'Grey')
e45.configure(bg = 'Grey')
e46.configure(bg = 'Grey')



#Fifth Column
e51 = tkinter.Entry(m) 
e52 = tkinter.Entry(m)
e53 = tkinter.Entry(m) 
e54 = tkinter.Entry(m)
e55 = tkinter.Entry(m) 
e56 = tkinter.Entry(m)
e57 = tkinter.Entry(m) 
e58 = tkinter.Entry(m)
e59 = tkinter.Entry(m) 
e51.grid(row=1, column=5) 
e52.grid(row=2, column=5)
e53.grid(row=3, column=5) 
e54.grid(row=4, column=5)
e55.grid(row=5, column=5) 
e56.grid(row=6, column=5)
e57.grid(row=7, column=5) 
e58.grid(row=8, column=5)
e59.grid(row=9, column=5) 


e51.config(width = 3)
e52.config(width = 3)
e53.config(width = 3) 
e54.config(width = 3)
e55.config(width = 3)
e56.config(width = 3)
e57.config(width = 3)
e58.config(width = 3)
e59.config(width = 3) 

e54.configure(bg = 'Grey')
e55.configure(bg = 'Grey')
e56.configure(bg = 'Grey')



#Sixth Column
e61 = tkinter.Entry(m) 
e62 = tkinter.Entry(m)
e63 = tkinter.Entry(m) 
e64 = tkinter.Entry(m)
e65 = tkinter.Entry(m) 
e66 = tkinter.Entry(m)
e67 = tkinter.Entry(m) 
e68 = tkinter.Entry(m)
e69 = tkinter.Entry(m) 
e61.grid(row=1, column=6) 
e62.grid(row=2, column=6)
e63.grid(row=3, column=6) 
e64.grid(row=4, column=6)
e65.grid(row=5, column=6) 
e66.grid(row=6, column=6)
e67.grid(row=7, column=6) 
e68.grid(row=8, column=6)
e69.grid(row=9, column=6) 


e61.config(width = 3)
e62.config(width = 3)
e63.config(width = 3) 
e64.config(width = 3)
e65.config(width = 3)
e66.config(width = 3)
e67.config(width = 3)
e68.config(width = 3)
e69.config(width = 3) 


e64.configure(bg = 'Grey')
e65.configure(bg = 'Grey')
e66.configure(bg = 'Grey')



#Seventh Column
e71 = tkinter.Entry(m) 
e72 = tkinter.Entry(m)
e73 = tkinter.Entry(m) 
e74 = tkinter.Entry(m)
e75 = tkinter.Entry(m) 
e76 = tkinter.Entry(m)
e77 = tkinter.Entry(m) 
e78 = tkinter.Entry(m)
e79 = tkinter.Entry(m) 
e71.grid(row=1, column=7) 
e72.grid(row=2, column=7)
e73.grid(row=3, column=7) 
e74.grid(row=4, column=7)
e75.grid(row=5, column=7) 
e76.grid(row=6, column=7)
e77.grid(row=7, column=7) 
e78.grid(row=8, column=7)
e79.grid(row=9, column=7) 


e71.config(width = 3)
e72.config(width = 3)
e73.config(width = 3) 
e74.config(width = 3)
e75.config(width = 3)
e76.config(width = 3)
e77.config(width = 3)
e78.config(width = 3)
e79.config(width = 3) 


e71.configure(bg = 'Grey')
e72.configure(bg = 'Grey')
e73.configure(bg = 'Grey')
e77.configure(bg = 'Grey')
e78.configure(bg = 'Grey')
e79.configure(bg = 'Grey')



#Eighth Column
e81 = tkinter.Entry(m) 
e82 = tkinter.Entry(m)
e83 = tkinter.Entry(m) 
e84 = tkinter.Entry(m)
e85 = tkinter.Entry(m) 
e86 = tkinter.Entry(m)
e87 = tkinter.Entry(m) 
e88 = tkinter.Entry(m)
e89 = tkinter.Entry(m) 
e81.grid(row=1, column=8) 
e82.grid(row=2, column=8)
e83.grid(row=3, column=8) 
e84.grid(row=4, column=8)
e85.grid(row=5, column=8) 
e86.grid(row=6, column=8)
e87.grid(row=7, column=8) 
e88.grid(row=8, column=8)
e89.grid(row=9, column=8) 


e81.config(width = 3)
e82.config(width = 3)
e83.config(width = 3) 
e84.config(width = 3)
e85.config(width = 3)
e86.config(width = 3)
e87.config(width = 3)
e88.config(width = 3)
e89.config(width = 3) 


e81.configure(bg = 'Grey')
e82.configure(bg = 'Grey')
e83.configure(bg = 'Grey')
e87.configure(bg = 'Grey')
e88.configure(bg = 'Grey')
e89.configure(bg = 'Grey')



#Ninth Column
e91 = tkinter.Entry(m) 
e92 = tkinter.Entry(m)
e93 = tkinter.Entry(m) 
e94 = tkinter.Entry(m)
e95 = tkinter.Entry(m) 
e96 = tkinter.Entry(m)
e97 = tkinter.Entry(m) 
e98 = tkinter.Entry(m)
e99 = tkinter.Entry(m) 
e91.grid(row=1, column=9) 
e92.grid(row=2, column=9)
e93.grid(row=3, column=9) 
e94.grid(row=4, column=9)
e95.grid(row=5, column=9) 
e96.grid(row=6, column=9)
e97.grid(row=7, column=9) 
e98.grid(row=8, column=9)
e99.grid(row=9, column=9) 


e91.config(width = 3)
e92.config(width = 3)
e93.config(width = 3) 
e94.config(width = 3)
e95.config(width = 3)
e96.config(width = 3)
e97.config(width = 3)
e98.config(width = 3)
e99.config(width = 3) 


e91.configure(bg = 'Grey')
e92.configure(bg = 'Grey')
e93.configure(bg = 'Grey')
e97.configure(bg = 'Grey')
e98.configure(bg = 'Grey')
e99.configure(bg = 'Grey')


m.mainloop()