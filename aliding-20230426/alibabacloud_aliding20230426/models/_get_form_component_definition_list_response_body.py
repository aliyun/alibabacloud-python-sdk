# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetFormComponentDefinitionListResponseBody(DaraModel):
    def __init__(
        self,
        result: List[main_models.GetFormComponentDefinitionListResponseBodyResult] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.result = result
        self.request_id = request_id
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
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetFormComponentDefinitionListResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetFormComponentDefinitionListResponseBodyResult(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        field_id: str = None,
        label: str = None,
        parent_id: str = None,
    ):
        self.component_name = component_name
        self.field_id = field_id
        self.label = label
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.label is not None:
            result['Label'] = self.label

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

