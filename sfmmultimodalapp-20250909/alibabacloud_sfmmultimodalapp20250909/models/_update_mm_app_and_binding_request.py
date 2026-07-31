# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class UpdateMmAppAndBindingRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        binding_config: main_models.UpdateMmAppAndBindingRequestBindingConfig = None,
        conversation_config: main_models.UpdateMmAppAndBindingRequestConversationConfig = None,
        memory_config: main_models.UpdateMmAppAndBindingRequestMemoryConfig = None,
        model_config: main_models.UpdateMmAppAndBindingRequestModelConfig = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.app_name = app_name
        self.binding_config = binding_config
        self.conversation_config = conversation_config
        self.memory_config = memory_config
        self.model_config = model_config
        self.prompt = prompt
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.binding_config:
            self.binding_config.validate()
        if self.conversation_config:
            self.conversation_config.validate()
        if self.memory_config:
            self.memory_config.validate()
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

        if self.memory_config is not None:
            result['MemoryConfig'] = self.memory_config.to_map()

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
            temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfig()
            self.binding_config = temp_model.from_map(m.get('BindingConfig'))

        if m.get('ConversationConfig') is not None:
            temp_model = main_models.UpdateMmAppAndBindingRequestConversationConfig()
            self.conversation_config = temp_model.from_map(m.get('ConversationConfig'))

        if m.get('MemoryConfig') is not None:
            temp_model = main_models.UpdateMmAppAndBindingRequestMemoryConfig()
            self.memory_config = temp_model.from_map(m.get('MemoryConfig'))

        if m.get('ModelConfig') is not None:
            temp_model = main_models.UpdateMmAppAndBindingRequestModelConfig()
            self.model_config = temp_model.from_map(m.get('ModelConfig'))

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateMmAppAndBindingRequestModelConfig(DaraModel):
    def __init__(
        self,
        enable_intent_recognize: bool = None,
        enable_transition: bool = None,
        history_limit: int = None,
        intent_only_switch: bool = None,
        model_type: str = None,
        open_memory: bool = None,
        open_web_search: bool = None,
        search_model: str = None,
        search_strategy: str = None,
        text_modal: str = None,
        user_prompt_params: List[main_models.UpdateMmAppAndBindingRequestModelConfigUserPromptParams] = None,
        user_query_params: List[main_models.UpdateMmAppAndBindingRequestModelConfigUserQueryParams] = None,
    ):
        self.enable_intent_recognize = enable_intent_recognize
        self.enable_transition = enable_transition
        self.history_limit = history_limit
        self.intent_only_switch = intent_only_switch
        self.model_type = model_type
        self.open_memory = open_memory
        self.open_web_search = open_web_search
        self.search_model = search_model
        self.search_strategy = search_strategy
        self.text_modal = text_modal
        self.user_prompt_params = user_prompt_params
        self.user_query_params = user_query_params

    def validate(self):
        if self.user_prompt_params:
            for v1 in self.user_prompt_params:
                 if v1:
                    v1.validate()
        if self.user_query_params:
            for v1 in self.user_query_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_intent_recognize is not None:
            result['EnableIntentRecognize'] = self.enable_intent_recognize

        if self.enable_transition is not None:
            result['EnableTransition'] = self.enable_transition

        if self.history_limit is not None:
            result['HistoryLimit'] = self.history_limit

        if self.intent_only_switch is not None:
            result['IntentOnlySwitch'] = self.intent_only_switch

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.open_memory is not None:
            result['OpenMemory'] = self.open_memory

        if self.open_web_search is not None:
            result['OpenWebSearch'] = self.open_web_search

        if self.search_model is not None:
            result['SearchModel'] = self.search_model

        if self.search_strategy is not None:
            result['SearchStrategy'] = self.search_strategy

        if self.text_modal is not None:
            result['TextModal'] = self.text_modal

        result['UserPromptParams'] = []
        if self.user_prompt_params is not None:
            for k1 in self.user_prompt_params:
                result['UserPromptParams'].append(k1.to_map() if k1 else None)

        result['userQueryParams'] = []
        if self.user_query_params is not None:
            for k1 in self.user_query_params:
                result['userQueryParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIntentRecognize') is not None:
            self.enable_intent_recognize = m.get('EnableIntentRecognize')

        if m.get('EnableTransition') is not None:
            self.enable_transition = m.get('EnableTransition')

        if m.get('HistoryLimit') is not None:
            self.history_limit = m.get('HistoryLimit')

        if m.get('IntentOnlySwitch') is not None:
            self.intent_only_switch = m.get('IntentOnlySwitch')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('OpenMemory') is not None:
            self.open_memory = m.get('OpenMemory')

        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')

        if m.get('SearchModel') is not None:
            self.search_model = m.get('SearchModel')

        if m.get('SearchStrategy') is not None:
            self.search_strategy = m.get('SearchStrategy')

        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')

        self.user_prompt_params = []
        if m.get('UserPromptParams') is not None:
            for k1 in m.get('UserPromptParams'):
                temp_model = main_models.UpdateMmAppAndBindingRequestModelConfigUserPromptParams()
                self.user_prompt_params.append(temp_model.from_map(k1))

        self.user_query_params = []
        if m.get('userQueryParams') is not None:
            for k1 in m.get('userQueryParams'):
                temp_model = main_models.UpdateMmAppAndBindingRequestModelConfigUserQueryParams()
                self.user_query_params.append(temp_model.from_map(k1))

        return self

