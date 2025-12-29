# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartExecutionShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        loop_mode: str = None,
        mode: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        safety_check: str = None,
        tags_shrink: str = None,
        template_content: str = None,
        template_name: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The access token.
        self.client_token = client_token
        # The description of the execution.
        self.description = description
        # The loop mode. Valid values:
        # 
        # *   Automatic: does not suspend the execution of the template. This is the default value.
        # *   FirstBatchPause: suspends the execution of the template after the first batch is complete.
        # *   EveryBatchPause: suspends the execution of the template after each batch is complete.
        self.loop_mode = loop_mode
        # The execution mode. Valid values:
        # 
        # *   Automatic: automatically starts the execution of the template. This is the default value.
        # *   FailurePause: suspends the execution of the template upon a failure.
        # *   Debug: manually starts the execution of the template.
        self.mode = mode
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The ID of the region in which the execution resides.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security check mode. Valid values:
        # 
        # *   Skip: specifies that you are aware of the risks. The system performs all actions in the execution without manual confirmation, regardless of the risk level. This parameter is valid only if the `Mode` parameter is set to Automatic.
        # *   ConfirmEveryHighRiskAction: requires you to confirm each high-risk action. This is the default value. You can call the **NotifyExecution** operation to confirm or cancel an action.
        self.safety_check = safety_check
        # The tags for the execution.
        self.tags_shrink = tags_shrink
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        self.template_name = template_name
        # The Object Storage Service (OSS) URL of the object that stores the content of the Operation Orchestration Service (OOS) template. The access control list (ACL) of the object must be public-read. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url
        # The version number of the template. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

