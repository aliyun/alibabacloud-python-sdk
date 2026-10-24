# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceConfigDto(DaraModel):
    def __init__(
        self,
        config_key: str = None,
        config_type: str = None,
        config_value: str = None,
        node_group_id: str = None,
    ):
        # The configuration item name.
        self.config_key = config_key
        # The configuration type.
        self.config_type = config_type
        # The configuration item value.
        self.config_value = config_value
        # The compute group ID, which is required only when the parameter is exclusive to the compute group. In other scenarios, leave it empty or set it to the cluster ID.
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_key is not None:
            result['configKey'] = self.config_key

        if self.config_type is not None:
            result['configType'] = self.config_type

        if self.config_value is not None:
            result['configValue'] = self.config_value

        if self.node_group_id is not None:
            result['nodeGroupId'] = self.node_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configKey') is not None:
            self.config_key = m.get('configKey')

        if m.get('configType') is not None:
            self.config_type = m.get('configType')

        if m.get('configValue') is not None:
            self.config_value = m.get('configValue')

        if m.get('nodeGroupId') is not None:
            self.node_group_id = m.get('nodeGroupId')

        return self

