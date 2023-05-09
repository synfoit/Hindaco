from database import Database


column_compare = {
    'EQUAL_TO': '=',
    'GREATER_THAN': '>',
    'GREATER_THAN_OR_EQUAL_TO': '>=',
    'LESSER_THAN': '<',
    'LESSER_THAN_OR_EQUAL_TO': '<='
}


class BatchModel:
    BATCH_TABLE = 'batches'

    def __init__(self):
       # self._db_config = db_config
        self._db = Database()
        self._latest_error = ''

    @property
    def latest_error(self):
        return self._latest_error

    @latest_error.setter
    def latest_error(self, latest_error):
        self._latest_error = latest_error



    def find_by_batch_id(self, batch_id):
        query_columns_dict = {
            'id': (column_compare['EQUAL_TO'], batch_id)
        }
        result = self._db.get_single_data(BatchModel.BATCH_TABLE, query_columns_dict)
        return result


    def insert(self, Batch_ID, Batch,Tare_Weight,Gross_Weight,Net_Weight,Ship_Total,time):
        self.latest_error = ''


        query_columns_dict = {
            'batch_id': Batch_ID,
            'batch':Batch ,
            'tare_weight': Tare_Weight,
            'gross_weight': Gross_Weight,
            'net_weight':Net_Weight,
            'ship_total':Ship_Total,
            'time':time
        }

        row_count = self._db.insert_single_data(BatchModel.BATCH_TABLE, query_columns_dict)
        return row_count
