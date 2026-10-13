# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListContextDatabaseSyncConnectionsRequest(DaraModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        plugin_id: str = None,
        workspace_id: str = None,
    ):
        # The page number. Pages start from 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The plug-in ID.
        self.plugin_id = plugin_id
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
        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

