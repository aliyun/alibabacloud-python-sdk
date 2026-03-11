# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelProxiesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        proxy_mode: str = None,
        status: str = None,
        workspace_id: str = None,
        workspace_ids: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # proxyMode
        self.proxy_mode = proxy_mode
        self.status = status
        self.workspace_id = workspace_id
        self.workspace_ids = workspace_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.proxy_mode is not None:
            result['proxyMode'] = self.proxy_mode

        if self.status is not None:
            result['status'] = self.status

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_ids is not None:
            result['workspaceIds'] = self.workspace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('proxyMode') is not None:
            self.proxy_mode = m.get('proxyMode')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceIds') is not None:
            self.workspace_ids = m.get('workspaceIds')

        return self

