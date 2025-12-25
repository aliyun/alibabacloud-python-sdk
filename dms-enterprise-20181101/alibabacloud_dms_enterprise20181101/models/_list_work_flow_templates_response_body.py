# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListWorkFlowTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        work_flow_templates: main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplates = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The approval templates.
        self.work_flow_templates = work_flow_templates

    def validate(self):
        if self.work_flow_templates:
            self.work_flow_templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.work_flow_templates is not None:
            result['WorkFlowTemplates'] = self.work_flow_templates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('WorkFlowTemplates') is not None:
            temp_model = main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplates()
            self.work_flow_templates = temp_model.from_map(m.get('WorkFlowTemplates'))

        return self

class ListWorkFlowTemplatesResponseBodyWorkFlowTemplates(DaraModel):
    def __init__(
        self,
        work_flow_template: List[main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate] = None,
    ):
        self.work_flow_template = work_flow_template

    def validate(self):
        if self.work_flow_template:
            for v1 in self.work_flow_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WorkFlowTemplate'] = []
        if self.work_flow_template is not None:
            for k1 in self.work_flow_template:
                result['WorkFlowTemplate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.work_flow_template = []
        if m.get('WorkFlowTemplate') is not None:
            for k1 in m.get('WorkFlowTemplate'):
                temp_model = main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate()
                self.work_flow_template.append(temp_model.from_map(k1))

        return self

class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplate(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_user_id: int = None,
        enabled: str = None,
        is_system: int = None,
        template_id: int = None,
        template_name: str = None,
        workflow_nodes: main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes = None,
    ):
        # The description of the approval template.
        self.comment = comment
        # The ID of the creator.
        self.create_user_id = create_user_id
        # Indicates whether the approval template is enabled. Valid values:
        # 
        # *   Y: The approval template is enabled.
        # *   N: The approval template is disabled.
        self.enabled = enabled
        # Indicates whether the approval template is predefined by the system. Valid values:
        # 
        # *   1: The approval template is predefined by the system.
        # *   0: The approval template is not predefined by the system.
        self.is_system = is_system
        # The ID of the approval template.
        self.template_id = template_id
        # The name of the approval template.
        self.template_name = template_name
        # The details of approval nodes.
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.is_system is not None:
            result['IsSystem'] = self.is_system

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('IsSystem') is not None:
            self.is_system = m.get('IsSystem')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('WorkflowNodes') is not None:
            temp_model = main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m.get('WorkflowNodes'))

        return self

class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodes(DaraModel):
    def __init__(
        self,
        workflow_node: List[main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode] = None,
    ):
        self.workflow_node = workflow_node

    def validate(self):
        if self.workflow_node:
            for v1 in self.workflow_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WorkflowNode'] = []
        if self.workflow_node is not None:
            for k1 in self.workflow_node:
                result['WorkflowNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workflow_node = []
        if m.get('WorkflowNode') is not None:
            for k1 in m.get('WorkflowNode'):
                temp_model = main_models.ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k1))

        return self

class ListWorkFlowTemplatesResponseBodyWorkFlowTemplatesWorkFlowTemplateWorkflowNodesWorkflowNode(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_user_id: int = None,
        node_id: int = None,
        node_name: str = None,
        node_type: str = None,
        position: int = None,
        template_id: int = None,
    ):
        # The description of the approval node.
        self.comment = comment
        # The ID of the creator.
        self.create_user_id = create_user_id
        # The ID of the approval node.
        self.node_id = node_id
        # The name of the approval node.
        self.node_name = node_name
        # The type of the approval node. Valid values:
        # 
        # *   SYS: The approval node is predefined by the system.
        # *   USER_LIST: The approval node is created by a user.
        self.node_type = node_type
        # The position of the approval node.
        self.position = position
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.position is not None:
            result['Position'] = self.position

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

