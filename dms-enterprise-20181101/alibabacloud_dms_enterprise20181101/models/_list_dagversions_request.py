# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDAGVersionsRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        page_index: int = None,
        page_size: int = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the ID of the task flow.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_index = page_index
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

