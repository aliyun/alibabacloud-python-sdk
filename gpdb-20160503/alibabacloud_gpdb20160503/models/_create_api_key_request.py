# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateApiKeyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        key_name: str = None,
        region_id: str = None,
        service_ids: List[str] = None,
        workspace_id: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.key_name = key_name
        self.region_id = region_id
        self.service_ids = service_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

