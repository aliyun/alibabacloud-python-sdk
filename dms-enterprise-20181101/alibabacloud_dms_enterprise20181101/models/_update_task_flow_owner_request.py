# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowOwnerRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        new_owner_id: str = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlowInstance](https://help.aliyun.com/document_detail/424689.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The user ID of the new owner. You can call the [GetUser](https://help.aliyun.com/document_detail/147098.html) or [ListUsers](https://help.aliyun.com/document_detail/141938.html) operation to query the user ID.
        # 
        # This parameter is required.
        self.new_owner_id = new_owner_id
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
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

        if self.new_owner_id is not None:
            result['NewOwnerId'] = self.new_owner_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('NewOwnerId') is not None:
            self.new_owner_id = m.get('NewOwnerId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

