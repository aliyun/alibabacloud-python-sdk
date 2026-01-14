# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class GetPublishedAgentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPublishedAgentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetPublishedAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        application_config: main_models.GetPublishedAgentResponseBodyDataApplicationConfig = None,
        code: str = None,
        instructions: str = None,
        model_id: str = None,
        name: str = None,
    ):
        self.application_config = application_config
        self.code = code
        self.instructions = instructions
        self.model_id = model_id
        self.name = name

    def validate(self):
        if self.application_config:
            self.application_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_config is not None:
            result['applicationConfig'] = self.application_config.to_map()

        if self.code is not None:
            result['code'] = self.code

        if self.instructions is not None:
            result['instructions'] = self.instructions

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationConfig') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfig()
            self.application_config = temp_model.from_map(m.get('applicationConfig'))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instructions') is not None:
            self.instructions = m.get('instructions')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetPublishedAgentResponseBodyDataApplicationConfig(DaraModel):
    def __init__(
        self,
        history_config: main_models.GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig = None,
        long_term_memory: main_models.GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory = None,
        parameters: main_models.GetPublishedAgentResponseBodyDataApplicationConfigParameters = None,
        rag_config: main_models.GetPublishedAgentResponseBodyDataApplicationConfigRagConfig = None,
        security: main_models.GetPublishedAgentResponseBodyDataApplicationConfigSecurity = None,
        tools: List[main_models.GetPublishedAgentResponseBodyDataApplicationConfigTools] = None,
        work_flows: List[main_models.GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows] = None,
    ):
        self.history_config = history_config
        self.long_term_memory = long_term_memory
        self.parameters = parameters
        self.rag_config = rag_config
        self.security = security
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
        if self.security:
            self.security.validate()
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

        if self.security is not None:
            result['security'] = self.security.to_map()

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
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig()
            self.history_config = temp_model.from_map(m.get('historyConfig'))

        if m.get('longTermMemory') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory()
            self.long_term_memory = temp_model.from_map(m.get('longTermMemory'))

        if m.get('parameters') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('ragConfig') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigRagConfig()
            self.rag_config = temp_model.from_map(m.get('ragConfig'))

        if m.get('security') is not None:
            temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigSecurity()
            self.security = temp_model.from_map(m.get('security'))

        self.tools = []
        if m.get('tools') is not None:
            for k1 in m.get('tools'):
                temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigTools()
                self.tools.append(temp_model.from_map(k1))

        self.work_flows = []
        if m.get('workFlows') is not None:
            for k1 in m.get('workFlows'):
                temp_model = main_models.GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows()
                self.work_flows.append(temp_model.from_map(k1))

        return self

class GetPublishedAgentResponseBodyDataApplicationConfigWorkFlows(DaraModel):
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

class GetPublishedAgentResponseBodyDataApplicationConfigTools(DaraModel):
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

class GetPublishedAgentResponseBodyDataApplicationConfigSecurity(DaraModel):
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

class GetPublishedAgentResponseBodyDataApplicationConfigRagConfig(DaraModel):
    def __init__(
        self,
        enable_citation: bool = None,
        enable_search: bool = None,
        knowledge_base_code_list: List[str] = None,
        top_k: int = None,
    ):
        self.enable_citation = enable_citation
        self.enable_search = enable_search
        self.knowledge_base_code_list = knowledge_base_code_list
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_citation is not None:
            result['enableCitation'] = self.enable_citation

        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search

        if self.knowledge_base_code_list is not None:
            result['knowledgeBaseCodeList'] = self.knowledge_base_code_list

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableCitation') is not None:
            self.enable_citation = m.get('enableCitation')

        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')

        if m.get('knowledgeBaseCodeList') is not None:
            self.knowledge_base_code_list = m.get('knowledgeBaseCodeList')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class GetPublishedAgentResponseBodyDataApplicationConfigParameters(DaraModel):
    def __init__(
        self,
        dialog_round: int = None,
        max_tokens: int = None,
        temperature: float = None,
    ):
        self.dialog_round = dialog_round
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

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.temperature is not None:
            result['temperature'] = self.temperature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogRound') is not None:
            self.dialog_round = m.get('dialogRound')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        return self

class GetPublishedAgentResponseBodyDataApplicationConfigLongTermMemory(DaraModel):
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

class GetPublishedAgentResponseBodyDataApplicationConfigHistoryConfig(DaraModel):
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

