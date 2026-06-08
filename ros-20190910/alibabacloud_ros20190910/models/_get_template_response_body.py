# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateResponseBody(DaraModel):
    def __init__(
        self,
        additional_info: Dict[str, Any] = None,
        change_set_id: str = None,
        create_time: str = None,
        description: str = None,
        interface: str = None,
        owner_id: str = None,
        permissions: List[main_models.GetTemplateResponseBodyPermissions] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        tags: List[main_models.GetTemplateResponseBodyTags] = None,
        template_arn: str = None,
        template_body: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        # Supplementary information for the public template.
        self.additional_info = additional_info
        # The ID of the change set. This parameter is returned only if you specify ChangeSetId.
        self.change_set_id = change_set_id
        # The time when the template was created. This parameter is returned only if you specify TemplateId.
        # 
        # > - If you specify TemplateVersion, the creation time of the template whose version is specified by TemplateVersion is returned.
        # > - If you do not specify TemplateVersion, the creation time of the template whose version is the default version is returned.
        self.create_time = create_time
        # The description of the template. This parameter is returned only if you specify TemplateId.
        self.description = description
        # The description of the web UI in the ROS console.
        self.interface = interface
        # The ID of the Alibaba Cloud account to which the template belongs. This parameter is returned only if you specify TemplateId.
        self.owner_id = owner_id
        # Details of the sharing status of the template. This parameter is returned only if you specify TemplateId and set IncludePermission to Enabled.
        # 
        # > - If TemplateVersion is not specified or does not take effect, the details of the sharing status of the template whose version is the default version is returned.
        # > - If TemplateVersion is specified and takes effect, the details of the sharing status of the template whose version is specified by TemplateVersion is returned.
        self.permissions = permissions
        # The region ID of the stack or stack group that uses the template. This parameter is returned only if you specify StackId, ChangeSetId, or StackGroupName.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The sharing type of the template. This parameter is returned only if you specify TemplateId.
        # 
        # Valid values:
        # 
        # *   Private: The template belongs to the template owner.
        # *   Shared: The template is shared by other users.
        self.share_type = share_type
        # The name of the stack group. This parameter is returned only if you specify StackGroupName.
        self.stack_group_name = stack_group_name
        # The ID of the stack. This parameter is returned only if you specify StackId.
        self.stack_id = stack_id
        # The tags of the template.
        self.tags = tags
        # The Alibaba Cloud Resource Name (ARN) of the template. This parameter is returned only if you specify TemplateId.
        self.template_arn = template_arn
        # The content of the template.
        self.template_body = template_body
        # The ID of the template. This parameter is returned only if you specify TemplateId.
        # 
        # If the template is a shared template, the value of this parameter is the same as the value of TemplateARN.
        self.template_id = template_id
        # The name of the template. This parameter is returned only if you specify TemplateId.
        # 
        # > -   If you specify TemplateVersion, the name of the template whose version is specified by TemplateVersion is returned.
        # > -  If you not specify TemplateVersion, the name of the template whose version is the default version is returned.
        self.template_name = template_name
        # The version of the template. This parameter is returned only if you specify TemplateId.\\
        # If TemplateVersion is not specified or does not take effect, the default version is used.
        # 
        # If the template is a shared template, this parameter is returned only if you set VersionOption to AllVersions.
        self.template_version = template_version
        # The time when the template was last updated. This parameter is returned only if you specify TemplateId.
        # 
        # > - If you specify TemplateVersion, the last update time of the template whose version is specified by TemplateVersion is returned.
        # > - If you do not specify TemplateVersion, the last update time of the template whose version is the default version is returned.
        self.update_time = update_time

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_info is not None:
            result['AdditionalInfo'] = self.additional_info

        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.interface is not None:
            result['Interface'] = self.interface

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_type is not None:
            result['ShareType'] = self.share_type

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_arn is not None:
            result['TemplateARN'] = self.template_arn

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalInfo') is not None:
            self.additional_info = m.get('AdditionalInfo')

        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Interface') is not None:
            self.interface = m.get('Interface')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.GetTemplateResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTemplateResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateARN') is not None:
            self.template_arn = m.get('TemplateARN')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetTemplateResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the template.
        self.key = key
        # The tag value of the template.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetTemplateResponseBodyPermissions(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        share_option: str = None,
        share_source: str = None,
        template_version: str = None,
        version_option: str = None,
    ):
        # The ID of the Alibaba Cloud account with which the template is shared.
        self.account_id = account_id
        # The sharing option.
        # 
        # The value ShareToAccounts indicates that the template is shared with one or more Alibaba Cloud accounts.
        self.share_option = share_option
        # The service that is used for resource sharing. Valid values:
        # 
        # - ROS: Resources are shared from ROS by using the ROS console or calling the ROS API.
        # - ResourceDirectory: Resources are shared with accounts in a resource directory from Resource Management by using the resource sharing feature.
        # > -  The number of accounts with which resources are shared from ROS is independent of the number of accounts with which resources are shared from the resource directory.
        # > -  The shared resources from ROS cannot override or overwrite the shared resources from the resource directory.
        # > -  The shared resources from the resource directory can overwrite the shared resources from ROS.
        self.share_source = share_source
        # The version of the shared template. This parameter is returned only if you set ShareOption to ShareToAccounts and set VersionOption to Specified or Current.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The version option for the shared template. This parameter is returned only if you set ShareOption to ShareToAccounts.
        # 
        # Valid values:
        # 
        # *   AllVersions: All template versions are shared.
        # *   Latest: Only the latest template version is shared. When the version of the template is updated, Resource Orchestration Service (ROS) updates the shared version to the latest version.
        # *   Current: Only the latest template version is shared. When the version of the template is updated, ROS does not update the shared version.
        # *   Specified: Only the specified template version is shared.
        self.version_option = version_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.share_option is not None:
            result['ShareOption'] = self.share_option

        if self.share_source is not None:
            result['ShareSource'] = self.share_source

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.version_option is not None:
            result['VersionOption'] = self.version_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')

        if m.get('ShareSource') is not None:
            self.share_source = m.get('ShareSource')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')

        return self

