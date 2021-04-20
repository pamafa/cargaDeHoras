#IMPORTS
import PySimpleGUI as sg
import logging
import funcionesPrincipal

#CONSTANTES
MLINE_KEY = '-MLINE-'+sg.WRITE_ONLY_KEY


#VARIABLES
tareasGeotask = []
tareasClickup = []
archivoDiferencia = ''
errorMsg = ''
seguir = ''

#CODIGO
#Logger
# create logger with 'spam_application'
logger = logging.getLogger('logGeneral')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('log.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Design the window
layout = [ 
    [sg.Text('Archivos de entrada')],
    [sg.Text('Archivo GeoTask', size=(20, 1)), sg.InputText(), sg.FileBrowse()],
    [sg.Text('Archivo ClickUp ', size=(20, 1)), sg.InputText(), sg.FileBrowse()],
    [sg.Text('Versión Excel de salida ', size=(20, 1)), sg.Combo(['Excel 97 (.xls)', 'Excel 2007 (.xlsx)'], size=(15,1), enable_events=True, key='EXCEL_KEY')],
    [sg.Text('Tipo de Tarea de salida ', size=(20, 1)), sg.Combo(['Desarrollo', 'Testing'], size=(15,1), enable_events=True, key='TAREA_KEY')],
    [sg.Submit(), sg.Cancel()],
    [sg.Multiline(size=(80,20), key=MLINE_KEY)]
]

# Create the Window
window = sg.Window('Archivos de entrada', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    
    seguir = 'S'
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    
    window[MLINE_KEY].update("-- INICIO -- \n", text_color_for_value='blue', append=True)

    archivoGeotask = values[0]
    archivoClickup = values[1]
    
    if archivoGeotask == '':
        window[MLINE_KEY].update("ERROR: El archivo GeoTask no puede estar vacío, seleccione un archivo\n", text_color_for_value='red', append=True)
        logger.error("El archivo GeoTask no puede estar vacío, seleccione un archivo")
        seguir = 'N'

    if archivoClickup == '':
        window[MLINE_KEY].update("ERROR: El archivo ClickUp no puede estar vacío, seleccione un archivo\n", text_color_for_value='red', append=True)
        logger.error("El archivo ClickUp no puede estar vacío, seleccione un archivo")
        seguir = 'N'
    
    if seguir == 'S':

        window[MLINE_KEY].update("Archivo GeoTask:" + archivoGeotask + '\n', text_color_for_value='black', append=True)
        logger.info("Archivo GeoTask:" + archivoGeotask)

        window[MLINE_KEY].update("Archivo ClickUp:" + archivoClickup + '\n', text_color_for_value='black', append=True)
        logger.info("Archivo ClickUp:" + archivoClickup)

        window[MLINE_KEY].update('\n', text_color_for_value='black', append=True)

        window[MLINE_KEY].update("Extrayendo información necesaria de los archivos...\n", text_color_for_value='black', append=True)
        logger.info("Extrayendo información necesaria de los archivos...")

        logger.debug("Llama a importarArchivos")
        tareasGeotask, tareasClickup, errorMsg = funcionesPrincipal.importarArchivos(archivoGeotask, archivoClickup, values['TAREA_KEY'])
        logger.debug("Vuelve de importarArchivos")

        if errorMsg == "":
            window[MLINE_KEY].update("La información se extrajo correctamente:\n", text_color_for_value='black', append=True)

            cantGE = len(tareasGeotask)
            window[MLINE_KEY].update("Cantidad tareas GeoTask: " + str(cantGE) + "\n", text_color_for_value='black', append=True)
            logger.debug("Cantidad tareas GeoTask: " + str(cantGE))
            primerObjetoGE =  tareasGeotask[0].imprimir()
            logger.debug("Primer objeto: " + primerObjetoGE)

            cantCL = len(tareasClickup)
            window[MLINE_KEY].update("Cantidad tareas ClickUp: " + str(cantCL) + "\n", text_color_for_value='black', append=True)
            logger.debug("Cantidad tareas ClickUp: " + str(cantCL))
            primerObjetoCL =  tareasClickup[0].imprimir()
            logger.debug("Primer objeto: " + primerObjetoCL)

        else:
            window[MLINE_KEY].update("ERROR:" + errorMsg + '\n', text_color_for_value='red', append=True)
            logger.error("ERROR:" + errorMsg)
            seguir = 'N'

    else:
        logger.info('SEGUIR= ' + seguir)
    
    window[MLINE_KEY].update('\n', text_color_for_value='black', append=True)

    if seguir == 'S':

        window[MLINE_KEY].update("Generando nuevo archivo para GeoTask...\n", text_color_for_value='black', append=True)
        logger.info("Generando nuevo archivo para GeoTask...")

        logger.debug("Llama a exportarArchivo")
        archivoDiferencia, errorMsg = funcionesPrincipal.exportarArchivo(values['EXCEL_KEY'], tareasGeotask, tareasClickup)
        logger.debug("Vuelve de exportarArchivo")

        if errorMsg == '':
            window[MLINE_KEY].update("Nuevo archivo generado: " + archivoDiferencia + "\n", text_color_for_value='black', append=True)
            logger.info("Nuevo archivo generado: " + archivoDiferencia)

        else:
            window[MLINE_KEY].update("ERROR:" + errorMsg + '\n', text_color_for_value='red', append=True)
            logger.error("ERROR:" + errorMsg)

        window[MLINE_KEY].update("\n", text_color_for_value='black', append=True)
        window[MLINE_KEY].update("-- FIN -- \n", text_color_for_value='blue', append=True)

window.close()
