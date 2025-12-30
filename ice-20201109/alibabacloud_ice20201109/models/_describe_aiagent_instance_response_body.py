# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DescribeAIAgentInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.DescribeAIAgentInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The information about the AI agent.
        self.instance = instance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = main_models.DescribeAIAgentInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAIAgentInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        agent_config: main_models.AIAgentConfig = None,
        call_log_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        runtime_config: main_models.AIAgentRuntimeConfig = None,
        session_id: str = None,
        status: str = None,
        template_config: main_models.AIAgentTemplateConfig = None,
        user_data: str = None,
    ):
        self.agent_config = agent_config
        # The URL of the call log file.
        self.call_log_url = call_log_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        # The runtime configurations of the AI agent.
        self.runtime_config = runtime_config
        self.session_id = session_id
        # The state of the AI agent. Valid values: Finished and Executing.
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.runtime_config is not None:
            result['RuntimeConfig'] = self.runtime_config.to_map()

        if self.session_id is not None:
            result['SessionId'] = self.session_id

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('RuntimeConfig') is not None:
            temp_model = main_models.AIAgentRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('RuntimeConfig'))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.AIAgentTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

