# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGranularityBySummaryIdRequest(DaraModel):
    def __init__(
        self,
        env: str = None,
        model_id: int = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
        query_draft: bool = None,
    ):
        # Env
        self.env = env
        # ModelId
        # 
        # This parameter is required.
        self.model_id = model_id
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator ID.
        self.op_user_id = op_user_id
        # ProjectId
        # 
        # This parameter is required.
        self.project_id = project_id
        # QueryDraft
        self.query_draft = query_draft

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.query_draft is not None:
            result['QueryDraft'] = self.query_draft

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('QueryDraft') is not None:
            self.query_draft = m.get('QueryDraft')

        return self

