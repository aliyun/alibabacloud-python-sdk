# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PdpComponent(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        configuration: List[main_models.ConfigModel] = None,
        description: str = None,
        env: str = None,
        id: int = None,
        is_custom: bool = None,
        name: str = None,
        product_id: int = None,
        request_id: str = None,
        resource_id: int = None,
        resource_type: str = None,
        scope: str = None,
        template_configuration: List[main_models.ConfigModel] = None,
        template_id: int = None,
        template_version: int = None,
        type: str = None,
        use_scope: str = None,
        use_type: str = None,
    ):
        # This parameter is required.
        self.company_id = company_id
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.env = env
        self.id = id
        self.is_custom = is_custom
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.product_id = product_id
        self.request_id = request_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.scope = scope
        # This parameter is required.
        self.template_configuration = template_configuration
        # This parameter is required.
        self.template_id = template_id
        # This parameter is required.
        self.template_version = template_version
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.use_scope = use_scope
        # This parameter is required.
        self.use_type = use_type

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()
        if self.template_configuration:
            for v1 in self.template_configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        result['configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['configuration'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.id is not None:
            result['id'] = self.id

        if self.is_custom is not None:
            result['isCustom'] = self.is_custom

        if self.name is not None:
            result['name'] = self.name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.scope is not None:
            result['scope'] = self.scope

        result['templateConfiguration'] = []
        if self.template_configuration is not None:
            for k1 in self.template_configuration:
                result['templateConfiguration'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.template_version is not None:
            result['templateVersion'] = self.template_version

        if self.type is not None:
            result['type'] = self.type

        if self.use_scope is not None:
            result['useScope'] = self.use_scope

        if self.use_type is not None:
            result['useType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        self.configuration = []
        if m.get('configuration') is not None:
            for k1 in m.get('configuration'):
                temp_model = main_models.ConfigModel()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isCustom') is not None:
            self.is_custom = m.get('isCustom')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        self.template_configuration = []
        if m.get('templateConfiguration') is not None:
            for k1 in m.get('templateConfiguration'):
                temp_model = main_models.ConfigModel()
                self.template_configuration.append(temp_model.from_map(k1))

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('useScope') is not None:
            self.use_scope = m.get('useScope')

        if m.get('useType') is not None:
            self.use_type = m.get('useType')

        return self

