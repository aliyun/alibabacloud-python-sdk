# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_shrink: str = None,
        name: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # The definition of the workflow. The definition must comply with the flow definition language (FDL) syntax. Considering compatibility, the system supports the two workflow definition specifications.
        # 
        # >  In the preceding workflow definition example, Name:my_flow_name is the workflow name, which must be consistent with the input parameter Name
        self.definition = definition
        # The description of the flow.
        self.description = description
        self.environment_shrink = environment_shrink
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The Alibaba Cloud resource name (ARN) of the authorized role on which the execution of the flow relies. During the execution of the flow, the flow execution engine assumes the role to call API operations of relevant services.
        self.role_arn = role_arn
        # The type of the flow. Valid value: **FDL**.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['Definition'] = self.definition

        if self.description is not None:
            result['Description'] = self.description

        if self.environment_shrink is not None:
            result['Environment'] = self.environment_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Environment') is not None:
            self.environment_shrink = m.get('Environment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

