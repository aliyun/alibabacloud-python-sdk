# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetKgRelationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        relation_info: main_models.GetKgRelationResponseBodyRelationInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.relation_info = relation_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.relation_info:
            self.relation_info.validate()

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

        if self.relation_info is not None:
            result['RelationInfo'] = self.relation_info.to_map()

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

        if m.get('RelationInfo') is not None:
            temp_model = main_models.GetKgRelationResponseBodyRelationInfo()
            self.relation_info = temp_model.from_map(m.get('RelationInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKgRelationResponseBodyRelationInfo(DaraModel):
    def __init__(
        self,
        property_list: List[main_models.GetKgRelationResponseBodyRelationInfoPropertyList] = None,
        relation_id: str = None,
        relation_type: str = None,
        source_entity_id: str = None,
        target_entity_id: str = None,
    ):
        self.property_list = property_list
        self.relation_id = relation_id
        self.relation_type = relation_type
        self.source_entity_id = source_entity_id
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
                temp_model = main_models.GetKgRelationResponseBodyRelationInfoPropertyList()
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

class GetKgRelationResponseBodyRelationInfoPropertyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_type: str = None,
        value: str = None,
    ):
        self.code = code
        self.data_type = data_type
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

