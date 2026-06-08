# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class CreateStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        create_option: str = None,
        create_options: List[str] = None,
        deletion_protection: str = None,
        disable_rollback: bool = None,
        notification_urls: List[str] = None,
        parallelism: int = None,
        parameters: List[main_models.CreateStackRequestParameters] = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
        tags: List[main_models.CreateStackRequestTags] = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The creation option for the stack. Valid values:
        # 
        # *   KeepStackOnCreationComplete (default): After the stack is created, the stack and its resources are retained. The quota for the maximum number of stacks that can be created in ROS is consumed.
        # *   AbandonStackOnCreationComplete: After the stack is created, the stack is deleted, but its resources are retained. The quota for the maximum number of stacks that can be created in ROS is not consumed. If the stack fails to be created, the stack is retained.
        # *   AbandonStackOnCreationRollbackComplete: When the resources of the stack are rolled back after the stack fails to be created, the stack is deleted. The quota for the maximum number of stacks that can be created in ROS is not consumed. In other rollback scenarios, the stack is retained.
        # *   ManuallyPay: When you create the stack, you must manually pay for the subscription resources that are used. The following resource types support manual payment: `ALIYUN::ECS::InstanceGroup`, `ALIYUN::RDS::DBInstance`, `ALIYUN::SLB::LoadBalancer`, `ALIYUN::VPC::EIP`, and `ALIYUN::VPC::VpnGateway`.
        # 
        # >  You can specify only one of CreateOption and CreateOptions.
        self.create_option = create_option
        # The creation options for the stack.
        self.create_options = create_options
        # Specifies whether to enable deletion protection for the stack. Valid values:
        # 
        # *   Enabled.
        # *   Disabled (default). If deletion protection is disabled, you can delete the stack by using the ROS console or by calling the DeleteStack operation.
        # 
        # > The value of DeletionProtection that you specify for the root stack applies to its nested stacks.
        self.deletion_protection = deletion_protection
        # Specifies whether to disable rollback for the resources when the stack fails to be created.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # The callback URLs that are used to receive stack events. Valid values:
        # 
        # *   HTTP POST URL
        # 
        # Each URL can be up to 1,024 bytes in length.
        # 
        # *   eventbridge
        # 
        # When the status of a stack changes, ROS sends notifications to the EventBridge service. You can view the event information in the [EventBridge](https://eventbridge.console.aliyun.com) console.
        # 
        # > This feature is supported in the China (Hangzhou), China (Shanghai), China (Beijing), China (Hong Kong), and China (Zhangjiakou) regions.
        # 
        # Maximum value of N: 5. When the status of a stack changes, ROS sends a notification to the specified URL. When rollback is enabled for the stack, notifications are sent if the stack is in the CREATE_ROLLBACK or ROLLBACK state, but are not sent if the stack is in the CREATE_FAILED, UPDATE_FAILED, or IN_PROGRESS state.\\
        # ROS sends notifications regardless of whether you specify the Outputs section. The following sample code provides an example on the content of a notification:
        # 
        #     {
        #        "Outputs": [
        #            {
        #                "Description": "No description given",
        #                "OutputKey": "InstanceId",
        #                "OutputValue": "i-xxx"
        #            }
        #        ],
        #        "StackId": "80bd6b6c-e888-4573-ae3b-93d29113****",
        #        "StackName": "test-notification-url",
        #        "Status": "CREATE_COMPLETE"
        #     }
        self.notification_urls = notification_urls
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # 
        # 
        # > -  If you set this parameter to an integer that is greater than 0, the integer is used. If you set this parameter to 0 or leave this parameter empty, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > -  If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack, such as an update operation.
        self.parallelism = parallelism
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The name of the RAM role. ROS assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.
        # 
        # If you do not specify this parameter, ROS assumes the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.
        # 
        # The RAM role name can be up to 64 characters in length.
        self.ram_role_name = ram_role_name
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group. If you leave this parameter empty, the stack is added to the default resource group.
        # 
        # For more information about resource groups, see the "Resource group" section of the [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html) topic.
        self.resource_group_id = resource_group_id
        # The name of the stack.\\
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a letter.
        # 
        # This parameter is required.
        self.stack_name = stack_name
        # The structure that contains the stack policy body. The policy body must be 1 to 16,384 bytes in length.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        self.stack_policy_body = stack_policy_body
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        # The tags that you want to add to the stack.
        self.tags = tags
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_body = template_body
        # The template ID. This parameter applies to shared templates and private templates.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_id = template_id
        # The scenario ID.
        # 
        # For more information about how to query the scenario ID, see [ListTemplateScratches](https://help.aliyun.com/document_detail/363050.html).
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_scratch_id = template_scratch_id
        # The region ID of the scenario. The default value is the same as the value of RegionId.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        self.template_scratch_region_id = template_scratch_region_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an OSS bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when TemplateId is specified.
        self.template_version = template_version
        # The timeout period for creating the stack.
        # 
        # *   Default value: 60.
        # *   Unit: minutes.
        # *   Valid values: 10 to 1440.
        self.timeout_in_minutes = timeout_in_minutes

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

        if self.create_option is not None:
            result['CreateOption'] = self.create_option

        if self.create_options is not None:
            result['CreateOptions'] = self.create_options

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        if self.template_scratch_region_id is not None:
            result['TemplateScratchRegionId'] = self.template_scratch_region_id

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CreateOption') is not None:
            self.create_option = m.get('CreateOption')

        if m.get('CreateOptions') is not None:
            self.create_options = m.get('CreateOptions')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('NotificationURLs') is not None:
            self.notification_urls = m.get('NotificationURLs')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateStackRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateScratchRegionId') is not None:
            self.template_scratch_region_id = m.get('TemplateScratchRegionId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class CreateStackRequestTags(DaraModel):
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
        # > -  The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](https://help.aliyun.com/document_detail/201421.html).
        # 
        # This parameter is required.
        self.key = key
        # The value of tag N that you want to add to the stack.
        # 
        # Valid values of N: 1 to 20.
        # 
        # > The tag of a stack is propagated to each resource that supports the tag feature in the stack. For more information, see [Propagate tags](https://help.aliyun.com/document_detail/201421.html).
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

class CreateStackRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The key of parameter N that is defined in the template. If you do not specify the name and value of a parameter, ROS uses the default name and value that are specified in the template.
        # 
        # Maximum value of N: 200.\\
        # The name must be 1 to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template.
        # 
        # Maximum value of N: 200.\\
        # The value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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

