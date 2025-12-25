# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEnvironmentRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        description: str = None,
        gateway_id: str = None,
        name: str = None,
        resource_group_id: str = None,
    ):
        # Environment alias.
        # 
        # This parameter is required.
        self.alias = alias
        # Description of the environment, which can include information such as the purpose of the environment and its owner.
        self.description = description
        # Gateway ID.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # Environment name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.description is not None:
            result['description'] = self.description

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

