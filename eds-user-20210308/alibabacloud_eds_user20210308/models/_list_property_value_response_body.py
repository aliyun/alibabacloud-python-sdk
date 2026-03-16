# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class ListPropertyValueResponseBody(DaraModel):
    def __init__(
        self,
        property_value_infos: List[main_models.ListPropertyValueResponseBodyPropertyValueInfos] = None,
        request_id: str = None,
    ):
        # Details about property values.
        self.property_value_infos = property_value_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.property_value_infos:
            for v1 in self.property_value_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyValueInfos'] = []
        if self.property_value_infos is not None:
            for k1 in self.property_value_infos:
                result['PropertyValueInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_value_infos = []
        if m.get('PropertyValueInfos') is not None:
            for k1 in m.get('PropertyValueInfos'):
                temp_model = main_models.ListPropertyValueResponseBodyPropertyValueInfos()
                self.property_value_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPropertyValueResponseBodyPropertyValueInfos(DaraModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        # The value of the property.
        self.property_value = property_value
        # The ID of the property value.
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')

        return self

