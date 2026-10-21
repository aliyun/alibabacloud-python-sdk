# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryImageCacheShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        client_token: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The request body is a fixed empty object {}. WorkspaceId is passed as a query parameter. Do not pass the Pool, role, Digest, or network parameters.
        self.body_shrink = body_shrink
        # This parameter is required and cannot be empty. It is reserved to keep the API compatible. This field does not currently deduplicate requests or recover the original result. If a timeout occurs or the result is not confirmed, query the query cache status first before deciding whether to commit again.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The product entry region, which is determined by the selected region endpoint.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The current routed workspace. The server verifies the account, region, and resource ownership. You cannot omit this parameter or use it to access other workspaces.
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

