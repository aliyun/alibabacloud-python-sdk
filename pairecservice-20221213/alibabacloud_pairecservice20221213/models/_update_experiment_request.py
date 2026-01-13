# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExperimentRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        debug_crowd_id: str = None,
        debug_users: str = None,
        description: str = None,
        flow_percent: int = None,
        instance_id: str = None,
        name: str = None,
        type: str = None,
    ):
        self.config = config
        self.debug_crowd_id = debug_crowd_id
        self.debug_users = debug_users
        # This parameter is required.
        self.description = description
        self.flow_percent = flow_percent
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.debug_crowd_id is not None:
            result['DebugCrowdId'] = self.debug_crowd_id

        if self.debug_users is not None:
            result['DebugUsers'] = self.debug_users

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_percent is not None:
            result['FlowPercent'] = self.flow_percent

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DebugCrowdId') is not None:
            self.debug_crowd_id = m.get('DebugCrowdId')

        if m.get('DebugUsers') is not None:
            self.debug_users = m.get('DebugUsers')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowPercent') is not None:
            self.flow_percent = m.get('FlowPercent')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

