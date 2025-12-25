# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReDeployLhDagVersionRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_version: int = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the ID of the task flow.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the task flow version. You can call the [ListDAGVersions](https://help.aliyun.com/document_detail/424682.html) operation to obtain the ID of the task flow version.
        self.dag_version = dag_version
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the ID of the tenant.
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

        if self.dag_version is not None:
            result['DagVersion'] = self.dag_version

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagVersion') is not None:
            self.dag_version = m.get('DagVersion')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

