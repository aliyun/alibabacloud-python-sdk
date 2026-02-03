# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class ListNisInspectionResourceTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_list: List[main_models.ListNisInspectionResourceTypeResponseBodyResourceTypeList] = None,
    ):
        self.request_id = request_id
        self.resource_type_list = resource_type_list

    def validate(self):
        if self.resource_type_list:
            for v1 in self.resource_type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceTypeList'] = []
        if self.resource_type_list is not None:
            for k1 in self.resource_type_list:
                result['ResourceTypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_type_list = []
        if m.get('ResourceTypeList') is not None:
            for k1 in m.get('ResourceTypeList'):
                temp_model = main_models.ListNisInspectionResourceTypeResponseBodyResourceTypeList()
                self.resource_type_list.append(temp_model.from_map(k1))

        return self

class ListNisInspectionResourceTypeResponseBodyResourceTypeList(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

