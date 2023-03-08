# from stegano import lsb
#
# secret = lsb.hide('/home/divan/Изображения/оснфон.png', 'i am a lesbian')
# secret.save('/home/divan/Изображения/оснфон_secret.png')
#
# result = lsb.reveal('/home/divan/Изображения/оснфон_secret.png')
# print(result)
#
# from stegano import exifHeader
#
# secret2 = exifHeader.hide('/home/divan/Изображения/ssssssssssss.jpg', '/home/divan/Изображения/ssssssssssss_secret2.jpg', 'жду тебя')
#
# res = exifHeader.reveal('/home/divan/Изображения/ssssssssssss_secret2.jpg')
# res = res.decode()
# print(res)

from steganocryptopy.steganography import Steganography

Steganography.generate_key('')
secret3 = Steganography.encrypt('key.key', '/home/divan/Изображения/луна.png', 'secrMess.txt')
secret3.save('/home/divan/Изображения/лунаsecr.png')
res1 = Steganography.decrypt('key.key', '/home/divan/Изображения/лунаsecr.png')

print(res1)