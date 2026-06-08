# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class UpdateStackGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        administration_role_name: str = None,
        auto_deployment_shrink: str = None,
        capabilities: List[str] = None,
        client_token: str = None,
        deployment_options: List[str] = None,
        deployment_targets_shrink: str = None,
        description: str = None,
        execution_role_name: str = None,
        operation_description: str = None,
        operation_preferences_shrink: str = None,
        parameters: List[main_models.UpdateStackGroupShrinkRequestParameters] = None,
        permission_model: str = None,
        region_id: str = None,
        region_ids_shrink: str = None,
        stack_group_name: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Alibaba Cloud Object Storage Service (OSS) bucket. The template body must be 1 to 524,288 bytes in length. Examples: oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.account_ids_shrink = account_ids_shrink
        # The key of parameter N. If you do not specify the key and value of the parameter, ROS uses the default key and value in the template.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterKey parameter.
        self.administration_role_name = administration_role_name
        # The IDs of the folders in the resource directory. You can specify up to five folder IDs.
        # 
        # You can create stacks within all members in the specified folders. If you create stacks in the Root folder, the stacks are created within all members in the resource directory.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](https://help.aliyun.com/document_detail/111223.html).
        self.auto_deployment_shrink = auto_deployment_shrink
        # The option for the stack group. You can specify up to one option.
        self.capabilities = capabilities
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.client_token = client_token
        self.deployment_options = deployment_options
        # The ID of the request.
        self.deployment_targets_shrink = deployment_targets_shrink
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must specify only one of the TemplateBody, TemplateURL, and TemplateId parameters.
        self.description = description
        # The value of parameter N.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you set the Parameters parameter, you must set the Parameters.N.ParameterValue parameter.
        self.execution_role_name = execution_role_name
        # The version of the template. If you do not specify a version, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is set.
        self.operation_description = operation_description
        # The list of parameters.
        self.operation_preferences_shrink = operation_preferences_shrink
        # Specifies whether to enable automatic deployment.
        # 
        # Valid values:
        # 
        # *   true: enables automatic deployment. If you add a member to the folder to which the stack group belongs after you enable automatic deployment, the stack group deploys its stack instances within the member. If you remove a member from the folder, the stack group deletes stack instances that are deployed within the member.
        # *   false: disables automatic deployment. After you disable automatic deployment, the stack instances remain unchanged even if members in the folder change.
        self.parameters = parameters
        # The folder IDs in the resource directory. You can specify a maximum of five folder IDs.
        # 
        # You must set at least one of the RdFolderIds and AccountIds parameters. The parameters are subject to the following items:
        # 
        # *   If you set only the RdFolderIds parameter, stacks are deployed within all the members in the specified folders. If you specify the Root folder, ROS deploys the stacks within all the members in the resource directory.
        # *   If you set only the AccountIds parameter, stacks are deployed within the specified members.
        # *   If you set both parameters, the accounts specified by AccountIds must be contained in the folders specified by RdFolderIds.
        # 
        # >  To view the folder IDs, go to the **Overview** page in the **Resource Management** console. For more information, see [View the basic information of a folder](https://help.aliyun.com/document_detail/111223.html).
        self.permission_model = permission_model
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The description of the operation to update the stack group.
        self.region_ids_shrink = region_ids_shrink
        # The region IDs of stack instances. You can specify a maximum of 20 region IDs.
        # 
        # This parameter is required.
        self.stack_group_name = stack_group_name
        # The name of the RAM role to be assumed by the administrator account in ROS. This parameter is required if you want to grant self-managed permissions to the stack group. If you do not specify a value for this parameter, the default value AliyunROSStackGroupAdministrationRole is used. You can use the administrator role in ROS to assume the execution role AliyunROSStackGroupExecutionRole to perform operations on the stacks that correspond to stack instances in the stack group.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, and hyphens (-).
        self.template_body = template_body
        # The permission model.
        # 
        # Valid values:
        # 
        # *   SELF_MANAGED: the self-managed permission model. This is the default value. If you use the self-managed model for the stack group, you must create RAM roles for the administrator and execution accounts, and establish a trust relationship between the accounts to deploy stacks within the execution account.
        # *   SERVICE_MANAGED: the service-managed permission model. If you use the service-managed model for the stack group, ROS creates service-linked roles for the administrator and execution accounts, and the administrator account uses its role to deploy stacks within the execution account.
        # 
        # >- If stack instances have been created in the stack group, you cannot switch the permission mode of the stack group.
        # >- If you want to use the service-managed permission model to deploy stacks, your account must be the management account or a delegated administrator account of your resource directory and the trusted access feature is enabled for the account. For more information, see [Step 1: (Optional) Create a delegated administrator account](https://help.aliyun.com/document_detail/308253.html) and [Step 2: Enable trusted access](https://help.aliyun.com/document_detail/298229.html).
        self.template_id = template_id
        # The name of the RAM role to be assumed by the administrator role AliyunROSStackGroupAdministrationRole. This parameter is required if you want to grant self-managed permissions to the stack group. If you do not specify a value for this parameter, the default value AliyunROSStackGroupExecutionRole is used. You can use this role in ROS to perform operations on the stacks that correspond to stack instances in the stack group.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, and hyphens (-).
        self.template_url = template_url
        # The information about automatic deployment settings.
        # 
        # >  This parameter is required only if the PermissionModel parameter is set to SERVICE_MANAGED.
        self.template_version = template_version

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['AccountIds'] = self.account_ids_shrink

        if self.administration_role_name is not None:
            result['AdministrationRoleName'] = self.administration_role_name

        if self.auto_deployment_shrink is not None:
            result['AutoDeployment'] = self.auto_deployment_shrink

        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_options is not None:
            result['DeploymentOptions'] = self.deployment_options

        if self.deployment_targets_shrink is not None:
            result['DeploymentTargets'] = self.deployment_targets_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_role_name is not None:
            result['ExecutionRoleName'] = self.execution_role_name

        if self.operation_description is not None:
            result['OperationDescription'] = self.operation_description

        if self.operation_preferences_shrink is not None:
            result['OperationPreferences'] = self.operation_preferences_shrink

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.permission_model is not None:
            result['PermissionModel'] = self.permission_model

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_ids_shrink is not None:
            result['RegionIds'] = self.region_ids_shrink

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

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
        if m.get('AccountIds') is not None:
            self.account_ids_shrink = m.get('AccountIds')

        if m.get('AdministrationRoleName') is not None:
            self.administration_role_name = m.get('AdministrationRoleName')

        if m.get('AutoDeployment') is not None:
            self.auto_deployment_shrink = m.get('AutoDeployment')

        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentOptions') is not None:
            self.deployment_options = m.get('DeploymentOptions')

        if m.get('DeploymentTargets') is not None:
            self.deployment_targets_shrink = m.get('DeploymentTargets')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionRoleName') is not None:
            self.execution_role_name = m.get('ExecutionRoleName')

        if m.get('OperationDescription') is not None:
            self.operation_description = m.get('OperationDescription')

        if m.get('OperationPreferences') is not None:
            self.operation_preferences_shrink = m.get('OperationPreferences')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.UpdateStackGroupShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('PermissionModel') is not None:
            self.permission_model = m.get('PermissionModel')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionIds') is not None:
            self.region_ids_shrink = m.get('RegionIds')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

class UpdateStackGroupShrinkRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # Specifies whether to retain stacks in a member when you remove the member from the folder.
        # 
        # Valid values:
        # 
        # *   true: retains the stacks.
        # *   false: deletes the stacks.
        # 
        # >  This parameter is required if the Enabled parameter is set to true.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The folders in which you want to use service-managed permissions to update stacks.
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

