# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolicyContentShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        id: str = None,
        name: str = None,
        port_version: str = None,
    ):
        # The policy content.
        self.content_shrink = content_shrink
        # The ID of the policy.
        # 
        # This parameter is required.
        self.id = id
        # The name of the policy.
        self.name = name
        self.port_version = port_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self

