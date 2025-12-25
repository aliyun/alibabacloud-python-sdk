# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDifyAttributeRequest(DaraModel):
    def __init__(
        self,
        app_uuid: str = None,
        client_token: str = None,
        data_region: str = None,
        workspace_id: str = None,
    ):
        self.app_uuid = app_uuid
        self.client_token = client_token
        self.data_region = data_region
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uuid is not None:
            result['AppUuid'] = self.app_uuid

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUuid') is not None:
            self.app_uuid = m.get('AppUuid')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

