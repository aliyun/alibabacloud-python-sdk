# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workflow_definition: main_models.GetWorkflowDefinitionResponseBodyWorkflowDefinition = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the workflow.
        self.workflow_definition = workflow_definition

    def validate(self):
        if self.workflow_definition:
            self.workflow_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workflow_definition is not None:
            result['WorkflowDefinition'] = self.workflow_definition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkflowDefinition') is not None:
            temp_model = main_models.GetWorkflowDefinitionResponseBodyWorkflowDefinition()
            self.workflow_definition = temp_model.from_map(m.get('WorkflowDefinition'))

        return self

class GetWorkflowDefinitionResponseBodyWorkflowDefinition(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        spec: str = None,
        workflow_id: int = None,
    ):
        # The time when the workflow was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the workflow.
        self.id = id
        # The time when the workflow was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the workflow.
        self.name = name
        # The owner of the workflow.
        self.owner = owner
        # The ID of the workspace to which the workflow belongs.
        self.project_id = project_id
        # The FlowSpec field information about the workflow. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow/).
        self.spec = spec
        # The ID of the workflow on the scheduling side after publishing.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

