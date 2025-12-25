# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowConstantsShrinkRequest(DaraModel):
    def __init__(
        self,
        dag_constants_shrink: str = None,
        dag_id: int = None,
        tid: int = None,
    ):
        # The constants for the task flow.
        self.dag_constants_shrink = dag_constants_shrink
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_constants_shrink is not None:
            result['DagConstants'] = self.dag_constants_shrink

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagConstants') is not None:
            self.dag_constants_shrink = m.get('DagConstants')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

