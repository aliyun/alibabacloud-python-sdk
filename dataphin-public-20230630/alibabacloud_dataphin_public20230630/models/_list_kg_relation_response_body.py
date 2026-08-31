# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListKgRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListKgRelationResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paged query result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListKgRelationResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListKgRelationResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        relation_list: List[main_models.ListKgRelationResponseBodyPageResultRelationList] = None,
        total_count: int = None,
    ):
        # The list of paged relationship records.
        self.relation_list = relation_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.relation_list:
            for v1 in self.relation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RelationList'] = []
        if self.relation_list is not None:
            for k1 in self.relation_list:
                result['RelationList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.relation_list = []
        if m.get('RelationList') is not None:
            for k1 in m.get('RelationList'):
                temp_model = main_models.ListKgRelationResponseBodyPageResultRelationList()
                self.relation_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKgRelationResponseBodyPageResultRelationList(DaraModel):
    def __init__(
        self,
        property_list: List[main_models.ListKgRelationResponseBodyPageResultRelationListPropertyList] = None,
        relation_id: str = None,
        relation_type: str = None,
        source_entity_id: str = None,
        target_entity_id: str = None,
    ):
        # The list of properties for the relationship record.
        self.property_list = property_list
        # The relationship record ID.
        self.relation_id = relation_id
        # The relationship type code.
        self.relation_type = relation_type
        # The source entity ID.
        self.source_entity_id = source_entity_id
        # The target entity ID.
        self.target_entity_id = target_entity_id

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.source_entity_id is not None:
            result['SourceEntityId'] = self.source_entity_id

        if self.target_entity_id is not None:
            result['TargetEntityId'] = self.target_entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.ListKgRelationResponseBodyPageResultRelationListPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('SourceEntityId') is not None:
            self.source_entity_id = m.get('SourceEntityId')

        if m.get('TargetEntityId') is not None:
            self.target_entity_id = m.get('TargetEntityId')

        return self

class ListKgRelationResponseBodyPageResultRelationListPropertyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_type: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The data type of the property. Valid values: STRING (string), INTEGER (integer), FLOAT (floating-point number), BOOLEAN (Boolean), DATE (date), and LIST (list).
        self.data_type = data_type
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

