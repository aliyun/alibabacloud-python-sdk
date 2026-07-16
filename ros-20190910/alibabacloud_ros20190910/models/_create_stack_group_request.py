# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateStackGroupRequest(DaraModel):
    def __init__(
        self,
        administration_role_name: str = None,
        auto_deployment: main_models.CreateStackGroupRequestAutoDeployment = None,
        capabilities: List[str] = None,
        client_token: str = None,
        description: str = None,
        execution_role_name: str = None,
        parameters: List[main_models.CreateStackGroupRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_arn: str = None,
        stack_group_name: str = None,
        tags: List[main_models.CreateStackGroupRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The name of the RAM role that you specify for the administrator account when you create a self-managed stack group. ROS assumes the administrator role to perform operations. If you do not specify this parameter, AliyunROSStackGroupAdministrationRole is used as the default value. ROS uses the administrator role to assume the execution role AliyunROSStackGroupExecutionRole to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.administration_role_name = administration_role_name
        # The information about automatic deployment settings.
        # 
        # > You must specify this parameter if PermissionModel is set to SERVICE_MANAGED.
        self.auto_deployment = auto_deployment
        # The options for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can contain letters, digits, underscores (_), and hyphens (-) and cannot exceed 64 characters in length.\\
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The description of the stack group.\\
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The name of the RAM role that you specify for the execution account when you create a self-managed stack group. The administrator role AliyunROSStackGroupAdministrationRole assumes the execution role to perform operations. If you do not specify this parameter, AliyunROSStackGroupExecutionRole is used as the default value. ROS assumes the execution role to perform operations on the stacks in the stack group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, and hyphens (-).
        self.execution_role_name = execution_role_name
        # The parameters of the stack group.
        self.parameters = parameters
        # The permission model of the stack group.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED (default): the self-managed permission model. If you create a self-managed stack group, you must create RAM roles within the administrator and execution accounts and establish a trust relationship between the accounts. Then, you can deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you create a service-managed stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # > If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Manage a delegated administrator account](https://help.aliyun.com/document_detail/308253.html) and [Enable trusted access](https://help.aliyun.com/document_detail/298229.html).
        self.permission_model = permission_model
        # The region ID of the stack group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you do not specify this parameter, the stack group is added to the default resource group.\\
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        self.stack_arn = stack_arn
        # The name of the stack group. The name must be unique within a region.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or a letter.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The tags of the stack group.
        self.tags = tags
        # The template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # > TemplateVersion takes effect only if you specify TemplateId.
        self.template_version = template_version

    def validate(self):
        if self.auto_deployment:
            self.auto_deployment.validate()
        if self.parameters:
            for v1 in self.parameters:
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
        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name

        if self.auto_deployment is not None:
            result['AutoDeployment'] = self.auto_deployment.to_map()

        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_arn is not None:
            result['StackArn'] = self.stack_arn

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')

        if m.get('AutoDeployment') is not None:
            temp_model = main_models.CreateStackGroupRequestAutoDeployment()
            self.auto_deployment = temp_model.from_map(m.get('AutoDeployment'))

        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateStackGroupRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackArn') is not None:
            self.stack_arn = m.get('StackArn')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateStackGroupRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

class CreateStackGroupRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the stack group.
        # 
        # > Tags is optional. If you want to specify Tags, you must also specify Tags.N.Key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the stack group.
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

class CreateStackGroupRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N. If you do not specify the key and value of a parameter, ROS uses the default name and value that are defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterKey.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # > Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterValue.
        # 
        # This parameter is required.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class CreateStackGroupRequestAutoDeployment(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        retain_stacks_on_account_removal: bool = None,
    ):
        # Indicates whether automatic deployment is enabled.
        # 
        # Valid values:
        # 
        # *   true: Automatic deployment is enabled. If you add a member account to the folder to which the stack group belongs after you enable automatic deployment, ROS automatically adds the stacks in the stack group to the member account. If you remove a member account from the folder, ROS automatically deletes the stacks from the member account.
        # *   false: Automatic deployment is disabled. After you disable automatic deployment, the stacks remain unchanged when you add member accounts to or remove member accounts from the folder.
        self.enabled = enabled
        # Indicates whether the stacks within a member account are retained when you remove the member account from the folder.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # > You must specify RetainStacksOnAccountRemoval if Enabled is set to true.
        self.retain_stacks_on_account_removal = retain_stacks_on_account_removal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.retain_stacks_on_account_removal is not None:
            result['RetainStacksOnAccountRemoval'] = self.retain_stacks_on_account_removal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('RetainStacksOnAccountRemoval') is not None:
            self.retain_stacks_on_account_removal = m.get('RetainStacksOnAccountRemoval')

        return self

