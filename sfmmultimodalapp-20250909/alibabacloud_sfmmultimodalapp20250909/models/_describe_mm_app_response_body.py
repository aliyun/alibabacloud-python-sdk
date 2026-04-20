# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class DescribeMmAppResponseBody(DaraModel):
    def __init__(
        self,
        app_config: main_models.DescribeMmAppResponseBodyAppConfig = None,
        app_id: str = None,
        app_name: str = None,
        binding_config: main_models.DescribeMmAppResponseBodyBindingConfig = None,
        conversation_config: main_models.DescribeMmAppResponseBodyConversationConfig = None,
        create_user_id: str = None,
        create_user_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        model_config: main_models.DescribeMmAppResponseBodyModelConfig = None,
        modify_user_id: str = None,
        modify_user_name: str = None,
        prompt: str = None,
        publish_version: int = None,
        request_id: str = None,
        status: str = None,
    ):
        self.app_config = app_config
        self.app_id = app_id
        self.app_name = app_name
        self.binding_config = binding_config
        self.conversation_config = conversation_config
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.model_config = model_config
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.prompt = prompt
        self.publish_version = publish_version
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.app_config:
            self.app_config.validate()
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
        if self.app_config is not None:
            result['AppConfig'] = self.app_config.to_map()

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.binding_config is not None:
            result['BindingConfig'] = self.binding_config.to_map()

        if self.conversation_config is not None:
            result['ConversationConfig'] = self.conversation_config.to_map()

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.publish_version is not None:
            result['PublishVersion'] = self.publish_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyAppConfig()
            self.app_config = temp_model.from_map(m.get('AppConfig'))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BindingConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyBindingConfig()
            self.binding_config = temp_model.from_map(m.get('BindingConfig'))

        if m.get('ConversationConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyConversationConfig()
            self.conversation_config = temp_model.from_map(m.get('ConversationConfig'))

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModelConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyModelConfig()
            self.model_config = temp_model.from_map(m.get('ModelConfig'))

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PublishVersion') is not None:
            self.publish_version = m.get('PublishVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMmAppResponseBodyModelConfig(DaraModel):
    def __init__(
        self,
        history_limit: int = None,
        model_type: str = None,
        open_memory: bool = None,
        open_web_search: bool = None,
        text_modal: str = None,
    ):
        self.history_limit = history_limit
        self.model_type = model_type
        self.open_memory = open_memory
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

        if self.open_memory is not None:
            result['OpenMemory'] = self.open_memory

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

        if m.get('OpenMemory') is not None:
            self.open_memory = m.get('OpenMemory')

        if m.get('OpenWebSearch') is not None:
            self.open_web_search = m.get('OpenWebSearch')

        if m.get('TextModal') is not None:
            self.text_modal = m.get('TextModal')

        return self

class DescribeMmAppResponseBodyConversationConfig(DaraModel):
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

class DescribeMmAppResponseBodyBindingConfig(DaraModel):
    def __init__(
        self,
        commands: List[main_models.DescribeMmAppResponseBodyBindingConfigCommands] = None,
        mcps: List[main_models.DescribeMmAppResponseBodyBindingConfigMcps] = None,
        rag_config: main_models.DescribeMmAppResponseBodyBindingConfigRagConfig = None,
    ):
        self.commands = commands
        self.mcps = mcps
        self.rag_config = rag_config

    def validate(self):
        if self.commands:
            for v1 in self.commands:
                 if v1:
                    v1.validate()
        if self.mcps:
            for v1 in self.mcps:
                 if v1:
                    v1.validate()
        if self.rag_config:
            self.rag_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Commands'] = []
        if self.commands is not None:
            for k1 in self.commands:
                result['Commands'].append(k1.to_map() if k1 else None)

        result['Mcps'] = []
        if self.mcps is not None:
            for k1 in self.mcps:
                result['Mcps'].append(k1.to_map() if k1 else None)

        if self.rag_config is not None:
            result['RagConfig'] = self.rag_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commands = []
        if m.get('Commands') is not None:
            for k1 in m.get('Commands'):
                temp_model = main_models.DescribeMmAppResponseBodyBindingConfigCommands()
                self.commands.append(temp_model.from_map(k1))

        self.mcps = []
        if m.get('Mcps') is not None:
            for k1 in m.get('Mcps'):
                temp_model = main_models.DescribeMmAppResponseBodyBindingConfigMcps()
                self.mcps.append(temp_model.from_map(k1))

        if m.get('RagConfig') is not None:
            temp_model = main_models.DescribeMmAppResponseBodyBindingConfigRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        return self

class DescribeMmAppResponseBodyBindingConfigRagConfig(DaraModel):
    def __init__(
        self,
        enable_search: str = None,
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

class DescribeMmAppResponseBodyBindingConfigMcps(DaraModel):
    def __init__(
        self,
        code: str = None,
        tool_list: List[str] = None,
    ):
        self.code = code
        self.tool_list = tool_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ToolList') is not None:
            self.tool_list = m.get('ToolList')

        return self

class DescribeMmAppResponseBodyBindingConfigCommands(DaraModel):
    def __init__(
        self,
        domain_code: str = None,
        tools: List[str] = None,
        type: str = None,
    ):
        self.domain_code = domain_code
        self.tools = tools
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.tools is not None:
            result['Tools'] = self.tools

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('Tools') is not None:
            self.tools = m.get('Tools')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeMmAppResponseBodyAppConfig(DaraModel):
    def __init__(
        self,
        enable_transition: bool = None,
    ):
        self.enable_transition = enable_transition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_transition is not None:
            result['EnableTransition'] = self.enable_transition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableTransition') is not None:
            self.enable_transition = m.get('EnableTransition')

        return self

