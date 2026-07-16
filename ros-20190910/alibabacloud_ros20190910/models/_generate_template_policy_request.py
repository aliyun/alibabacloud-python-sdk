# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class GenerateTemplatePolicyRequest(DaraModel):
    def __init__(
        self,
        generate_options: List[str] = None,
        operation_types: List[str] = None,
        parameters: List[main_models.GenerateTemplatePolicyRequestParameters] = None,
        template_body: str = None,
        template_id: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        self.generate_options = generate_options
        # The type of operation N for which you want to generate the policy information.
        # 
        # Valid values:
        # 
        # *   CreateStack: creates a stack by calling the CreateStack operation.
        # *   UpdateStack: updates a stack by calling the UpdateStack operation.
        # *   DeleteStack: deletes a stack by calling the DeleteStack operation.
        # *   DetectStackDrift: detects drifts on a stack by calling the DelectStackDrift operation.
        # *   ListStackOperationRisks: lists the risks of a deletion operation on a stack by setting the OperationType parameter to DeleteStack in the ListStackOperationRisks operation.
        # *   GetTemplateEstimateCost: queries the estimated prices of resources that you want to use in the template by calling the GetTemplateEstimateCost operation.
        # *   GetTemplateParameterConstraints: queries the values of parameters in the template by calling the GetTemplateParameterConstraints operation.
        # *   ImportResourcesToStack: imports resources to a stack by setting the ChangeSetType parameter to IMPORT in the CreateChangeSet operation.
        # *   SignalResource: sends a signal to a stack.
        # 
        # >  The default value is the combination of all valid values.
        self.operation_types = operation_types
        self.parameters = parameters
        # The structure that contains the template body. The template body must be 1 to 524,288 bytes in length.
        # 
        # If the length of the template body exceeds the upper limit, we recommend that you add parameters to the HTTP POST request body to prevent request failures caused by excessively long URLs.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_body = template_body
        # The ID of the template. This parameter applies to shared templates and private templates.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        self.template_id = template_id
        # The URL of the file that contains the template body. The URL must point to a template that is located on an HTTP or HTTPS web server or in an Object Storage Service (OSS) bucket, such as oss://ros/template/demo or oss://ros/template/demo?RegionId=cn-hangzhou. The template body can be up to 524,288 bytes in length.
        # 
        # >  If you do not specify the region ID of the OSS bucket, the value of the RegionId parameter is used.
        # 
        # You can specify only one of the following parameters: TemplateBody, TemplateURL, and TemplateId.
        # 
        # The URL can be up to 1,024 bytes in length.
        self.template_url = template_url
        # The version of the template. This parameter takes effect only when the TemplateId parameter is specified.
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
        if self.generate_options is not None:
            result['GenerateOptions'] = self.generate_options

        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

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
        if m.get('GenerateOptions') is not None:
            self.generate_options = m.get('GenerateOptions')

        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.GenerateTemplatePolicyRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

class GenerateTemplatePolicyRequestParameters(DaraModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
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

