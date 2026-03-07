website="https://www.google.com"
course="Python for Beginners"

# 1-'course' karakter dizisinde kaç karakter bulunmaktadır? #bunun için len() fonksiyonunu kullanabilirsiniz.
result=len(course)
length=len(website)#website karakter dizisinde kaç karakter olduğunu bulmak için len() fonksiyonunu kullanabilirsiniz.

# 2- 'website' içinden www karakterlerini alın.#bunun için slicing yapabilirsiniz. www karakterleri 8. karakterden başlayıp 11. karaktere kadar devam eder.
result=website[8:11]

# 3- 'website' içinden com karakterlerini alın.#bunun için slicing yapabilirsiniz. com karakterleri 19. karakterden başlayıp 22. karaktere kadar devam eder.
result=website[19:22]
result=website[length-3:length]#com karakterlerini almak için slicing yapabilirsiniz. com karakterleri 3 karakter uzunluğunda olduğu için length-3 ile başlayıp length ile bitirebilirsiniz.

# 4-'course' içinden ilk 5 ve son 5 karakteri alın.
result=course[0:5]#course karakter dizisindeki ilk 5 karakteri almak için slicing yapabilirsiniz. İlk 5 karakter 0. karakterden başlayıp 4. karaktere kadar devam eder.
result=course[-5:]#course karakter dizisindeki son 5 karakteri almak için slicing yapabilirsiniz. Son 5 karakter -5. karakterden başlayıp sona kadar devam eder.

# 5-  'course' karakter dizisindeki karakterleri tersten yazdırın.
result=course[::]#course karakter dizisindeki bütün karakterleri yazar
result=course[::2]#course karakter dizisindeki bütün karakterleri 2'şer atlayarak yazar
result=course[::-1]#course karakter dizisindeki bütün karakterleri tersten yazar
s ='12345'*5 #12345 karakter dizisini 5 kez tekrarlayarak yeni bir karakter dizisi oluşturur.
#print(s[::5])#s karakter dizisindeki bütün karakterleri 5'er atlayarak yazar.yani 12345123451234512345 olan sonucun 1, 6, 11, 16, 21. karakterlerini yazdırır. Bu karakterler sırasıyla 1, 1, 1, 1, 1 olacaktır.


name,surname,age,job='ali','polat',21,'öğrenci'

#6- yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#   "Benim adım ali polat, yaşım 21 ve mesleğim öğrenci"
result = "benim adım " +name+" " +surname+",yaşım " + str(age)+ " ve mesleğim " +job
result = "benim adım {} {}, yaşım {} ve mesleğim {}".format (name,surname,age,job)#format() fonksiyonu ile değişkenleri sırasıyla {} içine yerleştirerek yazdırabilirsiniz. format() fonksiyonunun içine sırasıyla name, surname, age ve job değişkenlerini vererek istediğiniz sonucu elde edebilirsiniz.
result = f"benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"#f-string kullanarak değişkenleri {} içine yerleştirerek yazdırabilirsiniz. f-string kullanarak istediğiniz sonucu elde edebilirsiniz.

print(result)

#7-'Hello world' ifadesindeki 'w' ifadesini 'W' yapın.
s='Hello world'
s=s[0:6]+'W'+s[-4:]#s karakter dizisini değiştirmek için slicing ve string birleştirme kullanabilirsiniz.
s=s.replace('w','W')#s karakter dizisindeki 'w' karakterini 'W' karakteri ile değiştirmek için replace() fonksiyonunu kullanabilirsiniz. replace() fonksiyonunun ilk parametresi değiştirmek istediğiniz karakter, ikinci parametresi ise yeni karakterdir. Bu şekilde s karakter dizisindeki 'w' karakteri 'W' karakteri ile değiştirilir ve sonucu s değişkenine atar. Sonuç olarak s değişkeni 'Hello World' olacaktır.
print(s)
#8- 'abc' ifadesini 3 defa yan yana yazdırın.
result='abc'*3#'abc' karakter dizisini 3 kez tekrarlayarak yeni bir karakter dizisi oluşturur.
print(result)# tırnaktan sonra boşluk bırakırsan abc abc abc şeklinde çıkar. boşluk bırakmazsanız abcabcabc şeklinde çıkar.
