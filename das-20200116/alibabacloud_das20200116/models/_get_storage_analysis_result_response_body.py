# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetStorageAnalysisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetStorageAnalysisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request is successful, **Successful** is returned. Otherwise, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetStorageAnalysisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStorageAnalysisResultResponseBodyData(DaraModel):
    def __init__(
        self,
        analyzed_db_count: int = None,
        storage_analysis_result: main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResult = None,
        task_finish: bool = None,
        task_id: str = None,
        task_progress: int = None,
        task_state: str = None,
        task_success: bool = None,
        total_db_count: int = None,
    ):
        # The number of databases that have been analyzed.
        self.analyzed_db_count = analyzed_db_count
        # The details of storage analysis.
        self.storage_analysis_result = storage_analysis_result
        # Indicates whether the task is complete.
        self.task_finish = task_finish
        # The task ID.
        self.task_id = task_id
        # The task progress.
        # 
        # >  Valid values are integers that range from 0 to 100.
        self.task_progress = task_progress
        # The status of the storage analysis task. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **PENDING**: The task is being queued for execution.
        # *   **RECEIVED**: The task is received for execution.
        # *   **RUNNING**: The task is being executed.
        # *   **RETRY**: The task is being retried.
        # *   **SUCCESS**: The task succeeds.
        # *   **FAILURE**: The task fails.
        self.task_state = task_state
        # Indicates whether the task is successful.
        self.task_success = task_success
        # The number of databases that need to be analyzed in the storage analysis task.
        self.total_db_count = total_db_count

    def validate(self):
        if self.storage_analysis_result:
            self.storage_analysis_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzed_db_count is not None:
            result['AnalyzedDbCount'] = self.analyzed_db_count

        if self.storage_analysis_result is not None:
            result['StorageAnalysisResult'] = self.storage_analysis_result.to_map()

        if self.task_finish is not None:
            result['TaskFinish'] = self.task_finish

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_progress is not None:
            result['TaskProgress'] = self.task_progress

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_success is not None:
            result['TaskSuccess'] = self.task_success

        if self.total_db_count is not None:
            result['TotalDbCount'] = self.total_db_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzedDbCount') is not None:
            self.analyzed_db_count = m.get('AnalyzedDbCount')

        if m.get('StorageAnalysisResult') is not None:
            temp_model = main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResult()
            self.storage_analysis_result = temp_model.from_map(m.get('StorageAnalysisResult'))

        if m.get('TaskFinish') is not None:
            self.task_finish = m.get('TaskFinish')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskProgress') is not None:
            self.task_progress = m.get('TaskProgress')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskSuccess') is not None:
            self.task_success = m.get('TaskSuccess')

        if m.get('TotalDbCount') is not None:
            self.total_db_count = m.get('TotalDbCount')

        return self

