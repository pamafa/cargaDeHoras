import os
import logging
import funcionesXLSX
import funcionesCSV

logger = logging.getLogger('logGeneral')

def importarArchivos(archivoGE, archivoCL, tarea_combo):
    
    logger.debug("Entra a importarArchivos")
    
    claseGE     = []
    claseCL     = []
    errorMsg    = ''

    extensionGE = os.path.splitext(archivoGE)
    extensionCL = os.path.splitext(archivoCL)
  
    logger.debug("Ruta archivo GeoTask: " + extensionGE[0])
    logger.debug("Extensión archivo GeoTask: " + extensionGE[1])
    logger.debug("Ruta archivo ClickUp: " + extensionCL[0])
    logger.debug("Extensión archivo ClickUp: " + extensionCL[1])

    if extensionGE[1] == '.xlsx':
        logger.debug("Llama a funcionesXLSX.importarArchivoGEotask")
        #funcionesXLSX.importarArchivoGEotask(archivoGE, claseGE, errorMsg)
        claseGE, errorMsg = funcionesXLSX.importarArchivoGEotask(archivoGE)
        logger.debug("Vuelve de funcionesXLSX.importarArchivoGEotask")

    if extensionCL[1] == '.xlsx':
        logger.debug("Llama a funcionesXLSX.importarArchivoCLickup")
        claseCL, errorMsg = funcionesXLSX.importarArchivoCLickup(archivoCL, tarea_combo)
        logger.debug("Vuelve de funcionesXLSX.importarArchivoCLickup")

    
    # if extensionGE[1] == '.xls':
    #     funcionesXLSX.importarArchivoGEotask(archivoGE, claseGE, errorMsg)

    # if extensionCL[1] == '.xls':
    #     funcionesXLSX.importarArchivoCLickup(archivoCL, claseCL, errorMsg)
    
    #if extensionGE[1] == '.csv':
    #     funcionesXLSX.importarArchivoGEotask(archivoGE, claseGE, errorMsg)

    if extensionCL[1] == '.csv':
        logger.debug("Llama a funcionesCSV.importarArchivoCLickup")
        claseCL, errorMsg = funcionesCSV.importarArchivoCLickup(archivoCL, tarea_combo)
        logger.debug("Vuelve de funcionesCSV.importarArchivoCLickup")


    logger.debug("Sale de importarArchivos")
    return claseGE, claseCL, errorMsg

def exportarArchivo(excelCombo, claseGeotask, claseClickup):

    logger.debug("Entra a exportarArchivo")

    logger.debug("Tipo de archivo de Salida: " + excelCombo)

    archivoDiferencia = ''
    errorMsg = ''

    if excelCombo == '.xls':
        pass

    if excelCombo == '.xlsx':
        pass

    logger.debug("Sale de exportarArchivo")
    return archivoDiferencia, errorMsg

