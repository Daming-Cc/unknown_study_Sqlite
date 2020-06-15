import sqlite3

conn = sqlite3.Connection('f:/Big_Project.db3')
print('数据库连接成功！')
#--------------------------------------------------------------------------------------
while True:
       print('\n\t\t会员制超市管理系统\n')
       print('\n1.商品管理 2.会员管理 3.购物结账 4.销售统计 0.退出')
       n = int(input('请输入你的选择(0-4)：'))
       
       if(n==0):
               print('再见！')
               break

       if(n<0 or n>6):
               print('输入有误！')
               continue
       #--------------------------------------------------------------------------------       
       #商品管理模块
       if(n==1):
        while True:
           
           print('\n\t\t商品管理\n')
           print('\n1.新建 2.查找 3.添加 4.修改 5.删除 6.排序 0.退出')
           n = int(input('请输入你的选择(0-6)：'))

           if(n==0):
               print('再见！')
               break

           if(n<0 or n>6):
               print('输入有误！')
               continue

           elif(n==1):
               conn.execute('create table goods(id int primary key, \
                               name text, unit text, purchase_price text, \
                               price text, amount text, supplier text)')        
               print('数据库表创建成功！')

           elif(n==2):
               skey=input('请输入查找关键字,*表示查找全部数据：')
               if(skey=='*'):
                   cur=conn.execute('select * from goods')
               else:
                   sk='%'+skey+'%'
                   cur=conn.execute('select * from goods where id=? or \
                               name like ? or unit like ? or purchase_price like ? \
                               or price like ? or amount like ? or \
                               supplier like ?',(skey,sk,sk,sk,sk,sk,sk))
               for row in cur:
                   print()
                   print('编号：',row[0])
                   print('名称：',row[1])
                   print('计量单位：',row[2])
                   print('进价：',row[3])
                   print('售价：',row[4])
                   print('数量：',row[5])
                   print('供货商：',row[6])
               print('查询结束！')

           elif(n==3):
               id1=int(input('请输入记录编号：'))
               name=input('请输入名称：')
               unit=input('请输入计量单位：')
               purchase_price=input('请输入进价：')
               price=input('请输入售价：')
               amount=input('请输入数量：')
               supplier=input('请输入供货商：')

               conn.execute('insert into goods values(?,?,?,?,?,?,?)', \
                            (id1,name,unit,purchase_price,price,amount,supplier))
               conn.commit()
               print('添加记录成功！')

           elif(n==4):
               updateid=input('请输入要修改记录的编号：')
               cur=conn.execute('select * from goods where id='+updateid)
               for row in cur:
                   print('1.编号：',row[0],end='  ')
                   print('2.名称：',row[1],end='  ')
                   print('3.计量单位：',row[2],end='  ')
                   print('4.进价：',row[3],end='  ')
                   print('5.售价：',row[4],end='  ')
                   print('6.数量：',row[5],end='  ')
                   print('7.供货商：',row[6],end='  ')
                   print('0.退出')
               while True:
                   col=int(input('请输入要修改的字段编号：'))
                   if(col==0):
                       break
                   else:
                       data=input('请输入修改后的值：')
                       if(col==1):
                           conn.execute('update goods set id=? where id=?',(data,updateid))
                           updateid=data
                       elif(col==2):
                           conn.execute('update goods set name=? where id=?',(data,updateid))
                       elif(col==3):
                           conn.execute('update goods set unit=? where id=?',(data,updateid))
                       elif(col==4):
                           conn.execute('update goods set purchase_price=? where id=?',(data,updateid))
                       elif(col==5):
                           conn.execute('update goods set price=? where id=?',(data,updateid))
                       elif(col==6):
                           conn.execute('update goods set amount=? where id=?',(data,updateid))
                       elif(col==7):
                           conn.execute('update goods set supplier=? where id=?',(data,updateid))
                       conn.commit()    

               print('修改记录成功！')

           elif(n==5):
               delid=input('请输入要删除的记录编号：')
               yorn=input('是否确定删除此记录？（Y/N）:')
               if(yorn=='Y' or yorn=='y'):
                   conn.execute('delete from goods where id='+delid)
                   conn.commit()
                   print('删除记录成功！')

           else:
               while True:
                   print('1.编号',end=' ')
                   print('2.名称',end=' ')
                   print('3.计量单位',end=' ')
                   print('4.进价',end=' ')
                   print('5.售价',end=' ')
                   print('6.数量',end=' ')
                   print('7.供货商',end=' ')
                   print('0.退出')
                   order=input('请选择排序关键字（0-7）：')
                   if(order=='0'):
                       break
                   else:
                       cur=conn.execute('select * from goods order by '+order)
                       for row in cur:
                           print()
                           print('编号：',row[0])
                           print('名称：',row[1])
                           print('计量单位：',row[2])
                           print('进价：',row[3])
                           print('售价：',row[4])
                           print('数量：',row[5])
                           print('供货商：',row[6])

               print('排序输出结束！')
       #---------------------------------------------------------------------------------daming
       #会员管理模块
       if(n==2):
        while True:
           
           print('\n\t\t会员管理\n')
           print('\n1.新建 2.查找 3.添加 4.修改 5.删除 6.排序 0.退出')
           n = int(input('请输入你的选择(0-6)：'))

           if(n==0):
               print('再见！')
               break

           if(n<0 or n>6):
               print('输入有误！')
               continue

           elif(n==1):
               conn.execute('create table members(id int primary key, \
                               name text, tel text, level text, \
                               discount text, integral text, balance text)')        
               print('数据库表创建成功！')

           elif(n==2):
               skey=input('请输入查找关键字,*表示查找全部数据：')
               if(skey=='*'):
                   cur=conn.execute('select * from members')
               else:
                   sk='%'+skey+'%'
                   cur=conn.execute('select * from members where id=? or \
                               name like ? or tel like ? or level like ? \
                               or discount like ? or integral like ? or \
                               balance like ?',(skey,sk,sk,sk,sk,sk,sk))
               for row in cur:
                   print()
                   print('编号：',row[0])
                   print('姓名：',row[1])
                   print('电话：',row[2])
                   print('等级：',row[3])
                   print('折扣系数：',row[4])
                   print('积分：',row[5])
                   print('余额：',row[6])
               print('查询结束！')

           elif(n==3):
               id1=int(input('请输入记录编号：'))
               name=input('请输入姓名：')
               tel=input('请输入电话：')
               level=input('请输入等级：')
               discount=input('请输入折扣系数：')
               integral=input('请输入积分：')
               balance=input('请输入余额：')

               conn.execute('insert into members values(?,?,?,?,?,?,?)', \
                            (id1,name,tel,level,discount,integral,balance))
               conn.commit()
               print('添加记录成功！')

           elif(n==4):
               updateid=input('请输入要修改记录的编号：')
               cur=conn.execute('select * from members where id='+updateid)
               for row in cur:
                   print('1.编号：',row[0],end='  ')
                   print('2.姓名：',row[1],end='  ')
                   print('3.电话：',row[2],end='  ')
                   print('4.等级：',row[3],end='  ')
                   print('5.折扣系数：',row[4],end='  ')
                   print('6.积分：',row[5],end='  ')
                   print('7.余额：',row[6],end='  ')
                   print('0.退出')
               while True:
                   col=int(input('请输入要修改的字段编号：'))
                   if(col==0):
                       break
                   else:
                       data=input('请输入修改后的值：')
                       if(col==1):
                           conn.execute('update members set id=? where id=?',(data,updateid))
                           updateid=data
                       elif(col==2):
                           conn.execute('update members set name=? where id=?',(data,updateid))
                       elif(col==3):
                           conn.execute('update members set tel=? where id=?',(data,updateid))
                       elif(col==4):
                           conn.execute('update members set level=? where id=?',(data,updateid))
                       elif(col==5):
                           conn.execute('update members set discount=? where id=?',(data,updateid))
                       elif(col==6):
                           conn.execute('update members set integral=? where id=?',(data,updateid))
                       elif(col==7):
                           conn.execute('update members set balance=? where id=?',(data,updateid))
                       conn.commit()    

               print('修改记录成功！')

           elif(n==5):
               delid=input('请输入要删除的记录编号：')
               yorn=input('是否确定删除此记录？（Y/N）:')
               if(yorn=='Y' or yorn=='y'):
                   conn.execute('delete from members where id='+delid)
                   conn.commit()
                   print('删除记录成功！')

           else:
               while True:
                   print('1.编号',end=' ')
                   print('2.姓名',end=' ')
                   print('3.电话',end=' ')
                   print('4.等级',end=' ')
                   print('5.折扣系数',end=' ')
                   print('6.积分',end=' ')
                   print('7.余额',end=' ')
                   print('0.退出')
                   order=input('请选择排序关键字（0-7）：')
                   if(order=='0'):
                       break
                   else:
                       cur=conn.execute('select * from members order by '+order)
                       for row in cur:
                           print()
                           print('编号：',row[0])
                           print('姓名：',row[1])
                           print('电话：',row[2])
                           print('等级：',row[3])
                           print('折扣系数：',row[4])
                           print('积分：',row[5])
                           print('余额：',row[6])

               print('排序输出结束！')
       #---------------------------------------------------------------------------------copy right
       #购物结账模块
       #if(n==3):
               print('\n\t\t购物结账\n')
       


conn.close()
