# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateRequest(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        include_permission: str = None,
        include_tags: str = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        template_id: str = None,
        template_stage: str = None,
        template_version: str = None,
    ):
        # The ID of the change set.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.change_set_id = change_set_id
        # Specifies whether to query the shared information about the template. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > Only the template owner can query the shared information of a template.
        self.include_permission = include_permission
        # Specifies whether to query the information about tags. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > This parameter takes effect only if you specify TemplateId.
        self.include_tags = include_tags
        # The region ID of the stack or stack group that uses the template. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        self.region_id = region_id
        # The name of the stack group.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.stack_group_name = stack_group_name
        # The ID of the stack.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.stack_id = stack_id
        # The ID of the template.
        # 
        # This parameter applies to shared and private templates. If the template is a shared template, the value of TemplateId is the same as the value of TemplateARN. You can use the template ID to query a shared template.
        # 
        # > You must specify one of the following parameters: StackId, ChangeSetId, StackGroupName, and TemplateId.
        self.template_id = template_id
        # The stage of the template. This parameter takes effect only if you specify StackId, ChangeSetId, or StackGroupName.
        # 
        # Valid values:
        # 
        # *   Processed (default): returns the processed template.
        # *   Original: returns the original template.
        self.template_stage = template_stage
        # The version of the template. This parameter takes effect only if you specify TemplateId.\\
        # If the template is a shared template, you can specify this parameter only if VersionOption is set to AllVersions. For more information, see [SetTemplatePermission](https://help.aliyun.com/document_detail/194768.html).
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.include_permission is not None:
            result['IncludePermission'] = self.include_permission

        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_stage is not None:
            result['TemplateStage'] = self.template_stage

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('IncludePermission') is not None:
            self.include_permission = m.get('IncludePermission')

        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateStage') is not None:
            self.template_stage = m.get('TemplateStage')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

