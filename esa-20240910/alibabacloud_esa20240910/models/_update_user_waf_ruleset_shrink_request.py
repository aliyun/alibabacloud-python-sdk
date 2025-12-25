# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserWafRulesetShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        id: int = None,
        instance_id: str = None,
        name: str = None,
        position: int = None,
        rules_shrink: str = None,
        shared_shrink: str = None,
        status: str = None,
    ):
        self.description = description
        self.expression = expression
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.position = position
        self.rules_shrink = rules_shrink
        self.shared_shrink = shared_shrink
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.position is not None:
            result['Position'] = self.position

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        if self.shared_shrink is not None:
            result['Shared'] = self.shared_shrink

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('Shared') is not None:
            self.shared_shrink = m.get('Shared')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

