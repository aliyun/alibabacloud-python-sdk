# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateStreamBatchJobMappingRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        stream_batch_job_mapping_create_command: main_models.CreateStreamBatchJobMappingRequestStreamBatchJobMappingCreateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.stream_batch_job_mapping_create_command = stream_batch_job_mapping_create_command

    def validate(self):
        if self.stream_batch_job_mapping_create_command:
            self.stream_batch_job_mapping_create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.stream_batch_job_mapping_create_command is not None:
            result['StreamBatchJobMappingCreateCommand'] = self.stream_batch_job_mapping_create_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('StreamBatchJobMappingCreateCommand') is not None:
            temp_model = main_models.CreateStreamBatchJobMappingRequestStreamBatchJobMappingCreateCommand()
            self.stream_batch_job_mapping_create_command = temp_model.from_map(m.get('StreamBatchJobMappingCreateCommand'))

        return self

class CreateStreamBatchJobMappingRequestStreamBatchJobMappingCreateCommand(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        description: str = None,
        directory: str = None,
        engine_version: str = None,
        env: str = None,
        file_name: str = None,
        file_type: str = None,
        project_id: int = None,
        queue_name: str = None,
        vvp_cluster_type: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        self.description = description
        # This parameter is required.
        self.directory = directory
        # This parameter is required.
        self.engine_version = engine_version
        # This parameter is required.
        self.env = env
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vvp_cluster_type = vvp_cluster_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.env is not None:
            result['Env'] = self.env

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.vvp_cluster_type is not None:
            result['VvpClusterType'] = self.vvp_cluster_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('VvpClusterType') is not None:
            self.vvp_cluster_type = m.get('VvpClusterType')

        return self

