boudingBox = [
   (int(input()),int(input())),
   (int(input()),int(input()))
]

def getFullRectangle(list1):
   list1.append((list1[0][1], list1[1][0]))
   list1.append((list1[0][0], list1[1][1]))

   return list1

def checkRenderization(rectangle):

   # Check if some point is inside of bounding box
   for point in rectangle:
      # Check if some point is in x ray
      if point[0] >= boudingBox[3][0] and point[0] <= boudingBox[1][0]:

         if point[1] <= boudingBox[0][1] and point[1] >= boudingBox[3][1]:
            return True
   
   if rectangle[0][1] >= boudingBox[0][1] and rectangle[3][1] <= boudingBox[3][1]:
      if rectangle[3][0] >= boudingBox[3][0] or rectangle[1][0] <= boudingBox[1][0]:
         return True

      # Retangulo maior ou igual ao bounding box
      if rectangle[3][0] <= boudingBox[3][0] and rectangle[1][0] >= boudingBox[1][0]:
         return True

   if rectangle[3][0] <= boudingBox[3][0] and rectangle[1][0] >= boudingBox[1][0]:
      return False

   return False

boudingBox = getFullRectangle(boudingBox)
nRetangulos = int(input())

retangulosValidos = []

for i in range(nRetangulos):
   x0 = int(input())
   y0 = int(input())

   x1 = int(input())
   y1 = int(input())

   rectangle = [(x0, y0), (x1, y1)]
   rectangle = getFullRectangle(rectangle)

   if checkRenderization(rectangle) == True:
      retangulosValidos.append(f'{x0} {y0} {x1} {y1}')

for item in retangulosValidos:
   print(item)