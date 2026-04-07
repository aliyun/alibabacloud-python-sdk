# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTablePartitionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaTablePartitionResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetaTablePartitionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMetaTablePartitionResponseBodyData(DaraModel):
    def __init__(
        self,
        data_entity_list: List[main_models.GetMetaTablePartitionResponseBodyDataDataEntityList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of partitions.
        self.data_entity_list = data_entity_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of partitions.
        self.total_count = total_count

    def validate(self):
        if self.data_entity_list:
            for v1 in self.data_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataEntityList'] = []
        if self.data_entity_list is not None:
            for k1 in self.data_entity_list:
                result['DataEntityList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_entity_list = []
        if m.get('DataEntityList') is not None:
            for k1 in m.get('DataEntityList'):
                temp_model = main_models.GetMetaTablePartitionResponseBodyDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMetaTablePartitionResponseBodyDataDataEntityList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        data_size: int = None,
        modified_time: int = None,
        partition_guid: str = None,
        partition_location: str = None,
        partition_name: str = None,
        partition_path: str = None,
        partition_type: str = None,
        record_count: int = None,
        table_guid: str = None,
    ):
        # The comment.
        self.comment = comment
        # The time when the partition was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.create_time = create_time
        # The size of the partition. Unit: bytes.
        self.data_size = data_size
        # The time when the partition was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.modified_time = modified_time
        # The GUID of the partition.
        self.partition_guid = partition_guid
        # The location of the Hive partition.
        self.partition_location = partition_location
        # The name of the partition.
        self.partition_name = partition_name
        # The path of the partition.
        self.partition_path = partition_path
        # The type of the partition.
        self.partition_type = partition_type
        # The number of entries in the partition.
        self.record_count = record_count
        # The unique identifier of the metatable.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.partition_guid is not None:
            result['PartitionGuid'] = self.partition_guid

        if self.partition_location is not None:
            result['PartitionLocation'] = self.partition_location

        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name

        if self.partition_path is not None:
            result['PartitionPath'] = self.partition_path

        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PartitionGuid') is not None:
            self.partition_guid = m.get('PartitionGuid')

        if m.get('PartitionLocation') is not None:
            self.partition_location = m.get('PartitionLocation')

        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')

        if m.get('PartitionPath') is not None:
            self.partition_path = m.get('PartitionPath')

        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

