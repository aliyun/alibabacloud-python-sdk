# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEditableNamespaceRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        page_index: str = None,
        page_size: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

