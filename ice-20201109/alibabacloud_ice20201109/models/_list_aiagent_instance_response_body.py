# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAIAgentInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListAIAgentInstanceResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The list of the AI agents.
        self.instances = instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListAIAgentInstanceResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAIAgentInstanceResponseBodyInstances(DaraModel):
    def __init__(
        self,
        agent_config: main_models.AIAgentConfig = None,
        call_log_url: str = None,
        runtime_config: main_models.AIAgentRuntimeConfig = None,
        status: str = None,
        template_config: main_models.AIAgentTemplateConfig = None,
        user_data: str = None,
    ):
        self.agent_config = agent_config
        # The URL of the call log file for the AI agent. The structure of the file is CallLog in the JSON format.
        self.call_log_url = call_log_url
        # The runtime configurations of the AI agent.
        self.runtime_config = runtime_config
        # The state of the instance. Valid values:
        # 
        # *   Executing
        # *   Finished
        self.status = status
        # The template configurations of the AI agent.
        self.template_config = template_config
        # The custom information.
        self.user_data = user_data

    def validate(self):
        if self.agent_config:
            self.agent_config.validate()
        if self.runtime_config:
            self.runtime_config.validate()
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config is not None:
            result['AgentConfig'] = self.agent_config.to_map()

        if self.call_log_url is not None:
            result['CallLogUrl'] = self.call_log_url

        if self.runtime_config is not None:
            result['RuntimeConfig'] = self.runtime_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentConfig') is not None:
            temp_model = main_models.AIAgentConfig()
            self.agent_config = temp_model.from_map(m.get('AgentConfig'))

        if m.get('CallLogUrl') is not None:
            self.call_log_url = m.get('CallLogUrl')

        if m.get('RuntimeConfig') is not None:
            temp_model = main_models.AIAgentRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('RuntimeConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.AIAgentTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

