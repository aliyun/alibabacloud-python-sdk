# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OfflinePipelineByAsyncRequest(DaraModel):
    def __init__(
        self,
        context: main_models.OfflinePipelineByAsyncRequestContext = None,
        offline_command: main_models.OfflinePipelineByAsyncRequestOfflineCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.offline_command = offline_command
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
            temp_model = main_models.OfflinePipelineByAsyncRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OfflineCommand') is not None:
            temp_model = main_models.OfflinePipelineByAsyncRequestOfflineCommand()
            self.offline_command = temp_model.from_map(m.get('OfflineCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class OfflinePipelineByAsyncRequestOfflineCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        delete: bool = None,
        file_id: int = None,
        node_id: str = None,
        pipeline_id: int = None,
    ):
        self.comment = comment
        # This parameter is required.
        self.delete = delete
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

class OfflinePipelineByAsyncRequestContext(DaraModel):
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

