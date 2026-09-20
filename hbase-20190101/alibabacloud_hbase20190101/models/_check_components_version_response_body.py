# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class CheckComponentsVersionResponseBody(DaraModel):
    def __init__(
        self,
        components: main_models.CheckComponentsVersionResponseBodyComponents = None,
        request_id: str = None,
    ):
        self.components = components
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.components:
            self.components.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.components is not None:
            result['Components'] = self.components.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            temp_model = main_models.CheckComponentsVersionResponseBodyComponents()
            self.components = temp_model.from_map(m.get('Components'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckComponentsVersionResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component: List[main_models.CheckComponentsVersionResponseBodyComponentsComponent] = None,
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
                temp_model = main_models.CheckComponentsVersionResponseBodyComponentsComponent()
                self.component.append(temp_model.from_map(k1))

        return self



class CheckComponentsVersionResponseBodyComponentsComponent(DaraModel):
    def __init__(
        self,
        component: str = None,
        is_latest_version: str = None,
    ):
        self.component = component
        self.is_latest_version = is_latest_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component is not None:
            result['Component'] = self.component

        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')

        return self

