# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateWorkFlowByJsonRequest(DaraModel):
    def __init__(
        self,
        context: main_models.CreateWorkFlowByJsonRequestContext = None,
        create_command: main_models.CreateWorkFlowByJsonRequestCreateCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context = context
        # The JSON script command for creating a workflow.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.context:
            self.context.validate()
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.CreateWorkFlowByJsonRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateWorkFlowByJsonRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateWorkFlowByJsonRequestCreateCommand(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory: str = None,
        schedule_config: str = None,
        submit: bool = None,
        task_name: str = None,
        task_type: int = None,
        work_flow_json: str = None,
    ):
        # The node description.
        self.description = description
        # The folder to which the node belongs. If this parameter is left empty, the root folder is used.
        self.directory = directory
        # The schedule configuration (required for periodic nodes). The value is a JSON string. Refer to the utility class: com.alibaba.dataphin.pipeline.common.facade.openapi.model.OAScheduleConfig#toJsonString method.
        self.schedule_config = schedule_config
        # Specifies whether to submit the node. Default value: true.
        self.submit = submit
        # The node name.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The node scheduling type. Valid values:
        # 
        # - 1: periodic scheduling.
        # - 3: manual scheduling.
        # - 5: real-time node.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The workflow JSON.
        # 
        # This parameter is required.
        self.work_flow_json = work_flow_json

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

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config

        if self.submit is not None:
            result['Submit'] = self.submit

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.work_flow_json is not None:
            result['WorkFlowJson'] = self.work_flow_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config = m.get('ScheduleConfig')

        if m.get('Submit') is not None:
            self.submit = m.get('Submit')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('WorkFlowJson') is not None:
            self.work_flow_json = m.get('WorkFlowJson')

        return self

class CreateWorkFlowByJsonRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The current operating environment. Valid values:
        # 
        # - DEV: the development environment.
        # - PROD: the production environment.
        # 
        # The current version supports only BASIC mode, so set this parameter to PROD.
        # 
        # This parameter is required.
        self.env = env
        # The ID of the project to which the workflow node belongs.
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

