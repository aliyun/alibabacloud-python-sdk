# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class UpdateMmAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        binding_config: main_models.UpdateMmAppRequestBindingConfig = None,
        conversation_config: main_models.UpdateMmAppRequestConversationConfig = None,
        model_config: main_models.UpdateMmAppRequestModelConfig = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        self.binding_config = binding_config
        self.conversation_config = conversation_config
        self.model_config = model_config
        self.prompt = prompt
        self.workspace_id = workspace_id

    def validate(self):
        if self.binding_config:
            self.binding_config.validate()
        if self.conversation_config:
            self.conversation_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()

        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BindingConfig') is not None:
            temp_model = main_models.UpdateMmAppRequestBindingConfig()
            self.binding_config = temp_model.from_map(m.get('BindingConfig'))

        if m.get('ConversationConfig') is not None:
            temp_model = main_models.UpdateMmAppRequestConversationConfig()
            self.conversation_config = temp_model.from_map(m.get('ConversationConfig'))

        if m.get('ModelConfig') is not None:
            temp_model = main_models.UpdateMmAppRequestModelConfig()
            self.model_config = temp_model.from_map(m.get('ModelConfig'))

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateMmAppRequestModelConfig(DaraModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_web_search = open_web_search
        self.text_modal = text_modal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search

        if self.text_modal is not None:
            result['TextModal'] = self.text_modal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')

        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')

        return self

class UpdateMmAppRequestConversationConfig(DaraModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.tts_model = tts_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_model is not None:
            result['AsrModel'] = self.asr_model

        if self.open_asr is not None:
            result['OpenAsr'] = self.open_asr

        if self.open_tts is not None:
            result['OpenTts'] = self.open_tts

        if self.tts_model is not None:
            result['TtsModel'] = self.tts_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModel') is not None:
            self.asr_model = m.get('AsrModel')

        if m.get('OpenAsr') is not None:
            self.open_asr = m.get('OpenAsr')

        if m.get('OpenTts') is not None:
            self.open_tts = m.get('OpenTts')

        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')

        return self

class UpdateMmAppRequestBindingConfig(DaraModel):
    def __init__(
        self,
        commands: List[main_models.UpdateMmAppRequestBindingConfigCommands] = None,
    ):
        self.commands = commands

    def validate(self):
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.UpdateMmAppRequestBindingConfigCommands()
                self.commands.append(temp_model.from_map(k1))

        return self

class UpdateMmAppRequestBindingConfigCommands(DaraModel):
    def __init__(
        self,
        domain_code: str = None,
        tools: List[main_models.UpdateMmAppRequestBindingConfigCommandsTools] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.domain_code = domain_code
        self.tools = tools
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.UpdateMmAppRequestBindingConfigCommandsTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateMmAppRequestBindingConfigCommandsTools(DaraModel):
    def __init__(
        self,
        tool_id: str = None,
    ):
        # This parameter is required.
        self.tool_id = tool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        return self

