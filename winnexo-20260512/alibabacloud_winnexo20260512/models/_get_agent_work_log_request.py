# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentWorkLogRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
        work_item_id: str = None,
    ):
        # The optional node key.
        self.node_id = node_id
        # The page number. Pages start from 1.
        self.page = page
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The tenant ID. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The work item ID.
        # 
        # This parameter is required.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