class UpdateMmAppAndBindingRequestModelConfigUserQueryParams(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateMmAppAndBindingRequestModelConfigUserPromptParams(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateMmAppAndBindingRequestMemoryConfig(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.UpdateMmAppAndBindingRequestMemoryConfigAttributes] = None,
        desc: str = None,
        name: str = None,
    ):
        self.attributes = attributes
        self.desc = desc
        self.name = name

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.UpdateMmAppAndBindingRequestMemoryConfigAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateMmAppAndBindingRequestMemoryConfigAttributes(DaraModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
    ):
        self.desc = desc
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateMmAppAndBindingRequestConversationConfig(DaraModel):
    def __init__(
        self,
        asr_model: str = None,
        open_asr: bool = None,
        open_tts: bool = None,
        stop_or_reject_flag: bool = None,
        tts_model: str = None,
    ):
        self.asr_model = asr_model
        self.open_asr = open_asr
        self.open_tts = open_tts
        self.stop_or_reject_flag = stop_or_reject_flag
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

        if self.stop_or_reject_flag is not None:
            result['StopOrRejectFlag'] = self.stop_or_reject_flag

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

        if m.get('StopOrRejectFlag') is not None:
            self.stop_or_reject_flag = m.get('StopOrRejectFlag')

        if m.get('TtsModel') is not None:
            self.tts_model = m.get('TtsModel')

        return self

class UpdateMmAppAndBindingRequestBindingConfig(DaraModel):
    def __init__(
        self,
        agents: List[main_models.UpdateMmAppAndBindingRequestBindingConfigAgents] = None,
        commands: List[main_models.UpdateMmAppAndBindingRequestBindingConfigCommands] = None,
        mcps: List[main_models.UpdateMmAppAndBindingRequestBindingConfigMcps] = None,
        plugins: List[main_models.UpdateMmAppAndBindingRequestBindingConfigPlugins] = None,
        rag_config: main_models.UpdateMmAppAndBindingRequestBindingConfigRagConfig = None,
    ):
        self.agents = agents
        self.commands = commands
        self.mcps = mcps
        self.plugins = plugins
        self.rag_config = rag_config

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()
        if self.mcps:
            for v1 in self.mcps:
                 if v1:
                    v1.validate()
        if self.plugins:
            for v1 in self.plugins:
                 if v1:
                    v1.validate()
        if self.rag_config:
            self.rag_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['Agents'].append(k1.to_map() if k1 else None)

        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        result['Mcps'] = []
        if self.mcps is not None:
            for k1 in self.mcps:
                result['Mcps'].append(k1.to_map() if k1 else None)

        result['Plugins'] = []
        if self.plugins is not None:
            for k1 in self.plugins:
                result['Plugins'].append(k1.to_map() if k1 else None)

        if self.rag_config is not None:
            result['RagConfig'] = self.rag_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('Agents') is not None:
            for k1 in m.get('Agents'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigAgents()
                self.agents.append(temp_model.from_map(k1))

        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigCommands()
                self.commands.append(temp_model.from_map(k1))

        self.mcps = []
        if m.get('Mcps') is not None:
            for k1 in m.get('Mcps'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigMcps()
                self.mcps.append(temp_model.from_map(k1))

        self.plugins = []
        if m.get('Plugins') is not None:
            for k1 in m.get('Plugins'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigPlugins()
                self.plugins.append(temp_model.from_map(k1))

        if m.get('RagConfig') is not None:
            temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        return self

class UpdateMmAppAndBindingRequestBindingConfigRagConfig(DaraModel):
    def __init__(
        self,
        enable_search: bool = None,
        knowledge_base_code_list: List[str] = None,
        prompt_strategy: str = None,
        rank_weights: Dict[str, float] = None,
        retrieve_max_length: int = None,
        top_k: int = None,
    ):
        self.enable_search = enable_search
        self.knowledge_base_code_list = knowledge_base_code_list
        self.prompt_strategy = prompt_strategy
        self.rank_weights = rank_weights
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_search is not None:
            result['EnableSearch'] = self.enable_search

        if self.knowledge_base_code_list is not None:
            result['KnowledgeBaseCodeList'] = self.knowledge_base_code_list

        if self.prompt_strategy is not None:
            result['PromptStrategy'] = self.prompt_strategy

        if self.rank_weights is not None:
            result['RankWeights'] = self.rank_weights

        if self.retrieve_max_length is not None:
            result['RetrieveMaxLength'] = self.retrieve_max_length

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSearch') is not None:
            self.enable_search = m.get('EnableSearch')

        if m.get('KnowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('KnowledgeBaseCodeList')

        if m.get('PromptStrategy') is not None:
            self.prompt_strategy = m.get('PromptStrategy')

        if m.get('RankWeights') is not None:
            self.rank_weights = m.get('RankWeights')

        if m.get('RetrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('RetrieveMaxLength')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

class UpdateMmAppAndBindingRequestBindingConfigPlugins(DaraModel):
    def __init__(
        self,
        plugin_code: str = None,
        plugin_name: str = None,
        plugin_type: str = None,
    ):
        self.plugin_code = plugin_code
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.plugin_code is not None:
            result['PluginCode'] = self.plugin_code

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginCode') is not None:
            self.plugin_code = m.get('PluginCode')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        return self

class UpdateMmAppAndBindingRequestBindingConfigMcps(DaraModel):
    def __init__(
        self,
        code: str = None,
        tool_list: List[str] = None,
        type: str = None,
    ):
        self.code = code
        self.tool_list = tool_list
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.tool_list is not None:
            result['ToolList'] = self.tool_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ToolList') is not None:
            self.tool_list = m.get('ToolList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateMmAppAndBindingRequestBindingConfigCommands(DaraModel):
    def __init__(
        self,
        domain_code: str = None,
        domain_name: str = None,
        tools: List[main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsTools] = None,
        type: str = None,
    ):
        self.domain_code = domain_code
        self.domain_name = domain_name
        self.tools = tools
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

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

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

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsTools()
                self.tools.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateMmAppAndBindingRequestBindingConfigCommandsTools(DaraModel):
    def __init__(
        self,
        reply_mode: str = None,
        tool_description: str = None,
        tool_examples: List[main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolExamples] = None,
        tool_id: str = None,
        tool_name: str = None,
        tool_params: List[main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolParams] = None,
    ):
        self.reply_mode = reply_mode
        self.tool_description = tool_description
        self.tool_examples = tool_examples
        self.tool_id = tool_id
        self.tool_name = tool_name
        self.tool_params = tool_params

    def validate(self):
        if self.tool_examples:
            for v1 in self.tool_examples:
                 if v1:
                    v1.validate()
        if self.tool_params:
            for v1 in self.tool_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reply_mode is not None:
            result['ReplyMode'] = self.reply_mode

        if self.tool_description is not None:
            result['ToolDescription'] = self.tool_description

        result['ToolExamples'] = []
        if self.tool_examples is not None:
            for k1 in self.tool_examples:
                result['ToolExamples'].append(k1.to_map() if k1 else None)

        if self.tool_id is not None:
            result['ToolId'] = self.tool_id

        if self.tool_name is not None:
            result['ToolName'] = self.tool_name

        result['ToolParams'] = []
        if self.tool_params is not None:
            for k1 in self.tool_params:
                result['ToolParams'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplyMode') is not None:
            self.reply_mode = m.get('ReplyMode')

        if m.get('ToolDescription') is not None:
            self.tool_description = m.get('ToolDescription')

        self.tool_examples = []
        if m.get('ToolExamples') is not None:
            for k1 in m.get('ToolExamples'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolExamples()
                self.tool_examples.append(temp_model.from_map(k1))

        if m.get('ToolId') is not None:
            self.tool_id = m.get('ToolId')

        if m.get('ToolName') is not None:
            self.tool_name = m.get('ToolName')

        self.tool_params = []
        if m.get('ToolParams') is not None:
            for k1 in m.get('ToolParams'):
                temp_model = main_models.UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolParams()
                self.tool_params.append(temp_model.from_map(k1))

        return self

class UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolParams(DaraModel):
    def __init__(
        self,
        param_desc: str = None,
        param_example: str = None,
        param_name: str = None,
        param_type: str = None,
        required: bool = None,
    ):
        self.param_desc = param_desc
        self.param_example = param_example
        self.param_name = param_name
        self.param_type = param_type
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_desc is not None:
            result['ParamDesc'] = self.param_desc

        if self.param_example is not None:
            result['ParamExample'] = self.param_example

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamDesc') is not None:
            self.param_desc = m.get('ParamDesc')

        if m.get('ParamExample') is not None:
            self.param_example = m.get('ParamExample')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

class UpdateMmAppAndBindingRequestBindingConfigCommandsToolsToolExamples(DaraModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        query: str = None,
    ):
        self.parameters = parameters
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

class UpdateMmAppAndBindingRequestBindingConfigAgents(DaraModel):
    def __init__(
        self,
        agent_code: str = None,
        agent_name: str = None,
        agent_type: str = None,
        central_config: Dict[str, Any] = None,
        description: str = None,
        intent_few_shot_config: Dict[str, List[main_models.BindingConfigAgentsIntentFewShotConfigValue]] = None,
        own_config: Dict[str, Any] = None,
    ):
        self.agent_code = agent_code
        self.agent_name = agent_name
        self.agent_type = agent_type
        self.central_config = central_config
        self.description = description
        self.intent_few_shot_config = intent_few_shot_config
        self.own_config = own_config

    def validate(self):
        if self.intent_few_shot_config:
            for v1 in self.intent_few_shot_config.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_code is not None:
            result['AgentCode'] = self.agent_code

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.central_config is not None:
            result['CentralConfig'] = self.central_config

        if self.description is not None:
            result['Description'] = self.description

        result['IntentFewShotConfig'] = {}
        if self.intent_few_shot_config is not None:
            for k1, v1 in self.intent_few_shot_config.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['IntentFewShotConfig'][k1] = l1

        if self.own_config is not None:
            result['OwnConfig'] = self.own_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCode') is not None:
            self.agent_code = m.get('AgentCode')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CentralConfig') is not None:
            self.central_config = m.get('CentralConfig')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.intent_few_shot_config = {}
        if m.get('IntentFewShotConfig') is not None:
            for k1, v1 in m.get('IntentFewShotConfig').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.BindingConfigAgentsIntentFewShotConfigValue()
                    l1.append(temp_model.from_map(k2))
                self.intent_few_shot_config[k1] = l1

        if m.get('OwnConfig') is not None:
            self.own_config = m.get('OwnConfig')

        return self

