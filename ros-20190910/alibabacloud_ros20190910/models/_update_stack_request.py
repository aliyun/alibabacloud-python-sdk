# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class UpdateStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disable_rollback: bool = None,
        dry_run: bool = None,
        dry_run_options: List[str] = None,
        parallelism: int = None,
        parameters: List[main_models.UpdateStackRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        replacement_option: str = None,
        resource_group_id: str = None,
        stack_id: str = None,
        stack_policy_body: str = None,
        stack_policy_during_update_body: str = None,
        stack_policy_during_update_url: str = None,
        stack_policy_url: str = None,
        tags: List[main_models.UpdateStackRequestTags] = None,
        taint_resources: List[str] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        use_previous_parameters: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.
        # 
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # Specifies whether to roll back the resources in the stack when the stack fails to be updated.
        # 
        # Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.disable_rollback = disable_rollback
        # Specifies whether only to validate the stack in the request. Default value: false. Valid values:
        # 
        # *   true: only validates the stack.
        # *   false: validates and updates the stack.
        # 
        # >  When no changes are made during the update, the following rules apply: If you set the DryRun parameter to false, the NotSupported error code is returned. If you set the DryRun parameter to true, no error is reported.
        self.dry_run = dry_run
        # The dry run option in the list format. You can specify only one dry run option.
        # 
        # > This parameter takes effect only when DryRun is set to true.
        self.dry_run_options = dry_run_options
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > - If you set this parameter to an integer that is greater than 0, the integer is used.
        # > -  If you set this parameter to 0, no limit is imposed on Resource Orchestration Service (ROS) stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > -  If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack.
        self.parallelism = parallelism
        # The parameters.
        self.parameters = parameters
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.
        # 
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.
        # 
        # If you do not specify this parameter, ROS assumes the existing RAM role that is associated with the stack. If no RAM roles are available, ROS uses a temporary credential that is generated from the credentials of your account.
        # 
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The ID of the region in which the stack is deployed. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable the replacement update feature. If you cannot change resource properties, you can enable the replacement update feature to replace the resource properties. If the replacement update feature is used, the existing resource is deleted and a new resource is created. The physical ID of the new resource is different from the physical ID of the deleted resource.
        # 
        # Default value: Disabled. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        # 
        # >  Changes have higher priorities than replacement updates.
        self.replacement_option = replacement_option
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the stack.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length.
        # 
        # >  You can specify only one of the StackPolicyBody and StackPolicyURL parameters.
        self.stack_policy_body = stack_policy_body
        # The structure that contains the body of the temporary overriding stack policy. The policy body must be 1 to 16,384 bytes in length.
        # 
        # If you want to update protected resources, you must specify a temporary overriding stack policy during the update. If you do not specify a temporary overriding stack policy, the existing policy that is associated with the stack is used.
        # 
        # This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_body = stack_policy_during_update_body
        # The URL of the file that contains the temporary overriding stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # >  If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # The URL can be up to 1,350 bytes in length.
        # 
        # If you want to update protected resources, you must specify a temporary overriding stack policy during the update. If you do not specify a temporary overriding stack policy, the existing policy that is associated with the stack is used. This parameter takes effect only when the ChangeSetType parameter is set to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_url = stack_policy_during_update_url
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You can specify only one of the StackPolicyBody and StackPolicyURL parameters.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        # The value of tag N that you want to add to the template.
        self.tags = tags
        self.taint_resources = taint_resources
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.
        # 
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared templates and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body must be 1 to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when the TemplateId parameter is specified.
        self.template_version = template_version
        # The timeout period for the update operation on the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes
        # Specifies whether to use the values specified in the previous request for the parameters that you do not specify in the current request.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.use_previous_parameters = use_previous_parameters

    def validate(self):
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dry_run_options is not None:
            result['DryRunOptions'] = self.dry_run_options

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replacement_option is not None:
            result['ReplacementOption'] = self.replacement_option

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        if self.stack_policy_during_update_body is not None:
            result['StackPolicyDuringUpdateBody'] = self.stack_policy_during_update_body

        if self.stack_policy_during_update_url is not None:
            result['StackPolicyDuringUpdateURL'] = self.stack_policy_during_update_url

        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.taint_resources is not None:
            result['TaintResources'] = self.taint_resources

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('DryRunOptions') is not None:
            self.dry_run_options = m.get('DryRunOptions')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.UpdateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        if m.get('StackPolicyDuringUpdateBody') is not None:
            self.stack_policy_during_update_body = m.get('StackPolicyDuringUpdateBody')

        if m.get('StackPolicyDuringUpdateURL') is not None:
            self.stack_policy_during_update_url = m.get('StackPolicyDuringUpdateURL')

        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UpdateStackRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaintResources') is not None:
            self.taint_resources = m.get('TaintResources')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')

        return self

class UpdateStackRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # > - The Tags parameter is optional. If you specify Tags, you must specify Tags.N.Key.
        # > - The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](https://help.aliyun.com/document_detail/201421.html).
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # >  The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](https://help.aliyun.com/document_detail/201421.html).
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

class UpdateStackRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of parameter N. If you do not specify the name and value of a parameter, ROS uses the default name and value in the template.
        # 
        # Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N. Maximum value of N: 200.
        # 
        # >  The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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

