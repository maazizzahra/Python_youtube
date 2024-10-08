import logging
from excel_lib.excel_processor import ExcelProcessor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Main')

def main():
    logger.info('start processing')
    
    # Utilisation du gestionnaire de contexte
    with ExcelProcessor('data.xlsx') as processor:
        processor.calculate_totals('A', 'B')  # Calcule le total de la colonne A et l'écrit en B
        processor.save('output.xlsx')

if __name__ == '__main__':
    main()
