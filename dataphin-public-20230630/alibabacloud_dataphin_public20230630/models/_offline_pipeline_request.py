# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OfflinePipelineRequest(DaraModel):
    def __init__(
        self,
        context: main_models.OfflinePipelineRequestContext = None,
        offline_command: main_models.OfflinePipelineRequestOfflineCommand = None,
        op_tenant_id: int = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context = context
        # The offline command for the pipeline node.
        # 
        # This parameter is required.
        self.offline_command = offline_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.context:
            self.context.validate()
        if self.offline_command:
            self.offline_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.offline_command is not None:
            result['OfflineCommand'] = self.offline_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.OfflinePipelineRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OfflineCommand') is not None:
            temp_model = main_models.OfflinePipelineRequestOfflineCommand()
            self.offline_command = temp_model.from_map(m.get('OfflineCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class OfflinePipelineRequestOfflineCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        delete: bool = None,
        file_id: int = None,
        node_id: str = None,
        pipeline_id: int = None,
    ):
        # The remarks.
        self.comment = comment
        # Specifies whether to delete the node.
        # 
        # This parameter is required.
        self.delete = delete
        # The file ID of the integration node. You can specify any one of PipelineId, FileId, or NodeId.
        self.file_id = file_id
        # The scheduling node ID of the integration node. You can specify any one of PipelineId, FileId, or NodeId.
        self.node_id = node_id
        # The primary key of the integration pipeline. You can specify any one of PipelineId, FileId, or NodeId.
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

class OfflinePipelineRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The current operating environment. Valid values:
        # - DEV: the development environment.
        # - PROD: the production environment.
        # 
        # This parameter is required.
        self.env = env
        # The ID of the project to which the integration pipeline node belongs.
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

