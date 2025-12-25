# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTablesInCategoryResponseBody(DaraModel):
    def __init__(
        self,
        entity_list: main_models.ListTablesInCategoryResponseBodyEntityList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # List of table information associated with the asset category.
        self.entity_list = entity_list
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request succeeded.
        # *   **false**: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.entity_list:
            self.entity_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_list is not None:
            result['EntityList'] = self.entity_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityList') is not None:
            temp_model = main_models.ListTablesInCategoryResponseBodyEntityList()
            self.entity_list = temp_model.from_map(m.get('EntityList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTablesInCategoryResponseBodyEntityList(DaraModel):
    def __init__(
        self,
        meta_category_table_entity: List[main_models.MetaCategoryTableEntity] = None,
    ):
        self.meta_category_table_entity = meta_category_table_entity

    def validate(self):
        if self.meta_category_table_entity:
            for v1 in self.meta_category_table_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetaCategoryTableEntity'] = []
        if self.meta_category_table_entity is not None:
            for k1 in self.meta_category_table_entity:
                result['MetaCategoryTableEntity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta_category_table_entity = []
        if m.get('MetaCategoryTableEntity') is not None:
            for k1 in m.get('MetaCategoryTableEntity'):
                temp_model = main_models.MetaCategoryTableEntity()
                self.meta_category_table_entity.append(temp_model.from_map(k1))

        return self

