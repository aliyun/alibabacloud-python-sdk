# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetFieldDefByUuidResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetFieldDefByUuidResponseBodyResult] = None,
        success: bool = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.GetFieldDefByUuidResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetFieldDefByUuidResponseBodyResult(DaraModel):
    def __init__(
        self,
        behavior: str = None,
        children: str = None,
        component_name: str = None,
        field_id: str = None,
        label: Any = None,
        props: Any = None,
        success: bool = None,
    ):
        self.behavior = behavior
        self.children = children
        self.component_name = component_name
        self.field_id = field_id
        self.label = label
        self.props = props
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior is not None:
            result['Behavior'] = self.behavior

        if self.children is not None:
            result['Children'] = self.children

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.label is not None:
            result['Label'] = self.label

        if self.props is not None:
            result['Props'] = self.props

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')

        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Props') is not None:
            self.props = m.get('Props')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

