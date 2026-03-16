# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFlowAliasShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        flow_name: str = None,
        name: str = None,
        routing_configurations_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.routing_configurations_shrink = routing_configurations_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.name is not None:
            result['Name'] = self.name

        if self.routing_configurations_shrink is not None:
            result['RoutingConfigurations'] = self.routing_configurations_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RoutingConfigurations') is not None:
            self.routing_configurations_shrink = m.get('RoutingConfigurations')

        return self

