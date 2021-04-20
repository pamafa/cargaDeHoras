import pandas
import logging

logger = logging.getLogger('logGeneral')

# archivo GEOTASK

# archivo CLICKUP
def importarArchivoCLickup(archivoCL, tarea_combo): 

    logger.debug("Entra a funcionesCSV.importarArchivoCLickup")

    claseCL     = []
    errorMsg    = ''

    archCL = pandas.read_csv(archivoCL, 
        sep=',',
        quotechar='"',
        encoding='utf8',
        header=1,
        parse_dates=[7],
        usecols=[48 ,49, 7, 35])

    for row in archCL:

        logger.debug(row)


    logger.debug("Sale de funcionesCSV.importarArchivoCLickup")
    return claseCL, errorMsg