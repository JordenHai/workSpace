#coding=gbk
# from tkinter import *
# master =Tk()
# def callback():
#     print('click!')
#����ͨ�ķ��ز�������ť����һ��ֵ��ͨ��һ���������ݣ�
#b=Button(master,text='OK',command=callback)

#DISABLED  state״̬    ��ʾ���ܰ��������ť���޷����������ť
#b = Button(master, text="Help", state=DISABLED)

#���㲻���ô�С��ʱ�򣬰�ť���������ж�������Ȼ��Ҳ����ָ����С��padx��pady
#b = Button(master, text="Help", state=DISABLED,padx=59,pady=99)

#��Ȼ����Ҳ�����ڰ�ť������д��һ�����壬����һ��������������ʾ�ģ����԰�ťҲ�ǿ��԰������������б�ʾ�ģ�λͼҲ�ǿ��Ե�
# f = Frame(master, height=320, width=320)
# f.pack_propagate(0) # don't shrink
# f.pack()
# b = Button(f, text="Sure!")#�����嵼��
# b.pack(fill=BOTH, expand=1)#��䶥������չ

# #��text�ж��е�ʱ��
# b = Button(master, text='longtext��ʿ���������ʿ���������', anchor=W, justify=LEFT, padx=2)

# ����������ð�ť�����Ѿ�����ȥ�˵���ʵ����û�д�����ť�Ĺ��ܣ��ٵ�����ܴ���
# b.config(relief=SUNKEN)

# b = Checkbutton(master, image=, variable='var', indicatoron=0)
# b = Button(master, text="Click me", image='pattern', compound=CENTER)


# b.pack()
#
# mainloop()
#coding=gbk
#
# activebackground, activeforeground:����ť������ʱ��ʹ�õ���ɫ
# anchor:���ư�ť�����ݵ�λ�á�ʹ��N, NE, E, SE, S, SW, W, NW, or CENTER��Щֵ֮һ��Ĭ��ֵ��CENTER��
# background (bg), foreground (fg):��ť����ɫ��Ĭ��ֵ���ض�ƽ̨��ء�
# bitmap:��ʾ�ڴ��ڲ����е�λͼ�����imageѡ�ָ���ˣ������ѡ����ԡ������λͼ������ƽ̨�϶��� Ч��error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, �� warning.
#
# borderwidth (bd):��ť�߿�Ŀ�ȡ�Ĭ��ֵ���ض�ƽ̨��ء���ͨ����1��2���ء�
# command:����ť������ʱ�����õ�һ�������򷽷������ص��Ŀ�����һ���������������Ŀɵ��õ�Python����
# cursor:������ƶ�����ť��ʱ����ʾ�Ĺ�ꡣ
# default:��������ˣ���ťΪĬ�ϰ�ť��
# disabledforeground:����ť��Чʱ����ɫ��
# image:�ڲ�������ʾ��ͼ�����ָ������text��bitmapѡ������ԡ�
# justify:��������ı���ζ��롣��ȡֵ�У�LEFT, RIGHT, �� CENTER��
# padx, pady:ָ���ı���ͼ���밴ť�߿�ļ�ࡣ
# state:��ť��״̬��NORMAL, ACTIVE �� DISABLED��Ĭ��ֵΪNORMAL��
# relief:�߿��װ�Ρ�ͨ����ť����ʱ�ǰ��ݵģ�����͹������Ŀ���ȡֵ��GROOVE, RIDGE, �� FLAT��
# text:��ʾ�ڰ�ť�е��ı����ı������Ƕ��С����bitmaps��imageѡ�ʹ�ã���textѡ�����
# textvariable:
# underline:���ı���ǩ���ĸ��ַ����»��ߡ�Ĭ��ֵΪ-1����˼��û���ַ����»���
# width, height:��ť�ĳߴ硣�����ť��ʾ�ı����ߴ�ʹ���ı��ĵ�λ�������ť��ʾͼ�󣬳ߴ�������Ϊ��λ������Ļ�ĵ�λ��������ߴ�ûָ��������
# ���ݰ�ť�����������㡣


# #coding=gbk
# from tkinter import *
# master = Tk()

# w = Label(master, text="Hello, world!")
#
# w = Label(master, text="Rouge", fg="red")
w = Label(master, text="Helvetica", font=("Helvetica", 16))

# w = Label(master, text=longtext, anchor=W, justify=LEFT)
#
# v = StringVar()
# Label(master, textvariable=v).pack()
# v.set("New Text!")
#
# # b.pack()
# mainloop()
