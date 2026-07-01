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
        # The AI agent configuration to update. This configuration is merged with the existing configuration of the instance. For more information, see the AIAgentConfig definition. The following parameters in AIAgentConfig can be updated:
        # 
        # - VoiceId
        # 
        # - EnableVoiceInterrupt
        # 
        # - Greeting
        # 
        # - Volume
        # 
        # - EnablePushToTalk
        # 
        # - UseVoiceprint
        # 
        # - BailianAppParams
        self.agent_config_shrink = agent_config_shrink
        # The ID of the AI agent instance.
        # 
        # > This unique ID is returned after the AI agent instance starts successfully. For more information about starting an agent, see [StartAIAgentInstance](https://help.aliyun.com/document_detail/2846201.html) and [GenerateAIAgentCall](https://help.aliyun.com/document_detail/2846209.html).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # > The AI agent template configuration. This parameter is deprecated. Use the AgentConfig parameter instead.
        # 
        # The AI agent configuration to update. This configuration is merged with the existing configuration of the instance. For more information, see the [AIAgentTemplateConfig](https://help.aliyun.com/document_detail/2846193.html) definition.
        # The following parameters in AIAgentTemplateConfig can be updated:
        # 
        # - VoiceId (Voice ID)
        # 
        # - EnableVoiceInterrupt (Enable voice interruption)
        # 
        # - Greeting (Greeting)
        # 
        # - Volume (Volume)
        # 
        # - EnablePushToTalk (Enable push-to-talk)
        # 
        # - UseVoiceprint (Use voiceprint)
        # 
        # - AsrMaxSilence (ASR maximum silence duration)
        self.template_config_shrink = template_config_shrink
        # Custom user data.
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

