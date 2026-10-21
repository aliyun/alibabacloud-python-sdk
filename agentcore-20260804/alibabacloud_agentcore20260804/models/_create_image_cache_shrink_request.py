# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageCacheShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        client_token: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The business parameters for creating an image cache.
        # 
        # This parameter is required.
        self.body_shrink = body_shrink
        # This parameter is required and cannot be empty. It is reserved to be compatible with the API. Currently, it does not provide the ability to deduplicate requests or recover the original result based on this field. If a timeout occurs or the result is unconfirmed, query the query cache status first before deciding whether to recommit.
        # 
        # This parameter is required.
        self.client_token = client_token
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
        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

