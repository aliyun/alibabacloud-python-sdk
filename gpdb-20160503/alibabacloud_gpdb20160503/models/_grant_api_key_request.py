# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GrantApiKeyRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        region_id: str = None,
        service_ids: List[str] = None,
        workspace_id: str = None,
    ):
        # The ID of the API key.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The region ID.
        self.region_id = region_id
        # The list of service IDs to authorize.
        # 
        # This parameter is required.
        self.service_ids = service_ids
        # The workspace ID.
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
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

