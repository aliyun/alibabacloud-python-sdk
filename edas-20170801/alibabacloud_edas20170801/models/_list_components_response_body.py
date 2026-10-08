# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListComponentsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        component_list: main_models.ListComponentsResponseBodyComponentList = None,
        message: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        self.component_list = component_list
        # The message that is returned.
        self.message = message

    def validate(self):
        if self.component_list:
            self.component_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.component_list is not None:
            result['ComponentList'] = self.component_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ComponentList') is not None:
            temp_model = main_models.ListComponentsResponseBodyComponentList()
            self.component_list = temp_model.from_map(m.get('ComponentList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ListComponentsResponseBodyComponentList(DaraModel):
    def __init__(
        self,
        component: List[main_models.ListComponentsResponseBodyComponentListComponent] = None,
    ):
        self.component = component

    def validate(self):
        if self.component:
            for v1 in self.component:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Component'] = []
        if self.component is not None:
            for k1 in self.component:
                result['Component'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component = []
        if m.get('Component') is not None:
            for k1 in m.get('Component'):
                temp_model = main_models.ListComponentsResponseBodyComponentListComponent()
                self.component.append(temp_model.from_map(k1))

        return self

class ListComponentsResponseBodyComponentListComponent(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_key: str = None,
        desc: str = None,
        expired: bool = None,
        type: str = None,
        version: str = None,
    ):
        self.component_id = component_id
        self.component_key = component_key
        self.desc = desc
        self.expired = expired
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_key is not None:
            result['ComponentKey'] = self.component_key

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

