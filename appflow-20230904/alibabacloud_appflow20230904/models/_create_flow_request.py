# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class CreateFlowRequest(DaraModel):
    def __init__(
        self,
        flow_desc: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_template: str = None,
        launch_status: bool = None,
        parameters: List[main_models.CreateFlowRequestParameters] = None,
        tag: List[main_models.CreateFlowRequestTag] = None,
        template_id: str = None,
    ):
        self.flow_desc = flow_desc
        self.flow_id = flow_id
        # This parameter is required.
        self.flow_name = flow_name
        self.flow_template = flow_template
        self.launch_status = launch_status
        self.parameters = parameters
        self.tag = tag
        self.template_id = template_id

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_desc is not None:
            result['FlowDesc'] = self.flow_desc

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_template is not None:
            result['FlowTemplate'] = self.flow_template

        if self.launch_status is not None:
            result['LaunchStatus'] = self.launch_status

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowDesc') is not None:
            self.flow_desc = m.get('FlowDesc')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowTemplate') is not None:
            self.flow_template = m.get('FlowTemplate')

        if m.get('LaunchStatus') is not None:
            self.launch_status = m.get('LaunchStatus')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.CreateFlowRequestParameters()
                self.parameters.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFlowRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class CreateFlowRequestTag(DaraModel):
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



class CreateFlowRequestParameters(DaraModel):
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

