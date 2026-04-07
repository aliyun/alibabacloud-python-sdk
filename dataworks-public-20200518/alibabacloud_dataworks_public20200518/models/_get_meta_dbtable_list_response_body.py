# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaDBTableListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaDBTableListResponseBodyData = None,
        request_id: str = None,
    ):
        # The metatable information in a compute engine instance.
        self.data = data
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetaDBTableListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMetaDBTableListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        table_entity_list: List[main_models.GetMetaDBTableListResponseBodyDataTableEntityList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of metatables in the compute engine instance.
        self.table_entity_list = table_entity_list
        # The total number of compute engine instances returned.
        self.total_count = total_count

    def validate(self):
        if self.table_entity_list:
            for v1 in self.table_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['TableEntityList'] = []
        if self.table_entity_list is not None:
            for k1 in self.table_entity_list:
                result['TableEntityList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.table_entity_list = []
        if m.get('TableEntityList') is not None:
            for k1 in m.get('TableEntityList'):
                temp_model = main_models.GetMetaDBTableListResponseBodyDataTableEntityList()
                self.table_entity_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetMetaDBTableListResponseBodyDataTableEntityList(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The name of the metadatabase.
        self.database_name = database_name
        # The GUID of the metatable.
        self.table_guid = table_guid
        # The name of the metatable.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

