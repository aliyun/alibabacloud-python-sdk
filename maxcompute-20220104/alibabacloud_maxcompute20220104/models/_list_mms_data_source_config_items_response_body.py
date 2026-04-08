# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsDataSourceConfigItemsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListMmsDataSourceConfigItemsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListMmsDataSourceConfigItemsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsDataSourceConfigItemsResponseBodyData(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enums: List[str] = None,
        group: str = None,
        key: str = None,
        name: str = None,
        place_holder: str = None,
        required: bool = None,
        sub_items: Dict[str, Any] = None,
        sub_type: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.desc = desc
        self.enums = enums
        self.group = group
        self.key = key
        self.name = name
        self.place_holder = place_holder
        self.required = required
        self.sub_items = sub_items
        self.sub_type = sub_type
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.enums is not None:
            result['enums'] = self.enums

        if self.group is not None:
            result['group'] = self.group

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.place_holder is not None:
            result['placeHolder'] = self.place_holder

        if self.required is not None:
            result['required'] = self.required

        if self.sub_items is not None:
            result['subItems'] = self.sub_items

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('enums') is not None:
            self.enums = m.get('enums')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('placeHolder') is not None:
            self.place_holder = m.get('placeHolder')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('subItems') is not None:
            self.sub_items = m.get('subItems')

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

