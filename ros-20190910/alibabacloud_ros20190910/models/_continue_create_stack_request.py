# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ContinueCreateStackRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        mode: str = None,
        parallelism: int = None,
        parameters: List[main_models.ContinueCreateStackRequestParameters] = None,
        ram_role_name: str = None,
        recreating_options: List[str] = None,
        recreating_resources: List[str] = None,
        region_id: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # Specifies whether only to validate the stack in the request. Valid values:
        # 
        # *   true: only validates the stack.
        # *   false (default): validates and continues to create the stack.
        self.dry_run = dry_run
        # The mode in which ROS continues to create the stack. Valid values:
        # 
        # *   Recreate (default)
        # 
        #     If you set this parameter to Recreate, ROS continues to create only the following types of resources:
        # 
        #     *   Resources that fail to be created
        #     *   Resources that you specify for RecreatingResources.N
        #     *   Dependencies of the resources that you specify for RecreatingResources.N
        #     *   Resources that you have not created
        # 
        # > RecreatingResources.N, TemplateBody, TemplateURL, and Parameters take effect only when Mode is set to Recreate.
        # 
        # *   Ignore
        # 
        #     *   ROS ignores and discards resources that fail to be created and you have not created, and considers that the stack is successfully created.
        #     *   The body of the template that you use to create the stack is changed.
        # 
        # > This mode is available only for ROS stacks.
        self.mode = mode
        # The maximum number of concurrent operations that can be performed on resources.
        # 
        # By default, this parameter is empty. You can set this parameter to an integer that is greater than or equal to 0.
        # 
        # > - If you set this parameter to an integer that is greater than 0, the integer is used.
        # > - If you set this parameter to 0, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you leave this parameter empty, the value that you specified for this parameter in the previous request is used. If you left this parameter empty in the previous request, no limit is imposed on ROS stacks. However, the default value in Terraform is used for Terraform stacks. In most cases, the default value in Terraform is 10.
        # > - If you set this parameter to a specific value, ROS associates the value with the stack. The value affects subsequent operations on the stack.
        self.parallelism = parallelism
        # The template parameters that you want to use to override specific parameters.
        self.parameters = parameters
        # The name of the RAM role. Resource Orchestration Service (ROS) assumes the RAM role to create the stack and uses the credentials of the role to call the APIs of Alibaba Cloud services.\\
        # ROS assumes the RAM role to perform operations on the stack. If you have permissions to perform operations on the stack but do not have permissions to use the RAM role, ROS still assumes the RAM role. You must make sure that the least privileges are granted to the RAM role.\\
        # If you do not specify this parameter, ROS assumes the existing role that is associated with the stack. If no roles are available, ROS uses a temporary credential that is generated from the credentials of your account.\\
        # The name of the RAM role can be up to 64 bytes in length.
        self.ram_role_name = ram_role_name
        # The options that ROS adopts when ROS continues to create the stack.
        self.recreating_options = recreating_options
        # The resources that ROS continues to create after the resources failed to be created. You can add new resources to the resources that ROS continues to create. ROS continues to create all dependencies of the new resources.
        # 
        # > This parameter is available only for ROS stacks.
        self.recreating_resources = recreating_resources
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The stack ID.
        # 
        # This parameter is required.
        self.stack_id = stack_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.\\
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # A ROS template is subject to the following limits:
        # 
        # *   You can modify only the following sections in the template: Description, Metadata, Resources, and Outputs.
        # 
        # *   You cannot add sections to or remove sections from the template.
        # 
        # *   The Resources section is subject to the following limits:
        # 
        #     *   You cannot delete the resources or change the template body for the resources that you do not want to continue to create.
        #     *   You can delete the resources or change the template body for the resources that you want to continue to create.
        #     *   You can add resources to this section.
        # 
        #  
        # 
        # > - This parameter takes effect only when Mode is set to Recreate.
        # > - You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId. If you do not specify the parameters, the existing template is used.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # > - This parameter takes effect when `Mode` is set to `Recreate`. When you specify TemplateId of a template, the template is subject to the limits that are described for `TemplateBody` in this topic.
        # > - You can specify only one of the following parameters: `TemplateBody`, `TemplateURL`, and `TemplateId`. If you do not specify the parameters, the existing template is used.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # > - This parameter takes effect only when Mode is set to Recreate. When you specify TemplateURL of a template, the template is subject to the limits that are described for TemplateBody in this topic.
        # > - You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId. If you do not specify the parameters, the existing template is used.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when TemplateId is specified.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.recreating_options is not None:
            result['RecreatingOptions'] = self.recreating_options

        if self.recreating_resources is not None:
            result['RecreatingResources'] = self.recreating_resources

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.ContinueCreateStackRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RecreatingOptions') is not None:
            self.recreating_options = m.get('RecreatingOptions')

        if m.get('RecreatingResources') is not None:
            self.recreating_resources = m.get('RecreatingResources')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self



class ContinueCreateStackRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of template parameter N that you want to use to override a specific parameter. If you do not specify the name and value of a template parameter, ROS uses the name and value specified in the previous operation that was performed to create the stack. Maximum value of N: 200.
        # 
        # > This parameter takes effect only when Mode is set to Recreate.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of template parameter N that you want to use to override a specific parameter. Maximum value of N: 200.
        # 
        # For ROS stacks, the template parameters that you use to override specific parameters are subject to the following limits:
        # 
        # *   You cannot change the condition values in the Conditions section of a template from true to false or from false to true.
        # *   The template parameters can be referenced only by resources that ROS continues to create.
        # 
        # > This parameter takes effect only when Mode is set to Recreate.
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

