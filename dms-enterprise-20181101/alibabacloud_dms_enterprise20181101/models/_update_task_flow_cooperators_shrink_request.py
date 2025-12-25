# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowCooperatorsShrinkRequest(DaraModel):
    def __init__(
        self,
        cooperator_ids_shrink: str = None,
        dag_id: int = None,
        tid: int = None,
    ):
        # The IDs of the users who are involved in the task flow to be updated.
        self.cooperator_ids_shrink = cooperator_ids_shrink
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the tenant.
        # 
        # > :To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cooperator_ids_shrink is not None:
            result['CooperatorIds'] = self.cooperator_ids_shrink

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CooperatorIds') is not None:
            self.cooperator_ids_shrink = m.get('CooperatorIds')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

