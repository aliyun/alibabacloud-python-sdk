# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkAgentRunParameters(DaraModel):
    def __init__(
        self,
        agent_runtime_name: str = None,
        body: main_models.SinkAgentRunParametersBody = None,
        endpoint_name: str = None,
        role_name: str = None,
        timeout: str = None,
    ):
        # The name of the AgentRun agent runtime. You can obtain it from the Alibaba Cloud AgentRun console.
        self.agent_runtime_name = agent_runtime_name
        # The triplet configuration for the Body parameter template. It defines the data transformation method and supports two modes: ORIGINAL (pass-through) and TEMPLATE (template replacement).
        self.body = body
        # The endpoint name of the AgentRun agent runtime, which is used to construct the invocation URL.
        self.endpoint_name = endpoint_name
        # The name of the AgentRun agent role.
        self.role_name = role_name
        # The HTTP request timeout period in milliseconds. Default value: 30000.
        self.timeout = timeout

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_runtime_name is not None:
            result['AgentRuntimeName'] = self.agent_runtime_name

        if self.body is not None:
            result['Body'] = self.body.to_map()

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentRuntimeName') is not None:
            self.agent_runtime_name = m.get('AgentRuntimeName')

        if m.get('Body') is not None:
            temp_model = main_models.SinkAgentRunParametersBody()
            self.body = temp_model.from_map(m.get('Body'))

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class SinkAgentRunParametersBody(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        # The transformation format. Default value: CONSTANT. Valid values: ORIGINAL, TEMPLATE. Example: `ORIGINAL`.
        self.form = form
        # The template pattern. This parameter is required only when Form is set to TEMPLATE. It supports ${variable} placeholder replacement. Example: `The value of ${key} is ${value}!`.
        self.template = template
        # The parameter value. In ORIGINAL mode, the value is $. In TEMPLATE mode, the value is a key-value mapping in JSON format, where the value is a JSONPath expression or a constant. Example: `$`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

