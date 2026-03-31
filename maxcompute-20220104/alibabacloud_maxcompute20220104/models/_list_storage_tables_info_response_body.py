# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListStorageTablesInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListStorageTablesInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListStorageTablesInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListStorageTablesInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_table_info_list: List[main_models.ListStorageTablesInfoResponseBodyDataStorageTableInfoList] = None,
        total_count: int = None,
    ):
        # The date on which the statistics are collected.
        self.date = date
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The table storage information.
        self.storage_table_info_list = storage_table_info_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.storage_table_info_list:
            for v1 in self.storage_table_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['storageTableInfoList'] = []
        if self.storage_table_info_list is not None:
            for k1 in self.storage_table_info_list:
                result['storageTableInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.storage_table_info_list = []
        if m.get('storageTableInfoList') is not None:
            for k1 in m.get('storageTableInfoList'):
                temp_model = main_models.ListStorageTablesInfoResponseBodyDataStorageTableInfoList()
                self.storage_table_info_list.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListStorageTablesInfoResponseBodyDataStorageTableInfoList(DaraModel):
    def __init__(
        self,
        date: str = None,
        is_partitioned: bool = None,
        last_access_time: int = None,
        long_term_storage: float = None,
        long_term_storage_file_count: int = None,
        long_term_storage_unit: str = None,
        low_freq_storage: float = None,
        low_freq_storage_file_count: int = None,
        low_freq_storage_unit: str = None,
        project_name: str = None,
        rate: float = None,
        schema_name: str = None,
        standard_storage: float = None,
        standard_storage_file_count: int = None,
        standard_storage_unit: str = None,
        storage_type: str = None,
        table_name: str = None,
        total_frequency: int = None,
        total_input_amount: float = None,
        total_input_amount_unit: str = None,
        total_storage: float = None,
        total_storage_file_count: int = None,
        total_storage_unit: str = None,
    ):
        # The date on which the statistics are collected. This value is not returned.
        self.date = date
        # Indicates whether the table is a partitioned table.
        self.is_partitioned = is_partitioned
        # The time when the table was last accessed. This value is returned when the table is a non-partitioned table.
        # 
        # >  The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the last access time cannot be collected.
        self.last_access_time = last_access_time
        # The storage usage at the long-term storage tier.
        self.long_term_storage = long_term_storage
        # The number of long-term storage files.
        self.long_term_storage_file_count = long_term_storage_file_count
        # The unit of the storage usage at the long-term storage tier.
        self.long_term_storage_unit = long_term_storage_unit
        # The storage usage at the low-frequency tier.
        self.low_freq_storage = low_freq_storage
        # The number of low-frequency storage files.
        self.low_freq_storage_file_count = low_freq_storage_file_count
        # The unit of the storage usage at the low-frequency storage tier.
        self.low_freq_storage_unit = low_freq_storage_unit
        # The project name.
        self.project_name = project_name
        # The change rate of the total storage usage compared with that of the recent {$recentDays} days.
        self.rate = rate
        # The schema name.
        self.schema_name = schema_name
        # The storage usage at the standard storage tier.
        self.standard_storage = standard_storage
        # The number of standard storage files.
        self.standard_storage_file_count = standard_storage_file_count
        # The unit of the storage usage at the standard storage tier.
        self.standard_storage_unit = standard_storage_unit
        # The table storage type.
        # 
        # *   standard
        # *   lowfrequency
        # *   longterm
        # *   unknown: This value is returned when the table is a partitioned table. You can call the ListStoragePartitionsInfo operation to query the storage type of each partition.
        self.storage_type = storage_type
        # The table name.
        self.table_name = table_name
        # The access frequency.
        # 
        # > 
        # 
        # *   Access behaviors include:
        # 
        # *   The table is used as the input table of an SQL task.
        # *   The table is downloaded by Tunnel.
        # *   The table is read by calling the Storage API. The partition granularity of the partitioned table is not available. Each time an access operation is performed, the access frequency is incremented by 1.
        # 
        # *   The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the access frequency cannot be collected.
        self.total_frequency = total_frequency
        # The total amount of accessed data.
        # 
        # >  The amount of data that is read by all access behaviors.
        self.total_input_amount = total_input_amount
        # The unit of the total amount of accessed data.
        self.total_input_amount_unit = total_input_amount_unit
        # The total storage usage. For a partitioned table, this parameter indicates the sum of the storage usage of all partitions. If the storage types of partitions are different, the value is the sum of the storage usage of each storage type.
        self.total_storage = total_storage
        # The total number of files.
        self.total_storage_file_count = total_storage_file_count
        # The unit of storage usage.
        self.total_storage_unit = total_storage_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['date'] = self.date

        if self.is_partitioned is not None:
            result['isPartitioned'] = self.is_partitioned

        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time

        if self.long_term_storage is not None:
            result['longTermStorage'] = self.long_term_storage

        if self.long_term_storage_file_count is not None:
            result['longTermStorageFileCount'] = self.long_term_storage_file_count

        if self.long_term_storage_unit is not None:
            result['longTermStorageUnit'] = self.long_term_storage_unit

        if self.low_freq_storage is not None:
            result['lowFreqStorage'] = self.low_freq_storage

        if self.low_freq_storage_file_count is not None:
            result['lowFreqStorageFileCount'] = self.low_freq_storage_file_count

        if self.low_freq_storage_unit is not None:
            result['lowFreqStorageUnit'] = self.low_freq_storage_unit

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.rate is not None:
            result['rate'] = self.rate

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        if self.standard_storage is not None:
            result['standardStorage'] = self.standard_storage

        if self.standard_storage_file_count is not None:
            result['standardStorageFileCount'] = self.standard_storage_file_count

        if self.standard_storage_unit is not None:
            result['standardStorageUnit'] = self.standard_storage_unit

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.total_frequency is not None:
            result['totalFrequency'] = self.total_frequency

        if self.total_input_amount is not None:
            result['totalInputAmount'] = self.total_input_amount

        if self.total_input_amount_unit is not None:
            result['totalInputAmountUnit'] = self.total_input_amount_unit

        if self.total_storage is not None:
            result['totalStorage'] = self.total_storage

        if self.total_storage_file_count is not None:
            result['totalStorageFileCount'] = self.total_storage_file_count

        if self.total_storage_unit is not None:
            result['totalStorageUnit'] = self.total_storage_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('isPartitioned') is not None:
            self.is_partitioned = m.get('isPartitioned')

        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')

        if m.get('longTermStorage') is not None:
            self.long_term_storage = m.get('longTermStorage')

        if m.get('longTermStorageFileCount') is not None:
            self.long_term_storage_file_count = m.get('longTermStorageFileCount')

        if m.get('longTermStorageUnit') is not None:
            self.long_term_storage_unit = m.get('longTermStorageUnit')

        if m.get('lowFreqStorage') is not None:
            self.low_freq_storage = m.get('lowFreqStorage')

        if m.get('lowFreqStorageFileCount') is not None:
            self.low_freq_storage_file_count = m.get('lowFreqStorageFileCount')

        if m.get('lowFreqStorageUnit') is not None:
            self.low_freq_storage_unit = m.get('lowFreqStorageUnit')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        if m.get('standardStorage') is not None:
            self.standard_storage = m.get('standardStorage')

        if m.get('standardStorageFileCount') is not None:
            self.standard_storage_file_count = m.get('standardStorageFileCount')

        if m.get('standardStorageUnit') is not None:
            self.standard_storage_unit = m.get('standardStorageUnit')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('totalFrequency') is not None:
            self.total_frequency = m.get('totalFrequency')

        if m.get('totalInputAmount') is not None:
            self.total_input_amount = m.get('totalInputAmount')

        if m.get('totalInputAmountUnit') is not None:
            self.total_input_amount_unit = m.get('totalInputAmountUnit')

        if m.get('totalStorage') is not None:
            self.total_storage = m.get('totalStorage')

        if m.get('totalStorageFileCount') is not None:
            self.total_storage_file_count = m.get('totalStorageFileCount')

        if m.get('totalStorageUnit') is not None:
            self.total_storage_unit = m.get('totalStorageUnit')

        return self

