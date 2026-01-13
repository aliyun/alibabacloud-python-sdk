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
    ):
        self.config_value = config_value
        self.description = description
        self.environment = environment
        self.instance_id = instance_id
        self.name = name

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

        return self

