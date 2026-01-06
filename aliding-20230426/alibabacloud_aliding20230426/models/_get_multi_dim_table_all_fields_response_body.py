# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetMultiDimTableAllFieldsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        value: List[main_models.GetMultiDimTableAllFieldsResponseBodyValue] = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.value = value
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.value:
            for v1 in self.value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['value'] = []
        if self.value is not None:
            for k1 in self.value:
                result['value'].append(k1.to_map() if k1 else None)

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.value = []
        if m.get('value') is not None:
            for k1 in m.get('value'):
                temp_model = main_models.GetMultiDimTableAllFieldsResponseBodyValue()
                self.value.append(temp_model.from_map(k1))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetMultiDimTableAllFieldsResponseBodyValue(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        property: Dict[str, Any] = None,
        type: str = None,
    ):
        self.id = id
        self.name = name
        self.property = property
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.property is not None:
            result['Property'] = self.property

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Property') is not None:
            self.property = m.get('Property')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

