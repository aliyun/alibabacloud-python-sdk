# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEngineConfigRequest(DaraModel):
    def __init__(
        self,
        config_value: str = None,
        description: str = None,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        # The content of the engine configuration.
        self.config_value = config_value
        # The description.
        self.description = description
        # The runtime environment. Valid values:
        # 
        # - Daily: daily environment.
        # 
        # - Pre: staging environment.
        # 
        # - Prod: production environment.
        self.environment = environment
        # The instance ID. You can obtain the ID from the [ListInstances](https://help.aliyun.com/document_detail/2411819.html) operation.
        self.instance_id = instance_id
        # The name of the engine configuration.
        self.name = name
        # The type of the engine configuration.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.description is not None:
            result['Description'] = self.description

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

