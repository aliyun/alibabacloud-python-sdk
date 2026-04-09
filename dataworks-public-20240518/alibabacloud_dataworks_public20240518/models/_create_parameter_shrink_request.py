# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateParameterShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        properties_shrink: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.owner = owner
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.properties_shrink = properties_shrink
        self.scope = scope
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

