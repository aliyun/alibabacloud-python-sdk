# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GetTemplateParameterConstraintsShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: List[main_models.GetTemplateParameterConstraintsShrinkRequestParameters] = None,
        parameters_key_filter_shrink: str = None,
        parameters_order_shrink: str = None,
        region_id: str = None,
        stack_id: str = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/134212.html).
        self.client_token = client_token
        # The name of parameter N in the template.
        self.parameters = parameters
        # The parameters whose values you want to query.
        self.parameters_key_filter_shrink = parameters_key_filter_shrink
        # The order in which associated parameters are arranged.
        # 
        # >  By default, the order of the associated parameters specified in the `Metadata` section of the template is used.
        self.parameters_order_shrink = parameters_order_shrink
        # The region ID of the template.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the stack.
        self.stack_id = stack_id
        # The structure that contains the template body.
        # 
        # The template body must be 1 to 524,288 bytes in length. If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared and private templates.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/stack-policy/demo or oss://ros/stack-policy/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length. If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # >  You must specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_url = template_url
        # The version of the template. If you do not specify this parameter, the latest version is used.
        # 
        # >  This parameter takes effect only if the TemplateId parameter is specified.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.parameters_key_filter_shrink is not None:
            result['ParametersKeyFilter'] = self.parameters_key_filter_shrink

        if self.parameters_order_shrink is not None:
            result['ParametersOrder'] = self.parameters_order_shrink

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GetTemplateParameterConstraintsShrinkRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('ParametersKeyFilter') is not None:
            self.parameters_key_filter_shrink = m.get('ParametersKeyFilter')

        if m.get('ParametersOrder') is not None:
            self.parameters_order_shrink = m.get('ParametersOrder')

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

class GetTemplateParameterConstraintsShrinkRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterKey parameter.
        # 
        # This parameter is required.
        self.parameter_key = parameter_key
        # The value of parameter N in the template.
        # 
        # >  The Parameters parameter is optional. If you specify the Parameters parameter, you must specify the Parameters.N.ParameterValue parameter.
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

