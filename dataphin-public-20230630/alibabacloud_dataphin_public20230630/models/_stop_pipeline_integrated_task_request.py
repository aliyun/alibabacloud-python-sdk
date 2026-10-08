# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class StopPipelineIntegratedTaskRequest(DaraModel):
    def __init__(
        self,
        context: main_models.StopPipelineIntegratedTaskRequestContext = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        stop_command: main_models.StopPipelineIntegratedTaskRequestStopCommand = None,
    ):
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # This parameter is required.
        self.stop_command = stop_command

    def validate(self):
        if self.context:
            self.context.validate()
        if self.stop_command:
            self.stop_command.validate()

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

        if self.stop_command is not None:
            result['StopCommand'] = self.stop_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.StopPipelineIntegratedTaskRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('StopCommand') is not None:
            temp_model = main_models.StopPipelineIntegratedTaskRequestStopCommand()
            self.stop_command = temp_model.from_map(m.get('StopCommand'))

        return self

class StopPipelineIntegratedTaskRequestStopCommand(DaraModel):
    def __init__(
        self,
        task_ids: List[str] = None,
    ):
        # This parameter is required.
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')

        return self

class StopPipelineIntegratedTaskRequestContext(DaraModel):
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

