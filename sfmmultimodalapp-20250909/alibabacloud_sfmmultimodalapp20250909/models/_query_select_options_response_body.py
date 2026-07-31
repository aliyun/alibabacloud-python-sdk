# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class QuerySelectOptionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        select_options: List[main_models.QuerySelectOptionsResponseBodySelectOptions] = None,
    ):
        self.request_id = request_id
        self.select_options = select_options

    def validate(self):
        if self.select_options:
            for v1 in self.select_options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SelectOptions'] = []
        if self.select_options is not None:
            for k1 in self.select_options:
                result['SelectOptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.select_options = []
        if m.get('SelectOptions') is not None:
            for k1 in m.get('SelectOptions'):
                temp_model = main_models.QuerySelectOptionsResponseBodySelectOptions()
                self.select_options.append(temp_model.from_map(k1))

        return self

class QuerySelectOptionsResponseBodySelectOptions(DaraModel):
    def __init__(
        self,
        biz_config: Dict[str, Any] = None,
        category: str = None,
        children: List[main_models.QuerySelectOptionsResponseBodySelectOptionsChildren] = None,
        description: str = None,
        label: str = None,
        tags: List[str] = None,
        value: str = None,
    ):
        self.biz_config = biz_config
        self.category = category
        self.children = children
        self.description = description
        self.label = label
        self.tags = tags
        self.value = value

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_config is not None:
            result['BizConfig'] = self.biz_config

        if self.category is not None:
            result['Category'] = self.category

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.QuerySelectOptionsResponseBodySelectOptionsChildren()
                self.children.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QuerySelectOptionsResponseBodySelectOptionsChildren(DaraModel):
    def __init__(
        self,
        biz_config: Dict[str, Any] = None,
        category: str = None,
        description: str = None,
        label: str = None,
        tags: List[str] = None,
        value: str = None,
    ):
        self.biz_config = biz_config
        self.category = category
        self.description = description
        self.label = label
        self.tags = tags
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_config is not None:
            result['BizConfig'] = self.biz_config

        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

