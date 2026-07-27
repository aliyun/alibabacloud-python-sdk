# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetKgEntityResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        entity_info: main_models.GetKgEntityResponseBodyEntityInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.entity_info = entity_info
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.entity_info:
            self.entity_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.entity_info is not None:
            result['EntityInfo'] = self.entity_info.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('EntityInfo') is not None:
            temp_model = main_models.GetKgEntityResponseBodyEntityInfo()
            self.entity_info = temp_model.from_map(m.get('EntityInfo'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKgEntityResponseBodyEntityInfo(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        property_list: List[main_models.GetKgEntityResponseBodyEntityInfoPropertyList] = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.property_list = property_list

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
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.GetKgEntityResponseBodyEntityInfoPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        return self

class GetKgEntityResponseBodyEntityInfoPropertyList(DaraModel):
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

