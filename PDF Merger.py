import os
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image

from PyPDF2 import *
from pdf2image import convert_from_path





root=Tk()
root.title('Merge PDFs')
root.geometry('360x640')


main_label=Label(root, text='PDF TOOLS', font= ('Arial', 20), background='#636363',fg='#FFFFFF', relief='solid', compound= CENTER)
main_label.pack()


#MERGE BUTTON:

merger=PdfFileMerger()
pdf_merge_files = []

def marge_click():
        global Merge
        Merge=Tk()
        Merge.title('Merge')
        Merge.geometry('360x640')
        Merge.attributes("-topmost", True)
        add_button=Button(Merge, text='Add', command=add_click)
        add_button.pack()
        save_button=Button(Merge, text='Save',command=save_merge_click)
        save_button.pack()
        
def add_click():
    file = filedialog.askopenfile(title='Select a File', filetypes=[('PDF Files', '*.pdf')])
    file_name = file.name
    file_link = Label(Merge, text=file_name)
    file_link.pack()
    pdf_merge_files.append(file_name)

def save_merge_click():
    for pdf_file in pdf_merge_files:
        merger.append(pdf_file)
    
    Tex = filedialog.asksaveasfilename()
    merger.write(Tex + '.pdf')
    pdf_merge_files.clear()
    Merge.destroy()

merge_button=Button(root, text='',command=marge_click, padx=20 ,pady=20, compound= LEFT)
merge_img = ImageTk.PhotoImage(Image.open('arrow_merge.png'))
merge_button.config(image= merge_img)
merge_button.place(x=25, y=50)

merge_label=Label(root, text='MERGE', font= ('Arial', 10), compound= CENTER)
merge_label.place(x=25, y=110)


#---------------------------------------------------------------------------------------------------

#SPLIT BUTTON:

def split_click():
    file = filedialog.askopenfile(title='Select a File', filetypes=[('PDF Files', '*.pdf')])
    file_name = file.name
    
    input_pdf = PdfFileReader(file_name)
    for p in range(input_pdf.numPages):
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(p))
        with open(file_name +'_page_' + str(p+1) +'.pdf', "wb") as output_stream:
            output.write(output_stream)


split_button=Button(root, text='',command=split_click, padx=20 ,pady=20, compound= LEFT)
split_img = ImageTk.PhotoImage(Image.open('arrow_split.png'))
split_button.config(image= split_img)
split_button.place(x=110, y=50)

split_label=Label(root, text='SPLIT', font= ('Arial', 10), compound= CENTER)
split_label.place(x=110, y=110)


#---------------------------------------------------------------------------------------------------

#PRESS BUTTON:

def Compress_click():
    file = filedialog.askopenfile(title='Select a File', filetypes=[('PDF Files', '*.pdf')])
    file_name = file.name
    
    input_pdf = PdfFileReader(file_name)  
    output = PdfWriter()

    for page in input_pdf.pages:
        page.compressContentStreams()  # This is CPU intensive!
        output.add_page(page)
        with open(file_name + '_Compressed.pdf', "wb") as output_stream:
            output.write(output_stream)


press_button=Button(root, text='',command=Compress_click, padx=20 ,pady=20, compound= LEFT)
press_img = ImageTk.PhotoImage(Image.open('press.png'))
press_button.config(image= press_img)
press_button.place(x=195, y=50)

press_label=Label(root, text='PRESS', font= ('Arial', 10), compound= CENTER)
press_label.place(x=195, y=110)


#---------------------------------------------------------------------------------------------------

#TO IMAGE BUTTON:

def to_image():
    file = filedialog.askopenfile(title='Select a File', filetypes=[('PDF Files', '*.pdf')])
    file_name = file.name
    
    #poppler is needed here
    poppler= r'C:\Users\alkallasa\Desktop\Main_Folder\PDF Project\poppler\Library\bin'

    pdf= file_name
    saving_folder= filedialog.askdirectory()

    pages= convert_from_path(pdf_path=pdf,poppler_path=poppler)
    c=1
    for page in pages:
        img_name=f'img-{c}.jpeg'
        page.save(os.path.join(saving_folder,img_name), 'JPEG')
        c+=1




to_img_button=Button(root, text='',command=to_image, padx=20 ,pady=20, compound= LEFT)
to_img = ImageTk.PhotoImage(Image.open('to_image.png'))
to_img_button.config(image= to_img)
to_img_button.place(x=280, y=50)

to_img_label=Label(root, text='TO JPG', font= ('Arial', 10), compound= CENTER)
to_img_label.place(x=280, y=110)

root.mainloop()
