# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrafanaWorkspaceUserOrg(DaraModel):
    def __init__(
        self,
        org_id: int = None,
        org_name: str = None,
        role: str = None,
    ):
        self.org_id = org_id
        self.org_name = org_name
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.org_id is not None:
            result['orgId'] = self.org_id

        if self.org_name is not None:
            result['orgName'] = self.org_name

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orgId') is not None:
            self.org_id = m.get('orgId')

        if m.get('orgName') is not None:
            self.org_name = m.get('orgName')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

