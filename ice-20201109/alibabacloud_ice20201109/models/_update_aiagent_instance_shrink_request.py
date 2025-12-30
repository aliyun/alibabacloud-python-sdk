# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAIAgentInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_config_shrink: str = None,
        instance_id: str = None,
        template_config_shrink: str = None,
        user_data: str = None,
    ):
        self.agent_config_shrink = agent_config_shrink
        # The ID of the AI agent that you want to update.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The template configurations of the AI agent. The configurations are merged with the template configurations that are used to start the AI agent. For more information, see the definition of TemplateConfig.
        self.template_config_shrink = template_config_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_config_shrink is not None:
            result['AgentConfig'] = self.agent_config_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.template_config_shrink is not None:
            result['TemplateConfig'] = self.template_config_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentConfig') is not None:
            self.agent_config_shrink = m.get('AgentConfig')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TemplateConfig') is not None:
            self.template_config_shrink = m.get('TemplateConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

