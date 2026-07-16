# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateSummaryRequest(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        client_token: str = None,
        parameters: List[main_models.GetTemplateSummaryRequestParameters] = None,
        region_id: str = None,
        stack_group_name: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The ID of the change set.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.change_set_id = change_set_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.\\
        # The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).\\
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The parameters that are defined in the template.
        self.parameters = parameters
        # The region ID of the stack or stack group that uses the template. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter takes effect only when one of the following parameters are specified: StackId, ChangeSetId, and StackGroupName.
        self.region_id = region_id
        # The name of the stack group.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.stack_group_name = stack_group_name
        # The stack ID.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.stack_id = stack_id
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.\\
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.\\
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.template_body = template_body
        # The template ID. This parameter applies to shared and private templates.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # > If you do not specify the region ID of the OSS bucket, the value of RegionId is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, TemplateId, StackId, ChangeSetId, and StackGroupName.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template. This parameter takes effect when TemplateId is specified.
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
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

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
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetTemplateSummaryRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

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

class GetTemplateSummaryRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of parameter N that is defined in the template. If you do not specify the name and value of a parameter, Resource Orchestration Service (ROS) uses the default name and value that are defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
        self.parameter_key = parameter_key
        # The value of parameter N that is defined in the template.
        # 
        # Maximum value of N: 200.
        # 
        # > The Parameters parameter is optional. If you specify Parameters, you must specify both Parameters.N.ParameterKey and Parameters.N.ParameterValue.
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

