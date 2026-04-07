# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaTableColumnResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaTableColumnResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
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
            temp_model = main_models.GetMetaTableColumnResponseBodyData()
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

class GetMetaTableColumnResponseBodyData(DaraModel):
    def __init__(
        self,
        column_list: List[main_models.GetMetaTableColumnResponseBodyDataColumnList] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The information about fields.
        self.column_list = column_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of fields.
        self.total_count = total_count

    def validate(self):
        if self.column_list:
            for v1 in self.column_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnList'] = []
        if self.column_list is not None:
            for k1 in self.column_list:
                result['ColumnList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_list = []
        if m.get('ColumnList') is not None:
            for k1 in m.get('ColumnList'):
                temp_model = main_models.GetMetaTableColumnResponseBodyDataColumnList()
                self.column_list.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMetaTableColumnResponseBodyDataColumnList(DaraModel):
    def __init__(
        self,
        caption: str = None,
        column_guid: str = None,
        column_name: str = None,
        column_type: str = None,
        comment: str = None,
        is_foreign_key: bool = None,
        is_partition_column: bool = None,
        is_primary_key: bool = None,
        position: int = None,
        relation_count: int = None,
    ):
        # The description of the field.
        self.caption = caption
        # The GUID of the field.
        self.column_guid = column_guid
        # The name of the field.
        self.column_name = column_name
        # The data type of the field.
        self.column_type = column_type
        # The remarks of the field.
        self.comment = comment
        # Indicates whether the field is a foreign key. Valid values:
        # 
        # *   true
        # *   false
        self.is_foreign_key = is_foreign_key
        # Indicates whether the field is a partition field. Valid values:
        # 
        # *   true
        # *   false
        self.is_partition_column = is_partition_column
        # Indicates whether the field is a primary key. Valid values:
        # 
        # *   true
        # *   false
        self.is_primary_key = is_primary_key
        # The sequence number of the field.
        self.position = position
        # The number of times the field is read.
        self.relation_count = relation_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.column_guid is not None:
            result['ColumnGuid'] = self.column_guid

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.is_foreign_key is not None:
            result['IsForeignKey'] = self.is_foreign_key

        if self.is_partition_column is not None:
            result['IsPartitionColumn'] = self.is_partition_column

        if self.is_primary_key is not None:
            result['IsPrimaryKey'] = self.is_primary_key

        if self.position is not None:
            result['Position'] = self.position

        if self.relation_count is not None:
            result['RelationCount'] = self.relation_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('ColumnGuid') is not None:
            self.column_guid = m.get('ColumnGuid')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('IsForeignKey') is not None:
            self.is_foreign_key = m.get('IsForeignKey')

        if m.get('IsPartitionColumn') is not None:
            self.is_partition_column = m.get('IsPartitionColumn')

        if m.get('IsPrimaryKey') is not None:
            self.is_primary_key = m.get('IsPrimaryKey')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('RelationCount') is not None:
            self.relation_count = m.get('RelationCount')

        return self

