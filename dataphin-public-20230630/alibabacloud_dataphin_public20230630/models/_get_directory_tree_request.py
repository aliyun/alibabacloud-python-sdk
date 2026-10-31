# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDirectoryTreeRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
    ):
        # The directory type. Valid values:
        # - tempCode: Ad hoc query.
        # - codeManage: Code task.
        # - offlinePipeline: Offline pipeline.
        # - offlinePipelineCustomPlugin: Custom pipeline component.
        # - dataX: Synchronization task.
        # - streamMeta: Real-time metadata table.
        # - streamCustomDataSource: Real-time custom source.
        # - streamTemplate: Real-time computing template.
        # - resourceManage: Resource management.
        # - udfResource: Offline function.
        # - streamFunction: Real-time function.
        # 
        # This parameter is required.
        self.category = category
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operating user.
        self.op_user_id = op_user_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

