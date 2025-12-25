# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataLakeCatalogRequest(DaraModel):
    def __init__(
        self,
        data_region: str = None,
        search_key: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # The region where the data lake resides.
        # 
        # This parameter is required.
        self.data_region = data_region
        # The keyword that is used to search for catalogs.
        self.search_key = search_key
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the ID of the tenant.
        self.tid = tid
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

