from tkinter import *
class MorsAlfabesi:
      mors_sozluk = {
'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','.': '.-.-.-',',': '--..--','?': '..--..',"'": '.----.','!': '-.-.--','/': '-..-.','(': '-.--.',')': '-.--.-','&': '.-...',':': '---...',';': '-.-.-.','=': '-...-','+': '.-.-.','-': '-....-','_': '..--.-','"': '.-..-.','$': '...-..-','@': '.--.-.',' ': '/'
}
      def __init__(self,widow):
            self.widow = widow
            widow.title("Mors Alfabesi Çevirici")
            self.btn1 = Button(widow,text="Çık",command = widow.quit)
            self.btn1.place(relx=0.5,rely=0.8,anchor="center",)
            self.btn2 = Button(widow,text="Yazı/mors",command=self.yazı_mors)
            self.btn2.place(relx=0.7,rely=0.3,anchor="center")
            self.btn3 = Button(widow,text="Mors/Yazı",command=self.mors_yazı)
            self.btn3.place(relx=0.3,rely=0.3,anchor="center")
            self.entry = Entry(widow)
            self.entry.place(height=90,width=800,relx=0.5,rely=0.4,anchor="center")
            self.text_area = Text(widow,height=10,width=45)
            self.text_area.place(relx=0.5,rely=0.6,anchor="center")
      def yazı_mors(self):
            yazı = self.entry.get().upper()
            sonuc = " ".join(self.mors_sozluk[karakter] for karakter in yazı if karakter in self.mors_sozluk)
            self.text_area.delete(1.0,END)
            self.text_area.insert(END,f"Mors Kodu: {sonuc}")
      def mors_yazı(self):
            mors = self.entry.get()
            ters_mors_sozluk = {deger: anahtar for anahtar,deger in self.mors_sozluk.items()}
            sonuc = "".join(ters_mors_sozluk.get(kod,"\t$Hata$"*7) for kod in mors.split(" ")).replace("/"," ")
            self.text_area.delete(1.0,END)
            self.text_area.insert(END,f"Metin: {sonuc}")
widow = Tk()
alfabe = MorsAlfabesi(widow)
widow.mainloop()