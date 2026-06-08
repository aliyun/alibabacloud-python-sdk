# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class PreviewStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disable_rollback: bool = None,
        enable_pre_config: bool = None,
        parallelism: int = None,
        parameters: List[main_models.PreviewStackRequestParameters] = None,
        region_id: str = None,
        stack_id: str = None,
        stack_name: str = None,
        stack_policy_body: str = None,
        stack_policy_url: str = None,
        taint_resources: List[str] = None,
        template_body: str = None,
        template_id: str = None,
        template_scratch_id: str = None,
        template_scratch_region_id: str = None,
        template_url: str = None,
        template_version: str = None,
        timeout_in_minutes: int = None,
        use_previous_parameters: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can be up to 64 characters in length, and can contain letters, digits, underscores (_), and hyphens (-).\\
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # Specifies whether to disable rollback for the resources when the stack fails to be created. Valid values:
        # 
        # *   true
        # *   false (default)
        self.disable_rollback = disable_rollback
        # Specifies whether to query the parameters that you want to use in compliance precheck.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (default)
        self.enable_pre_config = enable_pre_config
        # The maximum number of concurrent operations that can be performed on resources. This parameter takes effect only for Terraform stacks.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > If you set this parameter to an integer greater than 0, the integer is used. If you set this parameter to 0 or leave this parameter empty, the default value of Terraform is used. In most cases, the default value of Terraform is 10.
        self.parallelism = parallelism
        # The parameters of the stack.
        self.parameters = parameters
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The stack ID. You can use this parameter to preview a stack that you want to update.
        # 
        # 
        # 
        # > -  You must and can specify only one of StackName and StackId.
        # > - In the scenario in which you preview a stack that you want to create or update, you cannot preview the resources in its nested stacks.
        self.stack_id = stack_id
        # The stack name. You can use this parameter to preview the stack that you want to create. The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        # 
        # > You must and can specify only one of StackName and StackId.
        self.stack_name = stack_name
        # The structure that contains the stack policy body. The stack policy body must be 1 to 16,384 bytes in length.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        self.stack_policy_body = stack_policy_body
        # The URL of the file that contains the stack policy. The URL must point to a policy that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The policy file can be up to 16,384 bytes in length. If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > You can specify only one of StackPolicyBody and StackPolicyURL.
        # 
        # The URL can be up to 1,350 bytes in length.
        self.stack_policy_url = stack_policy_url
        self.taint_resources = taint_resources
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # > You must and can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, and TemplateScratchId.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
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
        # Unit: minutes.
        # 
        # Default value: 60.
        self.timeout_in_minutes = timeout_in_minutes
        self.use_previous_parameters = use_previous_parameters

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disable_rollback is not None:
            result['DisableRollback'] = self.disable_rollback

        if self.enable_pre_config is not None:
            result['EnablePreConfig'] = self.enable_pre_config

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        if self.stack_name is not None:
            result['StackName'] = self.stack_name

        if self.stack_policy_body is not None:
            result['StackPolicyBody'] = self.stack_policy_body

        if self.stack_policy_url is not None:
            result['StackPolicyURL'] = self.stack_policy_url

        if self.taint_resources is not None:
            result['TaintResources'] = self.taint_resources

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

        if self.use_previous_parameters is not None:
            result['UsePreviousParameters'] = self.use_previous_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisableRollback') is not None:
            self.disable_rollback = m.get('DisableRollback')

        if m.get('EnablePreConfig') is not None:
            self.enable_pre_config = m.get('EnablePreConfig')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.PreviewStackRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('StackName') is not None:
            self.stack_name = m.get('StackName')

        if m.get('StackPolicyBody') is not None:
            self.stack_policy_body = m.get('StackPolicyBody')

        if m.get('StackPolicyURL') is not None:
            self.stack_policy_url = m.get('StackPolicyURL')

        if m.get('TaintResources') is not None:
            self.taint_resources = m.get('TaintResources')

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

        if m.get('UsePreviousParameters') is not None:
            self.use_previous_parameters = m.get('UsePreviousParameters')

        return self

class PreviewStackRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter N. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are specified in the template. Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify Parameters.N.ParameterKey.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N. Maximum value of N: 200.
        # 
        # > If you specify Parameters, you must specify Parameters.N.ParameterValue.
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

