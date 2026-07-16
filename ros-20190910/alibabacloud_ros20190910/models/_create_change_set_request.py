# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateChangeSetRequest(DaraModel):
    def __init__(
        self,
        change_set_name: str = None,
        change_set_type: str = None,
        client_token: str = None,
        description: str = None,
        disable_rollback: bool = None,
        notification_urls: List[str] = None,
        parallelism: int = None,
        parameters: List[main_models.CreateChangeSetRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        replacement_option: str = None,
        resource_group_id: str = None,
        resources_to_import: List[main_models.CreateChangeSetRequestResourcesToImport] = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_during_update_body: str = None,
        stack_policy_during_update_url: str = None,
        stack_policy_url: str = None,
        tags: List[main_models.CreateChangeSetRequestTags] = None,
        taint_resources: List[str] = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        use_previous_parameters: bool = None,
    ):
        # The name of the change set.\\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). The name must start with a digit or a letter.
        # 
        # > Make sure that the name is unique among all names of change sets that are associated with the specified stack.
        # 
        # This parameter is required.
        self.change_set_name = change_set_name
        # The type of the change set. Valid values:
        # 
        # *   CREATE: creates a change set for a new stack.
        # *   UPDATE (default): creates a change set for an existing stack.
        # *   IMPORT: creates a change set for a new stack or an existing stack to import resources that are not managed by ROS.
        # 
        # If you set ChangeSetType to CREATE, ROS creates a stack. The stack remains in the `REVIEW_IN_PROGRESS` state until you execute the change set.
        # 
        # > 
        # 
        # *   You cannot set ChangeSetType to UPDATE when you create a change set for a new stack. You cannot set ChangeSetType to CREATE when you create a change set for an existing stack.
        # 
        # *   If you set ChangeSetType to Import, you cannot configure a stack policy. You can specify ChangeSetType only when you create or update a stack.
        self.change_set_type = change_set_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests.\\
        # The token can contain letters, digits, hyphens (-), and underscores (_) and cannot exceed 64 characters in length.\\
        # For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The description of the change set. The description can be up to 1,024 bytes in length.
        self.description = description
        # Specifies whether to disable rollback when the stack fails to be created.\\
        # Valid values:
        # 
        # *   true: disables rollback for the stack when the stack fails to be created.
        # *   false (default): enables rollback for the stack when the stack fails to be created.
        # 
        # > This parameter takes effect only if you set ChangeSetType to CREATE or IMPORT.
        self.disable_rollback = disable_rollback
        # The callback URLs that are used to receive stack events.
        self.notification_urls = notification_urls
        # The maximum number of concurrent operations that can be performed on resources. By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0. If you set this parameter to a specific value, ROS associates the value with the stack. The value can affect subsequent operations on the stack.
        # 
        # This parameter takes effect only if you set ChangeSetType to CREATE or UPDATE.
        # 
        # *   Valid values for change sets of the CREATE type:
        # 
        #     *   If you set this parameter to an integer that is greater than 0, the integer is used.
        #     *   If you set this parameter to 0 or leave this parameter empty, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # 
        # *   Valid values for change sets of the UPDATE type:
        # 
        #     *   If you set this parameter to an integer that is greater than 0, the integer is used.
        #     *   If you set this parameter to 0, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        #     *   If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        self.parallelism = parallelism
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The name of the Resource Access Management (RAM) role. ROS assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack, ROS assumes the RAM role even if you do not have permissions to use the RAM role. You must make sure that permissions are granted to the RAM role based on the principle of least privilege.\\
        # If you do not specify this parameter, ROS assumes the existing role of the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\\
        # The RAM role name can be up to 64 characters in length.
        # 
        # For more information about RAM roles, see [Use a stack role](https://help.aliyun.com/document_detail/2568025.html).
        self.ram_role_name = ram_role_name
        # The region ID of the change set.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable replacement update if a resource property is changed and you cannot modify the new resource property. For a change, the physical ID of the resource remains unchanged. For a replacement update, the existing resource is deleted, a new resource is created, and the physical ID of the resource is changed. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        # 
        # > Operations that you perform to modify the resource properties for an update take precedence over operations you perform to replace the resource properties for an update. This parameter takes effect only if you set ChangeSetType to UPDATE.
        self.replacement_option = replacement_option
        self.resource_group_id = resource_group_id
        # The resources that you want to import to the stack.
        self.resources_to_import = resources_to_import
        # The ID of the stack for which you want to create the change set. ROS compares the stack information with the information that you submit, such as an updated template or parameter value, to generate the change set.\\
        # You can call the [ListStacks](https://help.aliyun.com/document_detail/610818.html) operation to query the stack ID.
        # 
        # >  This parameter takes effect only when ChangeSetType is set to UPDATE or IMPORT.
        self.stack_id = stack_id
        # The name of the stack for which you want to create the change set.\\
        # The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (_). The name must start with a digit or a letter.
        # 
        # > This parameter takes effect only if you set ChangeSetType to CREATE or IMPORT.
        self.stack_name = stack_name
        # The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length.
        # 
        # If you set ChangeSetType to **CREATE**, you can specify StackPolicyBody or StackPolicyURL.
        # 
        # If you set ChangeSetType to **UPDATE**, you can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_body = stack_policy_body
        # The structure of the temporary overriding stack policy. The policy body must be 1 to 16,384 bytes in length.\\
        # If you need to update protected resources, specify a temporary overriding stack policy for the resources during the update. If you do not specify a temporary overriding stack policy, the existing stack policy that is associated with the stack is used.\\
        # This parameter takes effect only if you set ChangeSetType to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_body = stack_policy_during_update_body
        # The URL of the stack policy based on which the stack is updated. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/stack-policy/demo and oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # > If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # The URL can be up to 1,350 bytes in length.\\
        # If you need to update protected resources, specify a temporary overriding stack policy for the resources during the update. If you do not specify a stack policy, the existing policy that is associated with the stack is used. This parameter takes effect only if you set ChangeSetType to UPDATE. You can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_during_update_url = stack_policy_during_update_url
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length.
        # 
        # The URL can be up to 1,350 bytes in length.
        # 
        # >  If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # If you set ChangeSetType to **CREATE**, you can specify StackPolicyBody or StackPolicyURL.
        # 
        # If you set ChangeSetType to **UPDATE**, you can specify only one of the following parameters:
        # 
        # *   StackPolicyBody
        # *   StackPolicyURL
        # *   StackPolicyDuringUpdateBody
        # *   StackPolicyDuringUpdateURL
        self.stack_policy_url = stack_policy_url
        self.tags = tags
        self.taint_resources = taint_resources
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must and can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The template ID. This parameter applies to shared templates and private templates.
        # 
        # You can call the [ListTemplates](https://help.aliyun.com/document_detail/610842.html) operation to query the template ID.
        # 
        # >  You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The ID of the resource scenario. In this example, this parameter specifies the ID of a resource management scenario.
        # 
        # This parameter takes effect only when ChangeSetType is set to IMPORT. TemplateScratchId is supported only when you import resources to create a new stack.
        # 
        # If you want to use a resource management scenario to import resources, you can specify only TemplateScratchId rather than configuring parameters related to templates.
        # 
        # You can call the [ListTemplateScratches](https://help.aliyun.com/document_detail/610832.html) operation to query the ID of the resource management scenario.
        self.template_scratch_id = template_scratch_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo and oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template.
        # 
        # > This parameter takes effect only if you specify TemplateId.
        self.template_version = template_version
        # The amount of time that can elapse before the stack enters the CREATE_FAILED or UPDATE_FAILED state.\\
        # If you set ChangeSetType to CREATE, this parameter is required. If you set ChangeSetType to UPDATE, this parameter is optional.
        # 
        # *   Unit: minutes.
        # *   Valid values: 10 to 1440.
        # *   Default value: 60.
        self.timeout_in_minutes = timeout_in_minutes
        # Specifies whether to use the values that were passed last time for the parameters that you do not specify in the current request. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # > This parameter takes effect only if you set ChangeSetType to UPDATE or IMPORT.
        self.use_previous_parameters = use_previous_parameters

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.resources_to_import:
            for v1 in self.resources_to_import:
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
        if self.change_set_name is not None:
            result['ChangeSetName'] = self.change_set_name

        if self.change_set_type is not None:
            result['ChangeSetType'] = self.change_set_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.notification_urls is not None:
            result['NotificationURLs'] = self.notification_urls

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

        result['ResourcesToImport'] = []
        if self.resources_to_import is not None:
            for k1 in self.resources_to_import:
                result['ResourcesToImport'].append(k1.to_map() if k1 else None)

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

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

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

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
        if m.get('ChangeSetName') is not None:
            self.change_set_name = m.get('ChangeSetName')

        if m.get('ChangeSetType') is not None:
            self.change_set_type = m.get('ChangeSetType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateChangeSetRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReplacementOption') is not None:
            self.replacement_option = m.get('ReplacementOption')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resources_to_import = []
        if m.get('ResourcesToImport') is not None:
            for k1 in m.get('ResourcesToImport'):
                temp_model = main_models.CreateChangeSetRequestResourcesToImport()
                self.resources_to_import.append(temp_model.from_map(k1))

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

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
                temp_model = main_models.CreateChangeSetRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaintResources') is not None:
            self.taint_resources = m.get('TaintResources')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')

        return self

class CreateChangeSetRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class CreateChangeSetRequestResourcesToImport(DaraModel):
    def __init__(
        self,
        logical_resource_id: str = None,
        resource_identifier: str = None,
        resource_type: str = None,
    ):
        # The logical ID of resource N. The logical ID is the name of the resource defined in the template.
        # 
        # >  This parameter takes effect only when ChangeSetType is set to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must specify ResourcesToImport.N.LogicalResourceId.
        self.logical_resource_id = logical_resource_id
        # The key-value mapping between strings. The key-value mapping is used to identify resource N that you want to import. The key-value mapping must be a JSON string.\\
        # A key is an identifier property of a resource and a value is the property value. For example, the key of the ALIYUN::ECS::VPC resource is VpcId and the value is `vpc-2zevx9ios****`.
        # 
        # You can call the [GetTemplateSummary](https://help.aliyun.com/document_detail/172485.html) operation to query the identifier property of the resource.
        # 
        # >  This parameter takes effect only when ChangeSetType is set to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must specify ResourcesToImport.N.ResourceIdentifier.
        self.resource_identifier = resource_identifier
        # The type of resource N. The resource type must be the same as the resource type that is defined in the template.
        # 
        # >  This parameter takes effect only when ChangeSetType is set to IMPORT. ResourcesToImport is optional. If you specify ResourcesToImport, you must specify ResourcesToImport.N.ResourceType.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logical_resource_id is not None:
            result['LogicalResourceId'] = self.logical_resource_id

        if self.resource_identifier is not None:
            result['ResourceIdentifier'] = self.resource_identifier

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicalResourceId') is not None:
            self.logical_resource_id = m.get('LogicalResourceId')

        if m.get('ResourceIdentifier') is not None:
            self.resource_identifier = m.get('ResourceIdentifier')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class CreateChangeSetRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N that is defined in the template. If you do not specify the key and value of a parameter, ROS uses the default name and value that are defined in the template. Maximum value of N: 200.
        # 
        # >  Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterKey.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template. Maximum value of N: 200.
        # 
        # >  Parameters is optional. If you specify Parameters, you must also specify Parameters.N.ParameterValue.
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

