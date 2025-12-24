# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListTenantAddonsResponseBody(DaraModel):
    def __init__(
        self,
        addons: List[main_models.ListTenantAddonsResponseBodyAddons] = None,
        request_id: str = None,
    ):
        # The information about the plug-in.
        self.addons = addons
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.ListTenantAddonsResponseBodyAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTenantAddonsResponseBodyAddons(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        name: str = None,
    ):
        # The attributes of the plug-in.
        self.attributes = attributes
        # The name of the plug-in.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

