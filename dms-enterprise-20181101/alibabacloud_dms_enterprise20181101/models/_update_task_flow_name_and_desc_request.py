# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowNameAndDescRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_name: str = None,
        description: str = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The new name that you want to specify for the task flow.
        # 
        # This parameter is required.
        self.dag_name = dag_name
        # The description that you want to specify for the task flow.
        self.description = description
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

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.description is not None:
            result['Description'] = self.description

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

