# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowTimeVariablesRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        tid: int = None,
        time_variables: str = None,
    ):
        # The ID of the task node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the tenant.
        # 
        # > :To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The time variables for the task flow.
        # 
        # This parameter is required.
        self.time_variables = time_variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.time_variables is not None:
            result['TimeVariables'] = self.time_variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TimeVariables') is not None:
            self.time_variables = m.get('TimeVariables')

        return self

