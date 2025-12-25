# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeLhDagOwnerRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        owner_user_id: int = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the user to be specified as the new owner of the task flow. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetUser](https://help.aliyun.com/document_detail/147098.html) operation to obtain the user ID.
        # 
        # This parameter is required.
        self.owner_user_id = owner_user_id
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

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

