
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
    ifile = open('testfile.txt','rt')
    string = ifile.read()
    ifile.close()
    #打开读取了文件内容，然后关闭文件

    #输入字符串
    getToken(string)




def getToken(str):
    result = None;

    #打开文件
    ofile = open("output.txt","w")

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
            ofile.write("{} {}\n".format(grammer,result))
            print("{} {}".format(grammer,result))  # 输出

            if(len(str)==0):#通过是否等于0来判断这个时候str是不是None
                str = None

    #关闭文件
    ofile.close()
if __name__ == '__main__':
    mainFunc()
