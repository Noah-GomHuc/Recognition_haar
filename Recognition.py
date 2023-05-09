import cv2, numpy, os, argparse


DEFAULT_OUTPUT_PATH = "ImagenesCapturadas/"
DEFAULT_INPUT_PATH = "HaarCascade_caradefrente_alt.xml"

class Capturadevideo:
    def __init__(self):
        self.ars0bj = Parse()
        self.faceCascade = cv2.CascadeClassifier(self.ars0bj.input_path)
        #Inicializamos el contador
        self.count = 0
        #aca se selecciona la cantidad de camaras para el trabajo y como principal asignamos la variable "Source"
        self.Source = cv2.VideoCapture(0)

    def CaptureFrames(self):
        while True:
        
        #Crea un unico numero por cada frame
            NumeroDeFrame= "%01a" % (self.count)

            #Capturar frame x frame / #devuelve ret y frame 
            ret, frame = self.videoSource.read()

            #Seteamos al color gris , para que "haar cascade" pueda facilmente detectar caras y angulos
            ColorDePantalla =  cv2.cvtColor(frame, cv2.COLOR_BRG2GRAY)

            #Aca se customiza como queres que el modelo de dettección detece tu cara
            faces = cv2.faceCascade.detectMultiScale(ColorDePantalla, scaleFactor = 1.1, minNeighbors = 5, minsize = (30,30) flags = cv2.CASCADE_SCALE_IMAGE)
            
            
            #pone en pantalla el frame resultantee¿
            cv2.imshow("Te veo :)", ColorDePantalla)

            if len(faces) == 0:
                pass 

            elif len(faces) > 0:
                print("Biennn se detecto tu cara!!!")
                #Esto es para que se dibuje el rectangulo en la cara
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                
                #esto para que tenga output
                cv2.imwrite(DEFAULT_OUTPUT_PATH)

            #aumenta el contador para poder optener un unico nombre per frame
            self.count += 1
            #Apreta "esc" y muere
            if cv2.waitKey(2) == 27:
                break
            
            #para no mandarme cagada
            self.videoSource.release()
            cv2.waitKey(500)
            cv2.destroyAllWindows()
            cv2.waitKey(500)





def Parse():
    parser = argparse.ArgumentParser(description="ruta del reconocimiento ")
    parser.add_argument("-i", "--input_path", type=str, default=DEFAULT_INPUT_PATH)
    parser.add_argument("-o, ", "--outputpath", type=str, default=DEFAULT_OUTPUT_PATH)
    args = parser.parse_args()
    return args

