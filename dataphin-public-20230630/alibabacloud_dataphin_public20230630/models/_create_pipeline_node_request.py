# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreatePipelineNodeRequest(DaraModel):
    def __init__(
        self,
        create_pipeline_node_command: main_models.CreatePipelineNodeRequestCreatePipelineNodeCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_pipeline_node_command = create_pipeline_node_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_pipeline_node_command:
            self.create_pipeline_node_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_pipeline_node_command is not None:
            result['CreatePipelineNodeCommand'] = self.create_pipeline_node_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatePipelineNodeCommand') is not None:
            temp_model = main_models.CreatePipelineNodeRequestCreatePipelineNodeCommand()
            self.create_pipeline_node_command = temp_model.from_map(m.get('CreatePipelineNodeCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreatePipelineNodeRequestCreatePipelineNodeCommand(DaraModel):
    def __init__(
        self,
        file_info: main_models.CreatePipelineNodeRequestCreatePipelineNodeCommandFileInfo = None,
        node_type: str = None,
        pipeline_name: str = None,
        pipeline_type: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.file_info = file_info
        # This parameter is required.
        self.node_type = node_type
        # This parameter is required.
        self.pipeline_name = pipeline_name
        # This parameter is required.
        self.pipeline_type = pipeline_type
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_info is not None:
            result['FileInfo'] = self.file_info.to_map()

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name

        if self.pipeline_type is not None:
            result['PipelineType'] = self.pipeline_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileInfo') is not None:
            temp_model = main_models.CreatePipelineNodeRequestCreatePipelineNodeCommandFileInfo()
            self.file_info = temp_model.from_map(m.get('FileInfo'))

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')

        if m.get('PipelineType') is not None:
            self.pipeline_type = m.get('PipelineType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreatePipelineNodeRequestCreatePipelineNodeCommandFileInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory: str = None,
        file_name: str = None,
    ):
        self.description = description
        self.directory = directory
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

