# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddMembersRequest(DaraModel):
    def __init__(
        self,
        member_arns: List[str] = None,
        workspace_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_arns = member_arns
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_arns is not None:
            result['memberArns'] = self.member_arns

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberArns') is not None:
            self.member_arns = m.get('memberArns')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

