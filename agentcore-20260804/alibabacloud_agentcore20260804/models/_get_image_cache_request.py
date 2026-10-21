# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageCacheRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The product entry region, which is determined by the selected region endpoint.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The current routed workspace. The server verifies the account, region, and resource ownership. This parameter cannot be omitted or used to access other workspaces.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

