# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class GetApplicationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetApplicationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        concurrency: int = None,
        created_time: int = None,
        description: str = None,
        draft_version: main_models.GetApplicationResponseBodyDataDraftVersion = None,
        name: str = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        published_version: main_models.GetApplicationResponseBodyDataPublishedVersion = None,
        updated_time: int = None,
    ):
        self.application_id = application_id
        self.concurrency = concurrency
        self.created_time = created_time
        self.description = description
        self.draft_version = draft_version
        self.name = name
        self.nlu_access_type = nlu_access_type
        self.nlu_engine = nlu_engine
        self.published_version = published_version
        self.updated_time = updated_time

    def validate(self):
        if self.draft_version:
            self.draft_version.validate()
        if self.published_version:
            self.published_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.published_version is not None:
            result['PublishedVersion'] = self.published_version.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DraftVersion') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersion()
            self.draft_version = temp_model.from_map(m.get('DraftVersion'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('PublishedVersion') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersion()
            self.published_version = temp_model.from_map(m.get('PublishedVersion'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class GetApplicationResponseBodyDataPublishedVersion(DaraModel):
    def __init__(
        self,
        interaction_config: main_models.GetApplicationResponseBodyDataPublishedVersionInteractionConfig = None,
        rag_config: main_models.GetApplicationResponseBodyDataPublishedVersionRagConfig = None,
        script_profile: main_models.GetApplicationResponseBodyDataPublishedVersionScriptProfile = None,
        synthesizer_config: main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfig = None,
        tool_config: main_models.GetApplicationResponseBodyDataPublishedVersionToolConfig = None,
        transcriber_config: main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfig = None,
        version_id: str = None,
    ):
        self.interaction_config = interaction_config
        self.rag_config = rag_config
        self.script_profile = script_profile
        self.synthesizer_config = synthesizer_config
        self.tool_config = tool_config
        self.transcriber_config = transcriber_config
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.script_profile:
            self.script_profile.validate()
        if self.synthesizer_config:
            self.synthesizer_config.validate()
        if self.tool_config:
            self.tool_config.validate()
        if self.transcriber_config:
            self.transcriber_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

        if self.rag_config is not None:
            result['RagConfig'] = self.rag_config.to_map()

        if self.script_profile is not None:
            result['ScriptProfile'] = self.script_profile.to_map()

        if self.synthesizer_config is not None:
            result['SynthesizerConfig'] = self.synthesizer_config.to_map()

        if self.tool_config is not None:
            result['ToolConfig'] = self.tool_config.to_map()

        if self.transcriber_config is not None:
            result['TranscriberConfig'] = self.transcriber_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InteractionConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        if m.get('RagConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('ToolConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionToolConfig()
            self.tool_config = temp_model.from_map(m.get('ToolConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetApplicationResponseBodyDataPublishedVersionTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: int = None,
        vocabulary_id: str = None,
    ):
        self.correction_rules = correction_rules
        self.customization_id = customization_id
        self.end_silence_timeout = end_silence_timeout
        self.model = model
        self.nls_access_profile = nls_access_profile
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.speech_noise_threshold = speech_noise_threshold
        self.vocabulary_id = vocabulary_id

    def validate(self):
        if self.correction_rules:
            for v1 in self.correction_rules:
                 if v1:
                    v1.validate()
        if self.nls_access_profile:
            self.nls_access_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CorrectionRules'] = []
        if self.correction_rules is not None:
            for k1 in self.correction_rules:
                result['CorrectionRules'].append(k1.to_map() if k1 else None)

        if self.customization_id is not None:
            result['CustomizationId'] = self.customization_id

        if self.end_silence_timeout is not None:
            result['EndSilenceTimeout'] = self.end_silence_timeout

        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_profile is not None:
            result['NlsAccessProfile'] = self.nls_access_profile.to_map()

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.speech_noise_threshold is not None:
            result['SpeechNoiseThreshold'] = self.speech_noise_threshold

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.correction_rules = []
        if m.get('CorrectionRules') is not None:
            for k1 in m.get('CorrectionRules'):
                temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile()
            self.nls_access_profile = temp_model.from_map(m.get('NlsAccessProfile'))

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('SpeechNoiseThreshold') is not None:
            self.speech_noise_threshold = m.get('SpeechNoiseThreshold')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        return self

class GetApplicationResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        self.access_profile_id = access_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        return self

class GetApplicationResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        self.pattern = pattern
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        return self

class GetApplicationResponseBodyDataPublishedVersionToolConfig(DaraModel):
    def __init__(
        self,
        mcp_servers: List[main_models.GetApplicationResponseBodyDataPublishedVersionToolConfigMcpServers] = None,
    ):
        self.mcp_servers = mcp_servers

    def validate(self):
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['McpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['McpServers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mcp_servers = []
        if m.get('McpServers') is not None:
            for k1 in m.get('McpServers'):
                temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionToolConfigMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        return self

class GetApplicationResponseBodyDataPublishedVersionToolConfigMcpServers(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        name: str = None,
        sse_endpoint: str = None,
    ):
        self.base_url = base_url
        self.name = name
        self.sse_endpoint = sse_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.name is not None:
            result['Name'] = self.name

        if self.sse_endpoint is not None:
            result['SseEndpoint'] = self.sse_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SseEndpoint') is not None:
            self.sse_endpoint = m.get('SseEndpoint')

        return self

class GetApplicationResponseBodyDataPublishedVersionSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigPronRules] = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.model = model
        self.nls_access_profile = nls_access_profile
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.pitch_rate = pitch_rate
        self.pron_rules = pron_rules
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        if self.nls_access_profile:
            self.nls_access_profile.validate()
        if self.pron_rules:
            for v1 in self.pron_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_profile is not None:
            result['NlsAccessProfile'] = self.nls_access_profile.to_map()

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        result['PronRules'] = []
        if self.pron_rules is not None:
            for k1 in self.pron_rules:
                result['PronRules'].append(k1.to_map() if k1 else None)

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile()
            self.nls_access_profile = temp_model.from_map(m.get('NlsAccessProfile'))

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        self.pron_rules = []
        if m.get('PronRules') is not None:
            for k1 in m.get('PronRules'):
                temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        self.pattern = pattern
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        return self

class GetApplicationResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        self.access_profile_id = access_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        return self

class GetApplicationResponseBodyDataPublishedVersionScriptProfile(DaraModel):
    def __init__(
        self,
        agent_profile: main_models.GetApplicationResponseBodyDataPublishedVersionScriptProfileAgentProfile = None,
        model: str = None,
        temperature: str = None,
        top_p: str = None,
    ):
        self.agent_profile = agent_profile
        self.model = model
        self.temperature = temperature
        self.top_p = top_p

    def validate(self):
        if self.agent_profile:
            self.agent_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile is not None:
            result['AgentProfile'] = self.agent_profile.to_map()

        if self.model is not None:
            result['Model'] = self.model

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class GetApplicationResponseBodyDataPublishedVersionScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        agent_profile_id: str = None,
        description: str = None,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        self.agent_profile_id = agent_profile_id
        self.description = description
        self.prompts_json = prompts_json
        self.script_profile_template_id = script_profile_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_id is not None:
            result['AgentProfileId'] = self.agent_profile_id

        if self.description is not None:
            result['Description'] = self.description

        if self.prompts_json is not None:
            result['PromptsJson'] = self.prompts_json

        if self.script_profile_template_id is not None:
            result['ScriptProfileTemplateId'] = self.script_profile_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileId') is not None:
            self.agent_profile_id = m.get('AgentProfileId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PromptsJson') is not None:
            self.prompts_json = m.get('PromptsJson')

        if m.get('ScriptProfileTemplateId') is not None:
            self.script_profile_template_id = m.get('ScriptProfileTemplateId')

        return self

class GetApplicationResponseBodyDataPublishedVersionRagConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        knowledge_base_ids: List[str] = None,
        max_content_length: int = None,
        rag_engine: str = None,
        top_n: int = None,
    ):
        self.enabled = enabled
        self.knowledge_base_ids = knowledge_base_ids
        self.max_content_length = max_content_length
        self.rag_engine = rag_engine
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.knowledge_base_ids is not None:
            result['KnowledgeBaseIds'] = self.knowledge_base_ids

        if self.max_content_length is not None:
            result['MaxContentLength'] = self.max_content_length

        if self.rag_engine is not None:
            result['RagEngine'] = self.rag_engine

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('KnowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('KnowledgeBaseIds')

        if m.get('MaxContentLength') is not None:
            self.max_content_length = m.get('MaxContentLength')

        if m.get('RagEngine') is not None:
            self.rag_engine = m.get('RagEngine')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

class GetApplicationResponseBodyDataPublishedVersionInteractionConfig(DaraModel):
    def __init__(
        self,
        silence_detection_config: main_models.GetApplicationResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig = None,
    ):
        self.silence_detection_config = silence_detection_config

    def validate(self):
        if self.silence_detection_config:
            self.silence_detection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.silence_detection_config is not None:
            result['SilenceDetectionConfig'] = self.silence_detection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class GetApplicationResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        timeout: int = None,
    ):
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetApplicationResponseBodyDataDraftVersion(DaraModel):
    def __init__(
        self,
        interaction_config: main_models.GetApplicationResponseBodyDataDraftVersionInteractionConfig = None,
        rag_config: main_models.GetApplicationResponseBodyDataDraftVersionRagConfig = None,
        script_profile: main_models.GetApplicationResponseBodyDataDraftVersionScriptProfile = None,
        synthesizer_config: main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfig = None,
        tool_config: main_models.GetApplicationResponseBodyDataDraftVersionToolConfig = None,
        transcriber_config: main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfig = None,
        version_id: str = None,
    ):
        self.interaction_config = interaction_config
        self.rag_config = rag_config
        self.script_profile = script_profile
        self.synthesizer_config = synthesizer_config
        self.tool_config = tool_config
        self.transcriber_config = transcriber_config
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
        if self.rag_config:
            self.rag_config.validate()
        if self.script_profile:
            self.script_profile.validate()
        if self.synthesizer_config:
            self.synthesizer_config.validate()
        if self.tool_config:
            self.tool_config.validate()
        if self.transcriber_config:
            self.transcriber_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

        if self.rag_config is not None:
            result['RagConfig'] = self.rag_config.to_map()

        if self.script_profile is not None:
            result['ScriptProfile'] = self.script_profile.to_map()

        if self.synthesizer_config is not None:
            result['SynthesizerConfig'] = self.synthesizer_config.to_map()

        if self.tool_config is not None:
            result['ToolConfig'] = self.tool_config.to_map()

        if self.transcriber_config is not None:
            result['TranscriberConfig'] = self.transcriber_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InteractionConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        if m.get('RagConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('ToolConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionToolConfig()
            self.tool_config = temp_model.from_map(m.get('ToolConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetApplicationResponseBodyDataDraftVersionTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: int = None,
        vocabulary_id: str = None,
    ):
        self.correction_rules = correction_rules
        self.customization_id = customization_id
        self.end_silence_timeout = end_silence_timeout
        self.model = model
        self.nls_access_profile = nls_access_profile
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.speech_noise_threshold = speech_noise_threshold
        self.vocabulary_id = vocabulary_id

    def validate(self):
        if self.correction_rules:
            for v1 in self.correction_rules:
                 if v1:
                    v1.validate()
        if self.nls_access_profile:
            self.nls_access_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CorrectionRules'] = []
        if self.correction_rules is not None:
            for k1 in self.correction_rules:
                result['CorrectionRules'].append(k1.to_map() if k1 else None)

        if self.customization_id is not None:
            result['CustomizationId'] = self.customization_id

        if self.end_silence_timeout is not None:
            result['EndSilenceTimeout'] = self.end_silence_timeout

        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_profile is not None:
            result['NlsAccessProfile'] = self.nls_access_profile.to_map()

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.speech_noise_threshold is not None:
            result['SpeechNoiseThreshold'] = self.speech_noise_threshold

        if self.vocabulary_id is not None:
            result['VocabularyId'] = self.vocabulary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.correction_rules = []
        if m.get('CorrectionRules') is not None:
            for k1 in m.get('CorrectionRules'):
                temp_model = main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile()
            self.nls_access_profile = temp_model.from_map(m.get('NlsAccessProfile'))

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('SpeechNoiseThreshold') is not None:
            self.speech_noise_threshold = m.get('SpeechNoiseThreshold')

        if m.get('VocabularyId') is not None:
            self.vocabulary_id = m.get('VocabularyId')

        return self

class GetApplicationResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        self.access_profile_id = access_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        return self

class GetApplicationResponseBodyDataDraftVersionTranscriberConfigCorrectionRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        self.pattern = pattern
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        return self

class GetApplicationResponseBodyDataDraftVersionToolConfig(DaraModel):
    def __init__(
        self,
        mcp_servers: List[main_models.GetApplicationResponseBodyDataDraftVersionToolConfigMcpServers] = None,
    ):
        self.mcp_servers = mcp_servers

    def validate(self):
        if self.mcp_servers:
            for v1 in self.mcp_servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['McpServers'] = []
        if self.mcp_servers is not None:
            for k1 in self.mcp_servers:
                result['McpServers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mcp_servers = []
        if m.get('McpServers') is not None:
            for k1 in m.get('McpServers'):
                temp_model = main_models.GetApplicationResponseBodyDataDraftVersionToolConfigMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        return self

class GetApplicationResponseBodyDataDraftVersionToolConfigMcpServers(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        name: str = None,
        sse_endpoint: str = None,
    ):
        self.base_url = base_url
        self.name = name
        self.sse_endpoint = sse_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.name is not None:
            result['Name'] = self.name

        if self.sse_endpoint is not None:
            result['SseEndpoint'] = self.sse_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SseEndpoint') is not None:
            self.sse_endpoint = m.get('SseEndpoint')

        return self

class GetApplicationResponseBodyDataDraftVersionSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfigPronRules] = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.model = model
        self.nls_access_profile = nls_access_profile
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.pitch_rate = pitch_rate
        self.pron_rules = pron_rules
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        if self.nls_access_profile:
            self.nls_access_profile.validate()
        if self.pron_rules:
            for v1 in self.pron_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['Model'] = self.model

        if self.nls_access_profile is not None:
            result['NlsAccessProfile'] = self.nls_access_profile.to_map()

        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        result['PronRules'] = []
        if self.pron_rules is not None:
            for k1 in self.pron_rules:
                result['PronRules'].append(k1.to_map() if k1 else None)

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile()
            self.nls_access_profile = temp_model.from_map(m.get('NlsAccessProfile'))

        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        self.pron_rules = []
        if m.get('PronRules') is not None:
            for k1 in m.get('PronRules'):
                temp_model = main_models.GetApplicationResponseBodyDataDraftVersionSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetApplicationResponseBodyDataDraftVersionSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        self.pattern = pattern
        self.replacement = replacement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.replacement is not None:
            result['Replacement'] = self.replacement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Replacement') is not None:
            self.replacement = m.get('Replacement')

        return self

class GetApplicationResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        self.access_profile_id = access_profile_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        return self

class GetApplicationResponseBodyDataDraftVersionScriptProfile(DaraModel):
    def __init__(
        self,
        agent_profile: main_models.GetApplicationResponseBodyDataDraftVersionScriptProfileAgentProfile = None,
        model: str = None,
        temperature: str = None,
        top_p: str = None,
    ):
        self.agent_profile = agent_profile
        self.model = model
        self.temperature = temperature
        self.top_p = top_p

    def validate(self):
        if self.agent_profile:
            self.agent_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile is not None:
            result['AgentProfile'] = self.agent_profile.to_map()

        if self.model is not None:
            result['Model'] = self.model

        if self.temperature is not None:
            result['Temperature'] = self.temperature

        if self.top_p is not None:
            result['TopP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfile') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')

        if m.get('TopP') is not None:
            self.top_p = m.get('TopP')

        return self

class GetApplicationResponseBodyDataDraftVersionScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        agent_profile_id: str = None,
        description: str = None,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        self.agent_profile_id = agent_profile_id
        self.description = description
        self.prompts_json = prompts_json
        self.script_profile_template_id = script_profile_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_id is not None:
            result['AgentProfileId'] = self.agent_profile_id

        if self.description is not None:
            result['Description'] = self.description

        if self.prompts_json is not None:
            result['PromptsJson'] = self.prompts_json

        if self.script_profile_template_id is not None:
            result['ScriptProfileTemplateId'] = self.script_profile_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileId') is not None:
            self.agent_profile_id = m.get('AgentProfileId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PromptsJson') is not None:
            self.prompts_json = m.get('PromptsJson')

        if m.get('ScriptProfileTemplateId') is not None:
            self.script_profile_template_id = m.get('ScriptProfileTemplateId')

        return self

class GetApplicationResponseBodyDataDraftVersionRagConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        knowledge_base_ids: List[str] = None,
        max_content_length: int = None,
        rag_engine: str = None,
        top_n: int = None,
    ):
        self.enabled = enabled
        self.knowledge_base_ids = knowledge_base_ids
        self.max_content_length = max_content_length
        self.rag_engine = rag_engine
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.knowledge_base_ids is not None:
            result['KnowledgeBaseIds'] = self.knowledge_base_ids

        if self.max_content_length is not None:
            result['MaxContentLength'] = self.max_content_length

        if self.rag_engine is not None:
            result['RagEngine'] = self.rag_engine

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('KnowledgeBaseIds') is not None:
            self.knowledge_base_ids = m.get('KnowledgeBaseIds')

        if m.get('MaxContentLength') is not None:
            self.max_content_length = m.get('MaxContentLength')

        if m.get('RagEngine') is not None:
            self.rag_engine = m.get('RagEngine')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

class GetApplicationResponseBodyDataDraftVersionInteractionConfig(DaraModel):
    def __init__(
        self,
        silence_detection_config: main_models.GetApplicationResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig = None,
    ):
        self.silence_detection_config = silence_detection_config

    def validate(self):
        if self.silence_detection_config:
            self.silence_detection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.silence_detection_config is not None:
            result['SilenceDetectionConfig'] = self.silence_detection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.GetApplicationResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class GetApplicationResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        timeout: int = None,
    ):
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

