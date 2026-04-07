# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaColumnLineageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaColumnLineageResponseBodyData = None,
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
            temp_model = main_models.GetMetaColumnLineageResponseBodyData()
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

class GetMetaColumnLineageResponseBodyData(DaraModel):
    def __init__(
        self,
        data_entity_list: List[main_models.GetMetaColumnLineageResponseBodyDataDataEntityList] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The returned result.
        self.data_entity_list = data_entity_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of fields.
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

        if self.page_num is not None:
            result['PageNum'] = self.page_num

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
                temp_model = main_models.GetMetaColumnLineageResponseBodyDataDataEntityList()
                self.data_entity_list.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMetaColumnLineageResponseBodyDataDataEntityList(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_guid: str = None,
        column_name: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        # The EMR cluster ID.
        self.cluster_id = cluster_id
        # The unique identifier of the field.
        self.column_guid = column_guid
        # The name of the field.
        self.column_name = column_name
        # The name of the database.
        self.database_name = database_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.column_guid is not None:
            result['ColumnGuid'] = self.column_guid

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ColumnGuid') is not None:
            self.column_guid = m.get('ColumnGuid')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

