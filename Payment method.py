import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Define the payment URLs based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support
phonepay_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'

# Create QR codes for each payment app
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR codes to image files (optional)
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (you may need to install PIL/pillow library)
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()