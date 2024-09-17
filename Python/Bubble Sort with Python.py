def bubble_sort(liste):
  n = len(liste) # listenin uzunluğunu bul
  for i in range(n-1): # listenin son elemanına kadar döngü oluştur
    for j in range(0, n-i-1): # listenin sonundan başlayarak geriye doğru döngü oluştur
      if liste[j] > liste[j+1]: # bitişik iki elemanı karşılaştır
        liste[j], liste[j+1] = liste[j+1], liste[j] # eğer sol taraftaki sağ taraftakinden büyükse yerlerini değiştir
  return liste # sıralanmış listeyi döndür

# örnek bir liste tanımla
liste = [64, 34, 25, 12, 22, 11, 90]

# bubble_sort fonksiyonunu çağır ve sonucu yazdır
print(bubble_sort(liste))