

import re
#如果匹配成功，可以返回匹配成功的数据范围
#如果匹配失败，就返回None
#str.group属性代表了


#匹配，返回匹配的串和对应的文法符号
def match(str):

    grammer=None
    end = None

    #python中的换行符\会造成问题
    # 1 从加法运算符开始的各种符号匹配
    pattern = re.compile('(\+)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "PLUS"
        return end.group(),grammer

    pattern = re.compile('(\-)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "MINU"
        return end.group(), grammer

    pattern = re.compile('(\*)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "MULT"
        return end.group(), grammer

    pattern = re.compile('(/)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "DIV"
        return end.group(), grammer

    pattern = re.compile('(<=)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "LEQ"
        return end.group(), grammer

    pattern = re.compile('(<)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "LSS"
        return end.group(), grammer

    pattern = re.compile('(>=)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "GEQ"
        return end.group(), grammer

    pattern = re.compile('(>)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "GRE"
        return end.group(), grammer

    pattern = re.compile('(==)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "EQL"
        return end.group(), grammer

    pattern = re.compile('(!=)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "NEQ"
        return end.group(), grammer

    pattern = re.compile('(=)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "ASSIGN"
        return end.group(), grammer

    pattern = re.compile('(;)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "SEMICN"
        return end.group(), grammer

    pattern = re.compile('(,)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "COMMA"
        return end.group(), grammer

    pattern = re.compile('(\()')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "LPARENT"
        return end.group(), grammer

    pattern = re.compile('(\))')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "RPARENT"
        return end.group(), grammer

    pattern = re.compile('(\[)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "LBRACK"
        return end.group(), grammer

    pattern = re.compile('(\])')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "RBRACK"
        return end.group(), grammer

    pattern = re.compile('(\{)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "LBRACE"
        return end.group(), grammer

    pattern = re.compile('(\})')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "RBRACE"
        return end.group(), grammer

    pattern = re.compile('(\d+)')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "INTCON"
        return end.group(), grammer

    pattern = re.compile('(\'[^\']+\')')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "CHARCON"
        #去除首尾端字符
        end = end.group()
        return end, grammer

    pattern = re.compile('(\"[^\"]+\")')
    end = re.match(pattern, str)
    if (end != None):
        grammer = "STRCON"
        # 去除首尾端字符
        end = end.group()
        return end, grammer

    # 3 先匹配常量标识符，对于后缀里面有数字的要单独讨论
    pattern = re.compile('(const)|(int)|(char)|(void)|(main)|(if)|(else)|(do)|(while)|(for)|(scanf)|(printf)|(return)')
    end = re.match(pattern, str)
    if (end != None):
        end = end.group()
        grammer = end.upper()
        temp = "TK"
        grammer = grammer+temp
        #这个匹配成功，下面不成功，肯定为const
        #下面成功，且大于才是ident

    # 4 最后匹配标识符
    pattern = re.compile('[_a-zA-Z][_a-zA-Z0-9]*')
    grs = re.match(pattern, str)
    if(end==None and grs !=None):
        grammer = "IDENFR"
        end = grs.group()
    elif(end != None and grs != None):
        grs = grs.group()
        len1 = len(grs)
        len2 = len(end)
        if(len1>len2):
            grammer = "IDENFR"
            end = grs

    #当所有匹配都失败返回None
    return end,grammer





def mainFunc():
    """主函数"""
    ifile = open('testfile5.txt','rt')
    string = ifile.read()
    ifile.close()
    #打开读取了文件内容，然后关闭文件

    #输入字符串
    l1,l2 = getToken(string)
    return l1,l2



def getToken(str):
    result = None;

    #定义的词法列表和标识符列表
    lexcial_list =[]
    grammer_list =[]

    #当string不等于0就开始不断匹配
    while(str!=None):
        #每次匹配前消去空格

        pat = re.compile('\s*')  # 似乎消去了空格就可以了，没有考虑换行符
        kong = re.match(pat, str)
        if (kong != None):
            kong = kong.group()
            length = len(kong)
            str = str[length:]

        if (len(str) == 0):  # 通过是否等于0来判断这个时候str是不是None
            str = None
            break

        # 开始匹配1
        result,grammer = match(str)
        if result != None:
            # 先进行字符串裁剪
            length = len(result)
            str = str[length:]


            #这里输出的时候注意一下字符和字符串吧
            templen = len(result)
            if(result[0]=='\"' and result[templen-1]=='\"'):
                temp = len(result)
                result = result[1:temp-1]
            if(result[0]=='\'' and result[templen-1]=='\''):
                temp = len(result)
                result = result[1:temp - 1]

            #写入文本
            lexcial_list.append(result)
            grammer_list.append(grammer)



            if(len(str)==0):#通过是否等于0来判断这个时候str是不是None
                str = None

    #返回列表
    return lexcial_list,grammer_list



#建立一个词法分析器类
#初始化
#判断器
#分析方法，当str为0跳出
#分割线------------------------------------------------

p = 0

class gramAnly:
    def __init__(self):
        self.lookHead,self.gram= mainFunc()#两个都是列表
        self.lookHead.append("")
        self.lookHead.append("")
        self.ofile = open("output.txt",'w',encoding='utf-8')


    #输出词法分析的结果，并且得到下一个lookHead的值
    def _getToken(self):
        global p
        self.ofile.write("{} {}\n".format(self.gram[p],self.lookHead[p]))
        #print("{} {}".format(self.gram[p], self.lookHead[p]))
        p = p + 1


    def _match(self,str):
        if(self.lookHead[p]!=str):
            print("wrong")
            exit(0)
        else:
            self._getToken()


    def _matchIdent(self,ap):
        """专门用来匹配标识符"""
        if (self.gram[ap] == "IDENFR"):
            return True
        else:
            return False

    def _matchNZnumber(self,ap):
        """匹配非零数字"""
        pattern = re.compile('1-9')
        flag = re.match(pattern, self.lookHead[ap])
        if (flag != None):
            return True
        return False

    def _matchNumber(self,ap):
        """"匹配数字"""
        pattern = re.compile('0|([1-9][0-9]*)')
        flag = re.match(pattern, self.lookHead[ap])
        if (flag != None):
            return True
        return False

    def _matchLetter(self,ap):
        """匹配字母"""
        pattern = re.compile('_|a-z|A-Z')
        flag = re.match(pattern,self.lookHead[ap])
        if(flag != None):
            return True
        return False

    def _matchChar(self, ap):
        if (self.gram[ap] == "CHARCON"):
            return True
        else:
            return False

    def parseAdd(self):
        """加法"""
        if(self.lookHead[p]=="+"):
            self._match("+")
        elif(self.lookHead[p]=="-"):
            self._match("-")

    def parseMult(self):
        """乘法"""
        if (self.lookHead[p] == "*"):
            self._match("*")
        elif (self.lookHead[p] == "/"):
            self._match("/")

    def parseRealtion(self):
        """关系运算符"""
        if (self.lookHead[p] == "<"):
            self._match("<")
        elif (self.lookHead[p] == "<="):
            self._match("<=")
        elif (self.lookHead[p] == ">"):
            self._match(">")
        elif (self.lookHead[p] == ">="):
            self._match(">=")
        elif (self.lookHead[p] == "!="):
            self._match("!=")
        elif (self.lookHead[p] == "=="):
            self._match("==")


    def parseLetter(self):
        """字母"""
        pattern = re.compile('_|a-z|A-Z')
        flag = re.match(pattern,self.lookHead[p])
        if(flag != None):
            self._getToken()


    def parseNumber(self):
        "数字"
        if(self.lookHead[p]=="0"):
            self._match("0")
        else:
            pattern = re.compile('1-9')
            temp = self.lookHead[p]
            flag = re.match(pattern,temp)
            if(flag!=None):
                self.parseNotZeroNumber()

    def parseNotZeroNumber(self):
        "非零数字"
        pattern = re.compile('1-9')
        flag = re.match(pattern,self.lookHead)
        if(flag != None):
            self._getToken()

    def parseChar(self):
        """字符"""
        if (self._matchChar(p)):
            self._getToken()


    def parseString(self):
        """字符串"""
        pattern = re.compile('([\x20-\x21|\x23-\x7e]+)')
        flag = re.match(pattern,self.lookHead[p])
        if(flag==None):
            exit(0)
        else:
            self._getToken()
            self.ofile.write("<字符串>\n")

    def parseProgram(self):
        """程序"""
        if(self.lookHead[p]=='const'):
            self.parseConstDes()#

        if(self.lookHead[p]=="int" or self.lookHead[p]=="char"):
            if(self._matchIdent(p+1)):
                if(self.lookHead[p+2]==";" or self.lookHead[p+2]=="[" or self.lookHead[p+2]==","):
                    self.parseVariableDes()#

        while 1:
            if ((self.lookHead[p] == "int" or self.lookHead[p] == "char") and \
                self._matchIdent(p+1) and self.lookHead[p+2]=="(" ):

                    self.parseHaveReturnFuncDef()#

            elif(self.lookHead[p] == "void" and self._matchIdent(p+1) and \
                 self.lookHead[p+1]!="main" and self.lookHead[p+2]=="("):

                    self.parseNoReturnFuncdef()#
            else:
                break

        self.parseMainFunc()
        self.ofile.write("<程序>\n")

    def parseConstDes(self):#first const
        """常量说明"""
        self._match("const")
        self.parseConstDef()
        self._match(";")
        while 1:
            if(self.lookHead[p]=="const"):
                self._match("const")
                self.parseConstDef()
                self._match(";")

            else:
                break

        self.ofile.write("<常量说明>\n")

    def parseConstDef(self):
        """常量定义"""
        if(self.lookHead[p]=="int"):
            self._match("int")
            self.parseIdent()
            self._match("=")
            self.parseInteger()
            while 1:
                if(self.lookHead[p]==","):
                    self._match(",")
                    self.parseIdent()
                    self._match("=")
                    self.parseInteger()
                else:
                    break
        elif(self.lookHead[p]=="char"):
            self._match("char")
            self.parseIdent()
            self._match("=")
            self.parseChar()
            while 1:
                if (self.lookHead[p] == ","):
                    self._match(",")
                    self.parseIdent()
                    self._match("=")
                    self.parseChar()
                else:
                    break
        self.ofile.write("<常量定义>\n")

    def parseUnsignedInteger(self):
        """无符号整数"""
        if(self._matchNumber(p)):
            self._getToken()
            self.ofile.write("<无符号整数>\n")



    def parseInteger(self):
        """整数"""
        if(self.lookHead[p]=="+"):
            self._match("+")
        elif(self.lookHead[p] == "-"):
            self._match("-")
        self.parseUnsignedInteger()
        self.ofile.write("<整数>\n")


    def parseIdent(self):
        """标识符"""
        if(self._matchIdent(p)):
            self._getToken()

    def parseDesHead(self):
        """声明头部"""
        if(self.lookHead[p]=="int"):
            self._match("int")
            self.parseIdent()
        elif(self.lookHead[p]=="char"):
            self._match("char")
            self.parseIdent()
        self.ofile.write("<声明头部>\n")

    def parseVariableDes(self):#first: int or char
        """变量说明"""
        self.parseVariableDef()
        self._match(";")

        while 1:
            if(self.lookHead[p]=="int" or self.lookHead[p]=="char" ):
                if(self.lookHead[p+2]=="[" or self.lookHead[p+2]=="," or self.lookHead[p+2]==";"):
                    self.parseVariableDef()
                    self._match(";")
                else:
                    break
            else:
                break
        self.ofile.write("<变量说明>\n")

    def parseVariableDef(self):
        """变量定义"""

        self.parseTypeIdent()
        if(self._matchIdent(p)):
            if(self.lookHead[p+1]=="["):
                self.parseIdent()
                self._match("[")
                self.parseUnsignedInteger()
                self._match("]")
            else:
                self.parseIdent()
        while 1:
            if(self.lookHead[p]==","):
                self._match(",")
                if(self._matchIdent(p)):
                    if(self.lookHead[p+1]=="["):
                        self.parseIdent()
                        self._match("[")
                        self.parseUnsignedInteger()
                        self._match("]")
                    else:
                        self.parseIdent()
                else:
                    break
            else:
                break
        self.ofile.write("<变量定义>\n")

    def parseTypeIdent(self):
        """类型标识符"""
        if(self.lookHead[p]=="int"):
            self._match("int")
        elif(self.lookHead[p]=="char"):
            self._match("char")

    def parseHaveReturnFuncDef(self):
        """有返回值函数定义"""
        self.parseDesHead()
        self._match("(")
        self.parseParameterList()
        self._match(")")
        self._match("{")
        self.parseCompund()
        self._match("}")
        self.ofile.write("<有返回值函数定义>\n")


    def parseNoReturnFuncdef(self):
        """无返回值函数定义"""
        self._match("void")
        self.parseIdent()
        self._match("(")
        self.parseParameterList()
        self._match(")")
        self._match("{")
        self.parseCompund()
        self._match("}")
        self.ofile.write("<无返回值函数定义>\n")

    def parseCompund(self):
        """复合语句"""
        if(self.lookHead[p]=="const"):
            self.parseConstDes()#

        if(self.lookHead[p]=="int" or self.lookHead[p]=="char"):
            if(self._matchIdent(p+1)):
                if(self.lookHead[p+2]==";" or self.lookHead[p+2]=="[" or self.lookHead[p+2]==","):
                    self.parseVariableDes()#

        self.parseStenceCol()#
        self.ofile.write("<复合语句>\n")

    def parseParameterList(self):
        """参数表"""
        if(self.lookHead[p]=="int" or self.lookHead[p]=="char"):
            self.parseTypeIdent()
            self.parseIdent()
            while 1:
                if(self.lookHead[p]==","):
                    self._match(",")
                    self.parseTypeIdent()
                    self.parseIdent()
                    # if(self.lookHead[p]=="int" or self.lookHead[p] == "char"):
                    #     self.parseTypeIdent()
                    #     if(self._matchLetter()):
                    #         self.parseLetter()
                    #     else:
                    #         break
                    # else:
                    #     break
                else:
                    break
        elif(self.lookHead[p]==""):
            self.parseVoid()

        self.ofile.write("<参数表>\n")


    def parseMainFunc(self):
        """主函数"""
        self._match("void")
        self._match("main")
        self._match("(")
        self._match(")")
        self._match("{")
        self.parseCompund()
        self._match("}")

        #标亮部分输出
        self.ofile.write("<主函数>\n")


    def parseExpersion(self):
        """表达式"""
        if (self.gram[p] == "PLUS" and self.lookHead[p] == "+"):
            self._match("+")
        elif (self.gram[p] == "MINU" and self.lookHead[p] == "-"):
            self._match("-")

        self.parseItem()
        while 1:
            if(self.lookHead[p]=="+" or self.lookHead[p]=="-"):
                self.parseAdd()
                self.parseItem()
            else:
                break

        self.ofile.write("<表达式>\n")

    def parseItem(self):
        """项"""
        self.parseFactor()
        while 1:
            if(self.lookHead[p]=="*" or self.lookHead[p]=="/"):
                self.parseMult()
                self.parseFactor()
            else:
                break

        self.ofile.write("<项>\n")

#---------------留待-------------------
    def parseFactor(self):
        """因子"""
        if(self._matchIdent(p) and self.lookHead[p+1]=="["):
            self.parseIdent()
            self._match("[")
            self.parseExpersion()
            self._match("]")
        elif (self._matchIdent(p) and self.lookHead[p + 1] == "("):
            self.parseHaveReturnFuncCallStence()
        elif(self._matchIdent(p)):
            self.parseIdent()
        elif(self.lookHead[p]=="("):
            self._match("(")
            self.parseExpersion()
            self._match(")")
        elif (self._matchChar(p)):
            self.parseChar()
        elif(self.lookHead[p]=="+" or self.lookHead[p]=="-" or self._matchNumber(p)):
            self.parseInteger()


        self.ofile.write("<因子>\n")


    def parseStence(self):
        """语句"""

        if(self.lookHead[p]=="if"):
            self.parseCondationStence()
        elif(self.lookHead[p]=="while" or self.lookHead[p] == "do" or self.lookHead[p] == "for"):
            self.parseCircularStence()
        elif(self.lookHead[p]=="{"):
            self._match("{")
            self.parseStenceCol()
            self._match("}")
        elif (self.lookHead[p] == "scanf"):
            self.parseReadStence()
            self._match(";")
        elif (self.lookHead[p] == "printf"):
            self.parseWriteStence()
            self._match(";")
        elif (self.lookHead[p] == ";"):
            self._match(";")
        elif (self.lookHead[p] == "return"):
            self.parseHaveReturnStence()
            self._match(";")
        elif(self._matchIdent(p) and self.lookHead[p+1]=="("):
            if (self.lookHead[p - 1] == "="):
                self.parseHaveReturnFuncCallStence()
            else:
                self.parseNotHaveReturnFuncCallStence()
            self._match(";")
        elif(self._matchIdent(p) and (self.lookHead[p+1]=="=" or self.lookHead[p+1]=="[")):
            self.parseAssignStence()
            self._match(";")

        self.ofile.write("<语句>\n")

    def parseAssignStence(self):
        """赋值语句"""
        if(self._matchIdent(p) and self.lookHead[p+1]=="="):
            self.parseIdent()
            self._match("=")
            self.parseExpersion()
        elif(self._matchIdent(p) and self.lookHead[p+1]=="["):
            self.parseIdent()
            self._match("[")
            self.parseExpersion()
            self._match("]")
            self._match("=")
            self.parseExpersion()

        self.ofile.write("<赋值语句>\n")


    def parseCondationStence(self):
        """条件语句"""
        self._match("if")
        self._match("(")
        self.parseCondation()
        self._match(")")
        self.parseStence()
        if(self.lookHead[p]=="else"):
            if (self.lookHead[p+1] == "if" or self.lookHead[p+1] == "while" or \
                    self.lookHead[p+1] == "do" or self.lookHead[p+1] == "for" or \
                    self.lookHead[p+1] == "{" or (self._matchIdent(p+1) and \
                    self.lookHead[p + 2] == "(") or (self._matchIdent(p+1) and \
                    self.lookHead[p + 2] == "=") or \
                    self.lookHead[p+1] == "scanf" or self.lookHead[p+1] == "printf" or \
                    self.lookHead[p+1] == "" or self.lookHead[p+1] == "return"):
                self._match("else")
                self.parseStence()
        self.ofile.write("<条件语句>\n")


    def parseCondation(self):
        """条件"""
        self.parseExpersion()
        if(self.lookHead[p]=="<" or self.lookHead[p]=="<=" or \
            self.lookHead[p] == ">" or self.lookHead[p] == ">=" or \
            self.lookHead[p] == "!=" or self.lookHead[p] == "=="):
            self.parseRealtion()
            self.parseExpersion()

        self.ofile.write("<条件>\n")

    def parseCircularStence(self):
        """循环语句"""
        if(self.lookHead[p]=="while"):
            self._match("while")
            self._match("(")
            self.parseCondation()
            self._match(")")
            self.parseStence()
        elif(self.lookHead[p]=="do"):
            self._match("do")
            self.parseStence()
            self._match("while")
            self._match("(")
            self.parseCondation()
            self._match(")")

        elif(self.lookHead[p]=="for"):
            self._match("for")
            self._match("(")
            self.parseIdent()
            self._match("=")
            self.parseExpersion()
            self._match(";")
            self.parseCondation()
            self._match(";")
            self.parseIdent()
            self._match("=")
            self.parseIdent()
            if(self.lookHead[p]=="+"):
                self._match("+")
            elif(self.lookHead[p]=="-"):
                self._match("-")
            self.parseStep()
            self._match(")")
            self.parseStence()

        self.ofile.write("<循环语句>\n")


    def parseStep(self):
        """步长"""
        self.parseUnsignedInteger()
        self.ofile.write("<步长>\n")

    def parseHaveReturnFuncCallStence(self):
        """有返回值函数调用语句"""
        self.parseIdent()
        self._match("(")
        self.parseValueParaList()
        self._match(")")
        self.ofile.write("<有返回值函数调用语句>\n")


    def parseNotHaveReturnFuncCallStence(self):
        """无返回值函数调用语句"""
        self.parseIdent()
        self._match("(")
        self.parseValueParaList()
        self._match(")")
        self.ofile.write("<无返回值函数调用语句>\n")

    def parseValueParaList(self):
        """值参数表"""
        if(self.lookHead[p]==")"):
            a=1
        else:
            self.parseExpersion()
            while 1:
                if(self.lookHead[p]==","):
                    self._match(",")
                    self.parseExpersion()
                    # if(self.lookHead[p+1]=="+" or self.lookHead[p+1]=="-" or \
                    #     self._matchIdent(p+1) or self.lookHead[p+1]=="(" or \
                    #     self._matchNumber(p) or self._matchChar(p)):


                    # else:
                    #     break
                else:
                    break
        self.ofile.write("<值参数表>\n")


    def parseStenceCol(self):
        """语句列"""
        while 1:
            if(self.lookHead[p]=="if" or self.lookHead[p]=="while" or \
                self.lookHead[p] == "do" or self.lookHead[p] == "for" or \
                self.lookHead[p] == "{" or (self._matchIdent(p) and \
                self.lookHead[p+1] == "(" )  or (self._matchIdent(p) and (self.lookHead[p+1] == "=" or self.lookHead[p+1] == "[" )) or\
                self.lookHead[p] == "scanf" or self.lookHead[p] == "printf" or \
                self.lookHead[p] == ";" or self.lookHead[p] == "return"):

                self.parseStence()

            else:
                break
        self.ofile.write("<语句列>\n")

    def parseReadStence(self):
        """读语句"""
        self._match("scanf")
        self._match("(")
        self.parseIdent()
        while 1:
            if(self.lookHead[p] =="," and self._matchIdent(p+1)):
                self._match(",")
                self.parseIdent()
            else:
                break
        self._match(")")
        self.ofile.write("<读语句>\n")

    def parseWriteStence(self):
        """写语句"""
        self._match("printf")
        self._match("(")
        if(self.gram[p]=="STRCON" and self.lookHead[p+1]==","):
            self.parseString()
            self._match(",")
            self.parseExpersion()
            self._match(")")
        elif(self.gram[p]=="STRCON" and self.lookHead[p+1]==")"):
            self.parseString()
            self._match(")")
        elif (self.lookHead[p] == "+" or self.lookHead == "-" or self._matchIdent(p) or \
            self.lookHead[p] == "(" or self._matchNumber(p) or self._matchChar(p)):
            self.parseExpersion()
            self._match(")")
        self.ofile.write("<写语句>\n")

    def parseHaveReturnStence(self):
        """返回语句"""
        self._match("return")
        if(self.lookHead[p]=="("):
            self._match("(")
            self.parseExpersion()
            self._match(")")

        self.ofile.write("<返回语句>\n")



    def parseVoid(self):
        """空"""

    def anlysis(self):
        self.parseProgram()



if __name__ == '__main__':


    gra = gramAnly()
    gra.anlysis()
    gra.ofile.close()


