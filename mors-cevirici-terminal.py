class MorsAlfabesi:
      mors_sozluk = {
'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','.': '.-.-.-',',': '--..--','?': '..--..',"'": '.----.','!': '-.-.--','/': '-..-.','(': '-.--.',')': '-.--.-','&': '.-...',':': '---...',';': '-.-.-.','=': '-...-','+': '.-.-.','-': '-....-','_': '..--.-','"': '.-..-.','$': '...-..-','@': '.--.-.',' ': '/'
}
      def __init__(self):
            pass
      def yazı_mors(self,yazı):
            yazı = yazı.upper()
            return " ".join(self.mors_sozluk[karakter] for karakter in yazı if karakter in self.mors_sozluk)
      def mors_yazı(self,mors):
            ters_mors_sozluk = {deger: anahtar for anahtar,deger in self.mors_sozluk.items()}
            return "".join(ters_mors_sozluk.get(kod,"\t$Hata$"*7) for kod in mors.split(" ")).replace("/"," ")
alfabe = MorsAlfabesi()
while True:
      soru = input("\n1-Çık\n2-Karakterden morsa\n3-Morstan karaktere\n$$ ")
      if soru == "1": # çık 
         print("Çıkılıyor..")
         break
      elif soru == "2": # karakterden morsa
            metin = input("\n$# Metin girin: ")
            mors_kodu = alfabe.yazı_mors(metin)
            print(mors_kodu)
      elif soru == "3": # morstan karaktere
            morse_code = input("\n$# Mors girin: ")
            txt_kodu = alfabe.mors_yazı(morse_code)
            print(txt_kodu)
      else:
            print("\t$Hata$"*7)