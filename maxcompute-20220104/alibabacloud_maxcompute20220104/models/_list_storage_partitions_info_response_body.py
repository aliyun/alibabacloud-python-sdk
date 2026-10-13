# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListStoragePartitionsInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListStoragePartitionsInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. Valid values:
        # - 1xx: Informational response. The request was received and is being processed.
        # - 2xx: Success. The request was successfully received, understood, and accepted by the server.
        # - 3xx: Redirection. The request was redirected, and further action is required to complete it.
        # - 4xx: Client error. The request contains bad syntax, invalid parameters, or cannot be fulfilled.
        # - 5xx: Server error. The server failed to fulfill the request due to other reasons.
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
            temp_model = main_models.ListStoragePartitionsInfoResponseBodyData()
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

class ListStoragePartitionsInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_partition_info_list: List[main_models.ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList] = None,
        total_count: int = None,
    ):
        # The statistical date. The format is YYYYMMDD.
        self.date = date
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of partition storage information.
        self.storage_partition_info_list = storage_partition_info_list
        # The total number of returned results.
        self.total_count = total_count

    def validate(self):
        if self.storage_partition_info_list:
            for v1 in self.storage_partition_info_list:
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

        result['storagePartitionInfoList'] = []
        if self.storage_partition_info_list is not None:
            for k1 in self.storage_partition_info_list:
                result['storagePartitionInfoList'].append(k1.to_map() if k1 else None)

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

        self.storage_partition_info_list = []
        if m.get('storagePartitionInfoList') is not None:
            for k1 in m.get('storagePartitionInfoList'):
                temp_model = main_models.ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList()
                self.storage_partition_info_list.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList(DaraModel):
    def __init__(
        self,
        file_count: int = None,
        file_size: float = None,
        file_size_unit: str = None,
        is_partitioned: bool = None,
        last_access_time: int = None,
        partition: str = None,
        project_name: str = None,
        rate: float = None,
        schema_name: str = None,
        storage_type: str = None,
        table_name: str = None,
        total_frequency: int = None,
        total_input_amount: float = None,
        total_input_amount_unit: str = None,
        type: str = None,
    ):
        # The number of files.
        self.file_count = file_count
        # The storage size.
        self.file_size = file_size
        # The unit of the storage size.
        self.file_size_unit = file_size_unit
        # Indicates whether the table is partitioned. This API operation returns only partition information. You can ignore this field.
        self.is_partitioned = is_partitioned
        # The last access time of the data in the partition.
        # > The collection of this data has been gradually upgraded since July 2023. The last_access_time cannot be collected if the partition has not been accessed after the upgrade or if it is accessed through ALGO jobs or Hologres direct read.
        self.last_access_time = last_access_time
        # The partition name.
        self.partition = partition
        # The project name.
        self.project_name = project_name
        # The year-over-year comparison of the total storage capacity over the recent {$recentDays} days. This API operation does not return this value.
        self.rate = rate
        # The schema name.
        self.schema_name = schema_name
        # The storage type. Valid values:
        # - standard: Standard storage.
        # - lowfrequency: Low-frequency storage.
        # - longterm: Long-term storage.
        self.storage_type = storage_type
        # The table name.
        self.table_name = table_name
        # The access frequency.
        # > - Access behaviors include:
        # >> - The table is used as an input table in SQL computing tasks.
        # >> - The table is downloaded by using Tunnel.
        # >> - The table is read by calling the Read operation of StorageAPI (partition-level data for partitioned tables is currently unavailable). The access frequency increases by 1 for each additional access.
        # > - The statistics for this data have been gradually upgraded since July 2023. Accesses that did not occur after the upgrade or accesses made through ALGO jobs or Hologres direct read cannot be counted in the access frequency.
        self.total_frequency = total_frequency
        # The total amount of accessed data.
        # > The amount of data read by all access behaviors.
        self.total_input_amount = total_input_amount
        # The unit of the total amount of accessed data.
        self.total_input_amount_unit = total_input_amount_unit
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count is not None:
            result['fileCount'] = self.file_count

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.file_size_unit is not None:
            result['fileSizeUnit'] = self.file_size_unit

        if self.is_partitioned is not None:
            result['isPartitioned'] = self.is_partitioned

        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time

        if self.partition is not None:
            result['partition'] = self.partition

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.rate is not None:
            result['rate'] = self.rate

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

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

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('fileSizeUnit') is not None:
            self.file_size_unit = m.get('fileSizeUnit')

        if m.get('isPartitioned') is not None:
            self.is_partitioned = m.get('isPartitioned')

        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')

        if m.get('partition') is not None:
            self.partition = m.get('partition')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

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

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

