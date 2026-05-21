# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationVersionRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        business_unit_id: str = None,
        interaction_config: main_models.UpdateApplicationVersionRequestInteractionConfig = None,
        rag_config: main_models.UpdateApplicationVersionRequestRagConfig = None,
        script_profile: main_models.UpdateApplicationVersionRequestScriptProfile = None,
        synthesizer_config: main_models.UpdateApplicationVersionRequestSynthesizerConfig = None,
        tool_config: main_models.UpdateApplicationVersionRequestToolConfig = None,
        transcriber_config: main_models.UpdateApplicationVersionRequestTranscriberConfig = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.business_unit_id = business_unit_id
        self.interaction_config = interaction_config
        self.rag_config = rag_config
        # This parameter is required.
        self.script_profile = script_profile
        self.synthesizer_config = synthesizer_config
        self.tool_config = tool_config
        self.transcriber_config = transcriber_config
        # This parameter is required.
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

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
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('InteractionConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        if m.get('RagConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('ToolConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestToolConfig()
            self.tool_config = temp_model.from_map(m.get('ToolConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class UpdateApplicationVersionRequestTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.UpdateApplicationVersionRequestTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.UpdateApplicationVersionRequestTranscriberConfigNlsAccessProfile = None,
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
                temp_model = main_models.UpdateApplicationVersionRequestTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestTranscriberConfigNlsAccessProfile()
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

class UpdateApplicationVersionRequestTranscriberConfigNlsAccessProfile(DaraModel):
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

class UpdateApplicationVersionRequestTranscriberConfigCorrectionRules(DaraModel):
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

class UpdateApplicationVersionRequestToolConfig(DaraModel):
    def __init__(
        self,
        mcp_servers: List[main_models.UpdateApplicationVersionRequestToolConfigMcpServers] = None,
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
                temp_model = main_models.UpdateApplicationVersionRequestToolConfigMcpServers()
                self.mcp_servers.append(temp_model.from_map(k1))

        return self

class UpdateApplicationVersionRequestToolConfigMcpServers(DaraModel):
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

class UpdateApplicationVersionRequestSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.UpdateApplicationVersionRequestSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.UpdateApplicationVersionRequestSynthesizerConfigPronRules] = None,
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
            temp_model = main_models.UpdateApplicationVersionRequestSynthesizerConfigNlsAccessProfile()
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
                temp_model = main_models.UpdateApplicationVersionRequestSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class UpdateApplicationVersionRequestSynthesizerConfigPronRules(DaraModel):
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

class UpdateApplicationVersionRequestSynthesizerConfigNlsAccessProfile(DaraModel):
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

class UpdateApplicationVersionRequestScriptProfile(DaraModel):
    def __init__(
        self,
        agent_profile: main_models.UpdateApplicationVersionRequestScriptProfileAgentProfile = None,
        model: str = None,
    ):
        self.agent_profile = agent_profile
        self.model = model

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfile') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        return self

class UpdateApplicationVersionRequestScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        self.description = description
        self.name = name
        self.prompts_json = prompts_json
        self.script_profile_template_id = script_profile_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.prompts_json is not None:
            result['PromptsJson'] = self.prompts_json

        if self.script_profile_template_id is not None:
            result['ScriptProfileTemplateId'] = self.script_profile_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PromptsJson') is not None:
            self.prompts_json = m.get('PromptsJson')

        if m.get('ScriptProfileTemplateId') is not None:
            self.script_profile_template_id = m.get('ScriptProfileTemplateId')

        return self

class UpdateApplicationVersionRequestRagConfig(DaraModel):
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

class UpdateApplicationVersionRequestInteractionConfig(DaraModel):
    def __init__(
        self,
        silence_detection_config: main_models.UpdateApplicationVersionRequestInteractionConfigSilenceDetectionConfig = None,
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
            temp_model = main_models.UpdateApplicationVersionRequestInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class UpdateApplicationVersionRequestInteractionConfigSilenceDetectionConfig(DaraModel):
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

