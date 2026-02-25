# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class UpdateParameterSetAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: List[main_models.UpdateParameterSetAttributeRequestParameters] = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        self.parameters = parameters

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.UpdateParameterSetAttributeRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class UpdateParameterSetAttributeRequestParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        status: str = None,
        type: str = None,
        value: str = None,
    ):
        self.name = name
        self.status = status
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

