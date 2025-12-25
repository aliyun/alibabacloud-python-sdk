# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEntityStoreResponseBody(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        workspace_name: str = None,
    ):
        # Region ID
        self.region_id = region_id
        # Request ID
        self.request_id = request_id
        # Workspace name
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        return self

