# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class StartPipelineIntegratedTaskRequest(DaraModel):
    def __init__(
        self,
        context: main_models.StartPipelineIntegratedTaskRequestContext = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        start_command: main_models.StartPipelineIntegratedTaskRequestStartCommand = None,
    ):
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # This parameter is required.
        self.start_command = start_command

    def validate(self):
        if self.context:
            self.context.validate()
        if self.start_command:
            self.start_command.validate()

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

        if self.start_command is not None:
            result['StartCommand'] = self.start_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.StartPipelineIntegratedTaskRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('StartCommand') is not None:
            temp_model = main_models.StartPipelineIntegratedTaskRequestStartCommand()
            self.start_command = temp_model.from_map(m.get('StartCommand'))

        return self

class StartPipelineIntegratedTaskRequestStartCommand(DaraModel):
    def __init__(
        self,
        byte_speed: int = None,
        checkpoint: str = None,
        concurrent: int = None,
        full_task_mode: str = None,
        incremental_task_id: str = None,
        memory: int = None,
        node_id: str = None,
        quota_group_id: str = None,
        sync_mode: str = None,
    ):
        self.byte_speed = byte_speed
        self.checkpoint = checkpoint
        self.concurrent = concurrent
        self.full_task_mode = full_task_mode
        self.incremental_task_id = incremental_task_id
        self.memory = memory
        self.node_id = node_id
        self.quota_group_id = quota_group_id
        self.sync_mode = sync_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.byte_speed is not None:
            result['ByteSpeed'] = self.byte_speed

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.concurrent is not None:
            result['Concurrent'] = self.concurrent

        if self.full_task_mode is not None:
            result['FullTaskMode'] = self.full_task_mode

        if self.incremental_task_id is not None:
            result['IncrementalTaskId'] = self.incremental_task_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.quota_group_id is not None:
            result['QuotaGroupId'] = self.quota_group_id

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByteSpeed') is not None:
            self.byte_speed = m.get('ByteSpeed')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('Concurrent') is not None:
            self.concurrent = m.get('Concurrent')

        if m.get('FullTaskMode') is not None:
            self.full_task_mode = m.get('FullTaskMode')

        if m.get('IncrementalTaskId') is not None:
            self.incremental_task_id = m.get('IncrementalTaskId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('QuotaGroupId') is not None:
            self.quota_group_id = m.get('QuotaGroupId')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        return self

class StartPipelineIntegratedTaskRequestContext(DaraModel):
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

