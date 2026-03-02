# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PreviewComponentCrdSchemaCmd(DaraModel):
    def __init__(
        self,
        address: str = None,
        configuration: List[main_models.ConfigModel] = None,
        credentials: str = None,
        id: int = None,
        is_custom: bool = None,
        name: str = None,
        reesource_version: str = None,
        resource_id: int = None,
        scope: str = None,
        template_id: int = None,
        type: str = None,
    ):
        self.address = address
        self.configuration = configuration
        self.credentials = credentials
        self.id = id
        self.is_custom = is_custom
        self.name = name
        self.reesource_version = reesource_version
        self.resource_id = resource_id
        self.scope = scope
        self.template_id = template_id
        self.type = type

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        result['configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['configuration'].append(k1.to_map() if k1 else None)

        if self.credentials is not None:
            result['credentials'] = self.credentials

        if self.id is not None:
            result['id'] = self.id

        if self.is_custom is not None:
            result['isCustom'] = self.is_custom

        if self.name is not None:
            result['name'] = self.name

        if self.reesource_version is not None:
            result['reesourceVersion'] = self.reesource_version

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.scope is not None:
            result['scope'] = self.scope

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        self.configuration = []
        if m.get('configuration') is not None:
            for k1 in m.get('configuration'):
                temp_model = main_models.ConfigModel()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('credentials') is not None:
            self.credentials = m.get('credentials')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isCustom') is not None:
            self.is_custom = m.get('isCustom')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('reesourceVersion') is not None:
            self.reesource_version = m.get('reesourceVersion')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

