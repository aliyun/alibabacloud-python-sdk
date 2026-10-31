# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitPipelineAsyncRequest(DaraModel):
    def __init__(
        self,
        context: main_models.SubmitPipelineAsyncRequestContext = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        query_id: main_models.SubmitPipelineAsyncRequestQueryId = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context = context
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator user ID.
        self.op_user_id = op_user_id
        # The ID used to query the pipeline task.
        # 
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

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.query_id is not None:
            result['QueryId'] = self.query_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.SubmitPipelineAsyncRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('QueryId') is not None:
            temp_model = main_models.SubmitPipelineAsyncRequestQueryId()
            self.query_id = temp_model.from_map(m.get('QueryId'))

        return self

class SubmitPipelineAsyncRequestQueryId(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        node_id: str = None,
        pipeline_id: int = None,
    ):
        # The ID of the integration task file. You can specify any one of pipelineId, fileId, or nodeId.
        self.file_id = file_id
        # The ID of the scheduling node for the integration task. You can specify any one of pipelineId, fileId, or nodeId.
        self.node_id = node_id
        # The primary key of the integration pipeline. You can specify any one of pipelineId, fileId, or nodeId.
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

class SubmitPipelineAsyncRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The current operation environment. Valid values: DEV: development environment. PROD: production environment.
        # 
        # This parameter is required.
        self.env = env
        # The ID of the project to which the integration pipeline task belongs.
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

