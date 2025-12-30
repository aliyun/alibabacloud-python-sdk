# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPipelineAsyncResultRequest(DaraModel):
    def __init__(
        self,
        async_id: int = None,
        context: main_models.GetPipelineAsyncResultRequestContext = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.async_id = async_id
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_id is not None:
            result['AsyncId'] = self.async_id

        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncId') is not None:
            self.async_id = m.get('AsyncId')

        if m.get('Context') is not None:
            temp_model = main_models.GetPipelineAsyncResultRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetPipelineAsyncResultRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

