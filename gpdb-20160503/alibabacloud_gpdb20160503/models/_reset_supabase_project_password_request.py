# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetSupabaseProjectPasswordRequest(DaraModel):
    def __init__(
        self,
        account_password: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.account_password = account_password
        # This parameter is required.
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

