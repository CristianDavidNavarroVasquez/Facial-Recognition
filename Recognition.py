import cv2 as cv
import face_recognition
import os
import json

def validar_nombre(nombre, archivo_json="list.json"):
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as f:
            lista_nombres = json.load(f)
            return nombre in lista_nombres
    else:
        return False
    
def crear_lista (nombre, archivo_json="list.json"):
    if not os.path.exists(archivo_json):
        with open(archivo_json, 'w') as f:
            json.dump([nombre], f)
    else:
        with open(archivo_json, 'r') as f:
            lista_nombres = json.load(f)
            if nombre not in lista_nombres:
                lista_nombres.append(nombre)
                with open(archivo_json, 'w') as f:
                    json.dump(lista_nombres, f)

def mostrar_lista(archivo_json="list.json"):
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as f:
            lista_nombres = json.load(f)
            print("Lista de nombres registrados:")
            for nombre in lista_nombres:
                print(nombre)
    else:
        print("No hay archivo JSON existente.")

def reconocimiento_facial_en_carpeta(carpeta_imagenes="./FaceImages/"):
    # Lista para almacenar las codificaciones faciales y nombres asociados
    codificaciones_conocidas = []
    nombres_conocidos = []

    # Iterar sobre cada archivo en la carpeta de imágenes
    for nombre_archivo in os.listdir(carpeta_imagenes):
        # Comprobar si el archivo es una imagen (puedes ajustar las extensiones según tus necesidades)
        if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Ruta completa de la imagen
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_archivo)

            # Leer la imagen y obtener la codificación facial
            imagen = cv.imread(ruta_imagen)
            face_loc = face_recognition.face_locations(imagen)[0]
            face_encodings = face_recognition.face_encodings(imagen, known_face_locations=[face_loc])[0]

            # Agregar la codificación facial y el nombre asociado a las listas
            codificaciones_conocidas.append(face_encodings)
            nombres_conocidos.append(os.path.splitext(nombre_archivo)[0])  # Utilizando el nombre del archivo sin extensió
    cap = cv.VideoCapture(2)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv.CAP_PROP_FPS, 30)

    

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        frame = cv.flip(frame, 1)

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, known_face_locations=face_locations)

        # Procesar cada cara detectada
        # Realizamos una union  de los datos face_locations y face_encodings para despues compararalos 
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Comparar reconocimiento facial con todas las imágenes conocidas
            resultados = face_recognition.compare_faces(codificaciones_conocidas, face_encoding)

            # Determinar el nombre basado en los resultados de comparación
            nombre = "Desconocido"
            if True in resultados:
                nombre = nombres_conocidos[resultados.index(True)]
                if not validar_nombre(nombre=nombre):
                    crear_lista(nombre)


            # Dibujar un rectángulo alrededor de la cara y mostrar el nombre
            cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv.putText(frame, nombre, (left + 6, bottom - 6), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv.imshow("Frame", frame)
        k = cv.waitKey(1)
        if (k == 27) & 0xFF:
            break

    cap.release()
    cv.destroyAllWindows()

# Llamar a la función con la carpeta por defecto
reconocimiento_facial_en_carpeta()

  