# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateParameterRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        owner: str = None,
        properties: List[main_models.UpdateParameterRequestProperties] = None,
    ):
        self.description = description
        # This parameter is required.
        self.id = id
        self.owner = owner
        self.properties = properties

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.owner is not None:
            result['Owner'] = self.owner

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.UpdateParameterRequestProperties()
                self.properties.append(temp_model.from_map(k1))

        return self

class UpdateParameterRequestProperties(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        value: str = None,
    ):
        self.env_type = env_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