class GetStorageAnalysisResultResponseBodyDataStorageAnalysisResult(DaraModel):
    def __init__(
        self,
        analysis_error_type: str = None,
        analysis_success: bool = None,
        daily_increment: int = None,
        estimate_available_days: int = None,
        need_optimize_item_list: List[main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultNeedOptimizeItemList] = None,
        table_stats: List[main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultTableStats] = None,
        total_free_storage_size: int = None,
        total_storage_size: int = None,
        total_used_storage_size: int = None,
    ):
        # The reason why the analysis on the database and table fails.
        # 
        # *   **DB_OR_TABLE_NOT_EXIST**: The specified database or table does not exist.
        # *   **DB_NOT_EXIST**: The specified database does not exist.
        self.analysis_error_type = analysis_error_type
        # Indicates whether the analysis on the database and table is successful.
        self.analysis_success = analysis_success
        # The estimated average daily growth of the used storage space in the previous seven days. Unit: bytes.
        self.daily_increment = daily_increment
        # The estimated number of days for which the remaining storage space is available.
        self.estimate_available_days = estimate_available_days
        # The items to be optimized, which are generated based on DAS default rules. You can ignore these items based on your business requirements, and create custom rules to generate items to be optimized based on other basic data that is returned.
        self.need_optimize_item_list = need_optimize_item_list
        # The information about the table.
        self.table_stats = table_stats
        # The size of remaining storage.
        # 
        # >  Unit: bytes.
        self.total_free_storage_size = total_free_storage_size
        # The total size of instance storage.
        # 
        # >  Unit: bytes.
        self.total_storage_size = total_storage_size
        # The size of used storage.
        # 
        # >  Unit: bytes.
        self.total_used_storage_size = total_used_storage_size

    def validate(self):
        if self.need_optimize_item_list:
            for v1 in self.need_optimize_item_list:
                 if v1:
                    v1.validate()
        if self.table_stats:
            for v1 in self.table_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_error_type is not None:
            result['AnalysisErrorType'] = self.analysis_error_type

        if self.analysis_success is not None:
            result['AnalysisSuccess'] = self.analysis_success

        if self.daily_increment is not None:
            result['DailyIncrement'] = self.daily_increment

        if self.estimate_available_days is not None:
            result['EstimateAvailableDays'] = self.estimate_available_days

        result['NeedOptimizeItemList'] = []
        if self.need_optimize_item_list is not None:
            for k1 in self.need_optimize_item_list:
                result['NeedOptimizeItemList'].append(k1.to_map() if k1 else None)

        result['TableStats'] = []
        if self.table_stats is not None:
            for k1 in self.table_stats:
                result['TableStats'].append(k1.to_map() if k1 else None)

        if self.total_free_storage_size is not None:
            result['TotalFreeStorageSize'] = self.total_free_storage_size

        if self.total_storage_size is not None:
            result['TotalStorageSize'] = self.total_storage_size

        if self.total_used_storage_size is not None:
            result['TotalUsedStorageSize'] = self.total_used_storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisErrorType') is not None:
            self.analysis_error_type = m.get('AnalysisErrorType')

        if m.get('AnalysisSuccess') is not None:
            self.analysis_success = m.get('AnalysisSuccess')

        if m.get('DailyIncrement') is not None:
            self.daily_increment = m.get('DailyIncrement')

        if m.get('EstimateAvailableDays') is not None:
            self.estimate_available_days = m.get('EstimateAvailableDays')

        self.need_optimize_item_list = []
        if m.get('NeedOptimizeItemList') is not None:
            for k1 in m.get('NeedOptimizeItemList'):
                temp_model = main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultNeedOptimizeItemList()
                self.need_optimize_item_list.append(temp_model.from_map(k1))

        self.table_stats = []
        if m.get('TableStats') is not None:
            for k1 in m.get('TableStats'):
                temp_model = main_models.GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultTableStats()
                self.table_stats.append(temp_model.from_map(k1))

        if m.get('TotalFreeStorageSize') is not None:
            self.total_free_storage_size = m.get('TotalFreeStorageSize')

        if m.get('TotalStorageSize') is not None:
            self.total_storage_size = m.get('TotalStorageSize')

        if m.get('TotalUsedStorageSize') is not None:
            self.total_used_storage_size = m.get('TotalUsedStorageSize')

        return self

class GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultTableStats(DaraModel):
    def __init__(
        self,
        avg_row_length: int = None,
        data_free: int = None,
        data_size: int = None,
        db_name: str = None,
        engine: str = None,
        fragment_size: int = None,
        index_size: int = None,
        phy_total_size: int = None,
        physical_file_size: int = None,
        table_name: str = None,
        table_rows: int = None,
        table_type: str = None,
        total_size: int = None,
    ):
        # The average length of rows. Unit: bytes.
        self.avg_row_length = avg_row_length
        # The size of space fragments. Unit: bytes.
        # 
        # >  This parameter is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters. The fragmentation rate of a table is generally calculated based on the following formula: `Fragmentation rate = DataFree/(DataSize + IndexSize + DataFree)`. In this topic, `Fragmentation rate = DataFree/PhyTotalSize`.
        self.data_free = data_free
        # *   For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this parameter indicates the amount of space occupied by data. Unit: bytes.
        # *   For ApsaraDB for MongoDB instances, this parameter indicates the size of uncompressed data, that is, the amount of data. Unit: bytes.
        self.data_size = data_size
        # The name of the database.
        self.db_name = db_name
        # The type of the storage engine used by the table.
        # 
        # >  This parameter is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        self.engine = engine
        # The size of space that can be reclaimed. Unit: bytes.
        # 
        # >  This parameter is applicable only to ApsaraDB for MongoDB instances. `Fragmentation rate = FragmentSize/PhyTotalSize`.
        self.fragment_size = fragment_size
        # The storage space occupied by indexes. Unit: bytes.
        self.index_size = index_size
        # The storage space of the table. Unit: bytes.
        # 
        # >  For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, the value of the parameter is the sum of **DataSize**, **IndexSize**, and **DataFree**. For ApsaraDB for MongoDB instances, the value of this parameter is the sum of **DataSize** and **IndexSize**.
        self.phy_total_size = phy_total_size
        # The physical file size of the table. Unit: bytes.
        # 
        # >  This parameter is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters. Data of specific database instances cannot be obtained due to deployment mode.
        self.physical_file_size = physical_file_size
        # The name of the table.
        self.table_name = table_name
        # The number of rows in the table.
        self.table_rows = table_rows
        # The type of the table.
        # 
        # >  This parameter is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        self.table_type = table_type
        # *   For ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters, this parameter indicates the amount of space occupied by table data and indexes. Unit: bytes. The value is the sum of **DataSize** and **IndexSize**.
        # *   For ApsaraDB for MongoDB instances, this parameter indicates the actual size of space allocated by Block Manager. Unit: Bytes. The compression ratio of an ApsaraDB for MongoDB instance is calculated based on the following formula: `Compression ratio = TotalSize/DataSize`.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_row_length is not None:
            result['AvgRowLength'] = self.avg_row_length

        if self.data_free is not None:
            result['DataFree'] = self.data_free

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.fragment_size is not None:
            result['FragmentSize'] = self.fragment_size

        if self.index_size is not None:
            result['IndexSize'] = self.index_size

        if self.phy_total_size is not None:
            result['PhyTotalSize'] = self.phy_total_size

        if self.physical_file_size is not None:
            result['PhysicalFileSize'] = self.physical_file_size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_rows is not None:
            result['TableRows'] = self.table_rows

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgRowLength') is not None:
            self.avg_row_length = m.get('AvgRowLength')

        if m.get('DataFree') is not None:
            self.data_free = m.get('DataFree')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('FragmentSize') is not None:
            self.fragment_size = m.get('FragmentSize')

        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')

        if m.get('PhyTotalSize') is not None:
            self.phy_total_size = m.get('PhyTotalSize')

        if m.get('PhysicalFileSize') is not None:
            self.physical_file_size = m.get('PhysicalFileSize')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableRows') is not None:
            self.table_rows = m.get('TableRows')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class GetStorageAnalysisResultResponseBodyDataStorageAnalysisResultNeedOptimizeItemList(DaraModel):
    def __init__(
        self,
        associated_data: str = None,
        db_name: str = None,
        optimize_advice: str = None,
        optimize_item_name: str = None,
        table_name: str = None,
    ):
        # The data associated with the items to be optimized, which is in the JSON format.
        self.associated_data = associated_data
        # The name of the database.
        self.db_name = db_name
        # The optimization suggestion. Valid values:
        # 
        # *   **NEED_ANALYZE_TABLE**: You can execute the `ANALYZE TABLE` statement on the table during off-peak hours. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **NEED_OPTIMIZE_TABLE**: You can reclaim fragments during off-peak hours.
        # *   **CHANGE_TABLE_ENGINE_IF_NECESSARY**: Change the storage engine type of a table after risk assessment. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **AUTO_INCREMENT_ID_BE_TO_RUN_OUT**: Pay attention to the usage of auto-increment IDs. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **DUPLICATE_INDEX**: Optimize indexes of tables. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **TABLE_SIZE**: Pay attention to the table size. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **TABLE_ROWS_AND_AVG_ROW_LENGTH**: Pay attention to the number of rows in a table and the average row length. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # *   **STORAGE_USED_PERCENT**: Pay attention to the space usage to prevent the instance from being locked if the instance is full.
        self.optimize_advice = optimize_advice
        # The item to be optimized. Valid values:
        # 
        # *   **NEED_ANALYZE_TABLE**: tables whose storage statistics obtained from `information_schema.tables` are 50 GB larger or smaller than the physical file sizes. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **NEED_OPTIMIZE_TABLE**: tables whose space fragments are larger than 6 GB and whose fragmentation rates are greater than 30%. The fragmentation rate of a table is generally calculated based on the following formulas:
        # 
        #     *   ApsaraDB RDS for MySQL and PolarDB for MySQL: `Fragmentation rate = DataFree/(DataSize + IndexSize + DataFree)`. In this topic, PhyTotalSize = DataSize + IndexSize + DataFree. Thus, the fragmentation rate can be calculated based on the following formula: `Fragmentation rate = DataFree/PhyTotalSize`.
        #     *   ApsaraDB for MongoDB: `Fragmentation rate = FragmentSize/PhyTotalSize`.
        # 
        # *   **TABLE_ENGINE**: tables whose storage engines are not InnoDB or XEngine. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **AUTO_INCREMENT_ID_BE_TO_RUN_OUT**: tables whose usages of auto-increment IDs exceed 80%. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **DUPLICATE_INDEX**: tables whose indexes are redundant or duplicate. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **TABLE_SIZE**: single tables whose sizes are larger than 50 GB. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **TABLE_ROWS_AND_AVG_ROW_LENGTH**: single tables that contain more than 5 million rows and whose average row lengths exceed 10 KB. This is applicable only to ApsaraDB RDS for MySQL instances and PolarDB for MySQL clusters.
        # 
        # *   **TOTAL_DATA_FREE**: instances whose reclaimable space is larger than 60 GB and whose total fragmentation rate is larger than 5%.
        # 
        # *   **STORAGE_USED_PERCENT**: instances whose space usage is larger than 90%.
        self.optimize_item_name = optimize_item_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_data is not None:
            result['AssociatedData'] = self.associated_data

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.optimize_advice is not None:
            result['OptimizeAdvice'] = self.optimize_advice

        if self.optimize_item_name is not None:
            result['OptimizeItemName'] = self.optimize_item_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedData') is not None:
            self.associated_data = m.get('AssociatedData')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('OptimizeAdvice') is not None:
            self.optimize_advice = m.get('OptimizeAdvice')

        if m.get('OptimizeItemName') is not None:
            self.optimize_item_name = m.get('OptimizeItemName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

