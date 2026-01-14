# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class CreateAndPulishAgentRequest(DaraModel):
    def __init__(
        self,
        application_config: main_models.CreateAndPulishAgentRequestApplicationConfig = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
        sample_library: main_models.CreateAndPulishAgentRequestSampleLibrary = None,
    ):
        self.application_config = application_config
        self.instructions = instructions
        self.model_id = model_id
        self.name = name
        self.sample_library = sample_library

    def validate(self):
        if self.application_config:
            self.application_config.validate()
        if self.sample_library:
            self.sample_library.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()

        if self.instructions is not None:
            result['instructions'] = self.instructions

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.name is not None:
            result['name'] = self.name

        if self.sample_library is not None:
            result['sampleLibrary'] = self.sample_library.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfig()
            self.application_config = temp_model.from_map(m.get('applicationConfig'))

        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sampleLibrary') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestSampleLibrary()
            self.sample_library = temp_model.from_map(m.get('sampleLibrary'))

        return self

class CreateAndPulishAgentRequestSampleLibrary(DaraModel):
    def __init__(
        self,
        enable_sample: bool = None,
        sample_library_id_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_sample = enable_sample
        self.sample_library_id_list = sample_library_id_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_sample is not None:
            result['enableSample'] = self.enable_sample

        if self.sample_library_id_list is not None:
            result['sampleLibraryIdList'] = self.sample_library_id_list

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableSample') is not None:
            self.enable_sample = m.get('enableSample')

        if m.get('sampleLibraryIdList') is not None:
            self.sample_library_id_list = m.get('sampleLibraryIdList')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class CreateAndPulishAgentRequestApplicationConfig(DaraModel):
    def __init__(
        self,
        history_config: main_models.CreateAndPulishAgentRequestApplicationConfigHistoryConfig = None,
        long_term_memory: main_models.CreateAndPulishAgentRequestApplicationConfigLongTermMemory = None,
        parameters: main_models.CreateAndPulishAgentRequestApplicationConfigParameters = None,
        rag_config: main_models.CreateAndPulishAgentRequestApplicationConfigRagConfig = None,
        security_config: main_models.CreateAndPulishAgentRequestApplicationConfigSecurityConfig = None,
        tools: List[main_models.CreateAndPulishAgentRequestApplicationConfigTools] = None,
        work_flows: List[main_models.CreateAndPulishAgentRequestApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security_config = security_config
        self.tools = tools
        self.work_flows = work_flows

    def validate(self):
        if self.history_config:
            self.history_config.validate()
        if self.long_term_memory:
            self.long_term_memory.validate()
        if self.parameters:
            self.parameters.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.security_config:
            self.security_config.validate()
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()
        if self.work_flows:
            for v1 in self.work_flows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.history_config is not None:
            result['historyConfig'] = self.history_config.to_map()

        if self.long_term_memory is not None:
            result['longTermMemory'] = self.long_term_memory.to_map()

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.rag_config is not None:
            result['ragConfig'] = self.rag_config.to_map()

        if self.security_config is not None:
            result['securityConfig'] = self.security_config.to_map()

        result['tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['tools'].append(k1.to_map() if k1 else None)

        result['workFlows'] = []
        if self.work_flows is not None:
            for k1 in self.work_flows:
                result['workFlows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('historyConfig') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m.get('historyConfig'))

        if m.get('longTermMemory') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m.get('longTermMemory'))

        if m.get('parameters') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('ragConfig') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m.get('ragConfig'))

        if m.get('securityConfig') is not None:
            temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigSecurityConfig()
            self.security_config = temp_model.from_map(m.get('securityConfig'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigTools()
                self.tools.append(temp_model.from_map(k1))

        self.work_flows = []
        if m.get('workFlows') is not None:
            for k1 in m.get('workFlows'):
                temp_model = main_models.CreateAndPulishAgentRequestApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k1))

        return self

class CreateAndPulishAgentRequestApplicationConfigWorkFlows(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateAndPulishAgentRequestApplicationConfigTools(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateAndPulishAgentRequestApplicationConfigSecurityConfig(DaraModel):
    def __init__(
        self,
        processing_strategy: str = None,
    ):
        self.processing_strategy = processing_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processing_strategy is not None:
            result['processingStrategy'] = self.processing_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('processingStrategy') is not None:
            self.processing_strategy = m.get('processingStrategy')

        return self

class CreateAndPulishAgentRequestApplicationConfigRagConfig(DaraModel):
    def __init__(
        self,
        answer_scope: str = None,
        enable_citation: bool = None,
        enable_search: bool = None,
        enable_web_search: bool = None,
        fixed_reply_detail: str = None,
        knowledge_base_code_list: List[str] = None,
        prompt_strategy: str = None,
        rag_reject_type: str = None,
        reject_filter_prompt: str = None,
        reject_filter_type: str = None,
        retrieve_max_length: int = None,
        top_k: int = None,
    ):
        self.answer_scope = answer_scope
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.enable_web_search = enable_web_search
        self.fixed_reply_detail = fixed_reply_detail
        self.knowledge_base_code_list = knowledge_base_code_list
        self.prompt_strategy = prompt_strategy
        self.rag_reject_type = rag_reject_type
        self.reject_filter_prompt = reject_filter_prompt
        self.reject_filter_type = reject_filter_type
        self.retrieve_max_length = retrieve_max_length
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer_scope is not None:
            result['answerScope'] = self.answer_scope

        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation

        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

        if self.fixed_reply_detail is not None:
            result['fixedReplyDetail'] = self.fixed_reply_detail

        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list

        if self.prompt_strategy is not None:
            result['promptStrategy'] = self.prompt_strategy

        if self.rag_reject_type is not None:
            result['ragRejectType'] = self.rag_reject_type

        if self.reject_filter_prompt is not None:
            result['rejectFilterPrompt'] = self.reject_filter_prompt

        if self.reject_filter_type is not None:
            result['rejectFilterType'] = self.reject_filter_type

        if self.retrieve_max_length is not None:
            result['retrieveMaxLength'] = self.retrieve_max_length

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answerScope') is not None:
            self.answer_scope = m.get('answerScope')

        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')

        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

        if m.get('fixedReplyDetail') is not None:
            self.fixed_reply_detail = m.get('fixedReplyDetail')

        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')

        if m.get('promptStrategy') is not None:
            self.prompt_strategy = m.get('promptStrategy')

        if m.get('ragRejectType') is not None:
            self.rag_reject_type = m.get('ragRejectType')

        if m.get('rejectFilterPrompt') is not None:
            self.reject_filter_prompt = m.get('rejectFilterPrompt')

        if m.get('rejectFilterType') is not None:
            self.reject_filter_type = m.get('rejectFilterType')

        if m.get('retrieveMaxLength') is not None:
            self.retrieve_max_length = m.get('retrieveMaxLength')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class CreateAndPulishAgentRequestApplicationConfigParameters(DaraModel):
    def __init__(
        self,
        dialog_round: int = None,
        enable_thinking: bool = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
        self.enable_thinking = enable_thinking
        self.max_tokens = max_tokens
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialog_round is not None:
            result['dialogRound'] = self.dialog_round

        if self.enable_thinking is not None:
            result['enable_thinking'] = self.enable_thinking

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.temperature is not None:
            result['temperature'] = self.temperature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')

        if m.get('enable_thinking') is not None:
            self.enable_thinking = m.get('enable_thinking')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        return self

class CreateAndPulishAgentRequestApplicationConfigLongTermMemory(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

class CreateAndPulishAgentRequestApplicationConfigHistoryConfig(DaraModel):
    def __init__(
        self,
        enable_adb_record: bool = None,
        enable_record: bool = None,
        instance_id: str = None,
        region: str = None,
        store_code: str = None,
    ):
        self.enable_adb_record = enable_adb_record
        self.enable_record = enable_record
        self.instance_id = instance_id
        self.region = region
        self.store_code = store_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_adb_record is not None:
            result['enableAdbRecord'] = self.enable_adb_record

        if self.enable_record is not None:
            result['enableRecord'] = self.enable_record

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region is not None:
            result['region'] = self.region

        if self.store_code is not None:
            result['storeCode'] = self.store_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableAdbRecord') is not None:
            self.enable_adb_record = m.get('enableAdbRecord')

        if m.get('enableRecord') is not None:
            self.enable_record = m.get('enableRecord')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('storeCode') is not None:
            self.store_code = m.get('storeCode')

        return self

