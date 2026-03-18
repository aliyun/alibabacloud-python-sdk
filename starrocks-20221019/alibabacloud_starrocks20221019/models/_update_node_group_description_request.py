# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNodeGroupDescriptionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        node_group_id: str = None,
        x_acs_ram_auth_context: str = None,
    ):
        self.description = description
        self.node_group_id = node_group_id
        self.x_acs_ram_auth_context = x_acs_ram_auth_context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.x_acs_ram_auth_context is not None:
            result['X-Acs-Ram-Auth-Context'] = self.x_acs_ram_auth_context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('X-Acs-Ram-Auth-Context') is not None:
            self.x_acs_ram_auth_context = m.get('X-Acs-Ram-Auth-Context')

        return self

