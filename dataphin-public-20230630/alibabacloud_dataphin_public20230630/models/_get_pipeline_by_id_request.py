# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPipelineByIdRequest(DaraModel):
    def __init__(
        self,
        context: main_models.GetPipelineByIdRequestContext = None,
        op_tenant_id: int = None,
        query_id: main_models.GetPipelineByIdRequestQueryId = None,
    ):
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        if self.context:
            self.context.validate()
        if self.query_id:
            self.query_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.query_id is not None:
            result['QueryId'] = self.query_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.GetPipelineByIdRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('QueryId') is not None:
            temp_model = main_models.GetPipelineByIdRequestQueryId()
            self.query_id = temp_model.from_map(m.get('QueryId'))

        return self

class GetPipelineByIdRequestQueryId(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        node_id: str = None,
        pipeline_id: int = None,
    ):
        self.file_id = file_id
        self.node_id = node_id
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

class GetPipelineByIdRequestContext(DaraModel):
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

