# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class GetScriptResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetScriptResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # Internal error code
        self.code = code
        # Scenario object information
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # List of dynamic error parameters
        self.params = params
        # Request ID
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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetScriptResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetScriptResponseBodyData(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        created_time: int = None,
        description: str = None,
        draft_version: main_models.GetScriptResponseBodyDataDraftVersion = None,
        name: str = None,
        nlu_engine: str = None,
        published_version: main_models.GetScriptResponseBodyDataPublishedVersion = None,
        script_id: str = None,
        status: str = None,
        updated_time: int = None,
    ):
        # Concurrency
        self.concurrency = concurrency
        # Creation time
        self.created_time = created_time
        # Description
        self.description = description
        # Draft version information
        self.draft_version = draft_version
        # Scenario name
        self.name = name
        # Natural Language Understanding (NLU) engine
        self.nlu_engine = nlu_engine
        # Published version information
        self.published_version = published_version
        # Scenario ID
        self.script_id = script_id
        # Status
        self.status = status
        # Update time
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

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.published_version is not None:
            result['PublishedVersion'] = self.published_version.to_map()

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.status is not None:
            result['Status'] = self.status

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DraftVersion') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersion()
            self.draft_version = temp_model.from_map(m.get('DraftVersion'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('PublishedVersion') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersion()
            self.published_version = temp_model.from_map(m.get('PublishedVersion'))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class GetScriptResponseBodyDataPublishedVersion(DaraModel):
    def __init__(
        self,
        interaction_config: main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfig = None,
        label_config: List[main_models.GetScriptResponseBodyDataPublishedVersionLabelConfig] = None,
        script_profile: main_models.GetScriptResponseBodyDataPublishedVersionScriptProfile = None,
        synthesizer_config: main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfig = None,
        transcriber_config: main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfig = None,
        version_id: str = None,
    ):
        # Interaction configuration
        self.interaction_config = interaction_config
        # Custom tag configuration
        self.label_config = label_config
        # Dialogue capability configuration
        self.script_profile = script_profile
        # TTS configuration
        self.synthesizer_config = synthesizer_config
        # ASR configuration
        self.transcriber_config = transcriber_config
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
        if self.label_config:
            for v1 in self.label_config:
                 if v1:
                    v1.validate()
        if self.script_profile:
            self.script_profile.validate()
        if self.synthesizer_config:
            self.synthesizer_config.validate()
        if self.transcriber_config:
            self.transcriber_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

        result['LabelConfig'] = []
        if self.label_config is not None:
            for k1 in self.label_config:
                result['LabelConfig'].append(k1.to_map() if k1 else None)

        if self.script_profile is not None:
            result['ScriptProfile'] = self.script_profile.to_map()

        if self.synthesizer_config is not None:
            result['SynthesizerConfig'] = self.synthesizer_config.to_map()

        if self.transcriber_config is not None:
            result['TranscriberConfig'] = self.transcriber_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InteractionConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        self.label_config = []
        if m.get('LabelConfig') is not None:
            for k1 in m.get('LabelConfig'):
                temp_model = main_models.GetScriptResponseBodyDataPublishedVersionLabelConfig()
                self.label_config.append(temp_model.from_map(k1))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetScriptResponseBodyDataPublishedVersionTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: str = None,
        vocabulary_id: str = None,
    ):
        self.correction_rules = correction_rules
        # Custom language model ID for ASR
        self.customization_id = customization_id
        # Silence detection (sentence segmentation is triggered when the speaking interval exceeds x milliseconds, which is Voice Activity Detection (VAD)).
        self.end_silence_timeout = end_silence_timeout
        # ASR model
        self.model = model
        # **Associated configuration**
        self.nls_access_profile = nls_access_profile
        # **ASR call method**
        self.nls_access_type = nls_access_type
        # **ASR engine**
        self.nls_engine = nls_engine
        # Noise parameter threshold. The range is -100 to 100. The following describes the values:
        # 
        # The closer the value is to -100, the more likely noise is identified as speech.
        # 
        # The closer the value is to 100, the more likely speech is identified as noise.
        self.speech_noise_threshold = speech_noise_threshold
        # Hotword table ID (obtained from the hotword management page).
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
                temp_model = main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile()
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

class GetScriptResponseBodyDataPublishedVersionTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party voice configuration ID (required when using third-party ASR services such as Doubao or iFLYTEK).
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

class GetScriptResponseBodyDataPublishedVersionTranscriberConfigCorrectionRules(DaraModel):
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

class GetScriptResponseBodyDataPublishedVersionSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfigPronRules] = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        # **TTS model**
        self.model = model
        # Associated configuration
        self.nls_access_profile = nls_access_profile
        # **TTS call method**
        self.nls_access_type = nls_access_type
        # **TTS engine**
        self.nls_engine = nls_engine
        # Pitch rate
        # The range is -500 to 500.
        # The default value is 0.
        self.pitch_rate = pitch_rate
        # List of TTS intervention entries
        self.pron_rules = pron_rules
        # **Speech rate**
        # The range is -500 to 500.
        # The default value is 0.
        self.speech_rate = speech_rate
        # **Voice**
        self.voice = voice
        # Volume
        # The range is 0 to 100.
        # The default value is 50.
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
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile()
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
                temp_model = main_models.GetScriptResponseBodyDataPublishedVersionSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetScriptResponseBodyDataPublishedVersionSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        # Word prone to errors
        self.pattern = pattern
        # Homophone
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

class GetScriptResponseBodyDataPublishedVersionSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party voice configuration ID (required when using third-party ASR services such as Doubao or iFLYTEK).
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

class GetScriptResponseBodyDataPublishedVersionScriptProfile(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_profile: main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileAgentProfile = None,
        chatbot_id: str = None,
        function_meta: main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileFunctionMeta = None,
        model: str = None,
        nlu_access_profile: main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileNluAccessProfile = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        omni_model: bool = None,
    ):
        # Chatbot AgentKey. This is required when NluEngine is set to BEEBOT for the current scenario.
        self.agent_key = agent_key
        # Dialogue agent configuration
        self.agent_profile = agent_profile
        # Chatbot ID. This is required when NluEngine is set to BEEBOT for the current scenario.
        self.chatbot_id = chatbot_id
        # Function Compute configuration
        self.function_meta = function_meta
        # Dialogue model. This is required when NluEngine is set to PROMPTS for the current scenario.
        self.model = model
        # **Associated configuration**
        self.nlu_access_profile = nlu_access_profile
        # Dialogue model call method
        self.nlu_access_type = nlu_access_type
        # NLU engine
        self.nlu_engine = nlu_engine
        # Indicates whether the model is an Omni model.
        self.omni_model = omni_model

    def validate(self):
        if self.agent_profile:
            self.agent_profile.validate()
        if self.function_meta:
            self.function_meta.validate()
        if self.nlu_access_profile:
            self.nlu_access_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.agent_profile is not None:
            result['AgentProfile'] = self.agent_profile.to_map()

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.function_meta is not None:
            result['FunctionMeta'] = self.function_meta.to_map()

        if self.model is not None:
            result['Model'] = self.model

        if self.nlu_access_profile is not None:
            result['NluAccessProfile'] = self.nlu_access_profile.to_map()

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.omni_model is not None:
            result['OmniModel'] = self.omni_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AgentProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('FunctionMeta') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileFunctionMeta()
            self.function_meta = temp_model.from_map(m.get('FunctionMeta'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NluAccessProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionScriptProfileNluAccessProfile()
            self.nlu_access_profile = temp_model.from_map(m.get('NluAccessProfile'))

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('OmniModel') is not None:
            self.omni_model = m.get('OmniModel')

        return self

class GetScriptResponseBodyDataPublishedVersionScriptProfileNluAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party dialogue model configuration ID
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

class GetScriptResponseBodyDataPublishedVersionScriptProfileFunctionMeta(DaraModel):
    def __init__(
        self,
        function_id: str = None,
        function_name: str = None,
        http_trigger_name: str = None,
        http_trigger_url: str = None,
        region_id: str = None,
    ):
        # Function service ID. This is required when NluEngine is set to FUNCTION for the current scenario.
        self.function_id = function_id
        # Function service name. This is required when NluEngine is set to FUNCTION for the current scenario.
        self.function_name = function_name
        # Function trigger name. This is required when NluEngine is set to FUNCTION for the current scenario.
        self.http_trigger_name = http_trigger_name
        # Function trigger URL. This is required when NluEngine is set to FUNCTION for the current scenario.
        self.http_trigger_url = http_trigger_url
        # Region where the function service is located. This is required when NluEngine is set to FUNCTION for the current scenario.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_id is not None:
            result['FunctionId'] = self.function_id

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.http_trigger_name is not None:
            result['HttpTriggerName'] = self.http_trigger_name

        if self.http_trigger_url is not None:
            result['HttpTriggerUrl'] = self.http_trigger_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('HttpTriggerName') is not None:
            self.http_trigger_name = m.get('HttpTriggerName')

        if m.get('HttpTriggerUrl') is not None:
            self.http_trigger_url = m.get('HttpTriggerUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetScriptResponseBodyDataPublishedVersionScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        # Dialogue agent description
        self.description = description
        # Dialogue agent name
        self.name = name
        # **Prompt JSON**
        self.prompts_json = prompts_json
        # **Scenario template ID**
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

class GetScriptResponseBodyDataPublishedVersionLabelConfig(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # List of candidate values for the label
        self.candidate_values = candidate_values
        # Label description
        self.description = description
        # Label name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_values is not None:
            result['CandidateValues'] = self.candidate_values

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateValues') is not None:
            self.candidate_values = m.get('CandidateValues')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetScriptResponseBodyDataPublishedVersionInteractionConfig(DaraModel):
    def __init__(
        self,
        background_music_id: str = None,
        end_conversation_config: main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfig = None,
        initial_greeting_delay_milliseconds: int = None,
        silence_detection_config: main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig = None,
    ):
        # Background music ID
        self.background_music_id = background_music_id
        # Hang-up configuration
        self.end_conversation_config = end_conversation_config
        # - The delay before playing audio after the call is connected.
        # 
        # - Unit: milliseconds.
        self.initial_greeting_delay_milliseconds = initial_greeting_delay_milliseconds
        # Silence detection configuration
        self.silence_detection_config = silence_detection_config

    def validate(self):
        if self.end_conversation_config:
            self.end_conversation_config.validate()
        if self.silence_detection_config:
            self.silence_detection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_music_id is not None:
            result['BackgroundMusicId'] = self.background_music_id

        if self.end_conversation_config is not None:
            result['EndConversationConfig'] = self.end_conversation_config.to_map()

        if self.initial_greeting_delay_milliseconds is not None:
            result['InitialGreetingDelayMilliseconds'] = self.initial_greeting_delay_milliseconds

        if self.silence_detection_config is not None:
            result['SilenceDetectionConfig'] = self.silence_detection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundMusicId') is not None:
            self.background_music_id = m.get('BackgroundMusicId')

        if m.get('EndConversationConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfig()
            self.end_conversation_config = temp_model.from_map(m.get('EndConversationConfig'))

        if m.get('InitialGreetingDelayMilliseconds') is not None:
            self.initial_greeting_delay_milliseconds = m.get('InitialGreetingDelayMilliseconds')

        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class GetScriptResponseBodyDataPublishedVersionInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        max_repeats: int = None,
        timeout: int = None,
    ):
        # Hang up after consecutive rounds of silence.<br>
        # This takes effect when NluEngine is set to PROMPTS for the current scenario.<br>
        self.max_repeats = max_repeats
        # Silence timeout period in milliseconds.<br>
        # If the user remains silent for longer than the specified value, a silence timeout message is played.<br>
        # The range is 2000 to 10000.<br><br>
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_repeats is not None:
            result['MaxRepeats'] = self.max_repeats

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRepeats') is not None:
            self.max_repeats = m.get('MaxRepeats')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        triggers: List[main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfigTriggers] = None,
    ):
        # The hang-up action is executed x seconds after the hang-up message is played. The range is 0 to 5.
        self.delay = delay
        # Special case interception
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfigTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class GetScriptResponseBodyDataPublishedVersionInteractionConfigEndConversationConfigTriggers(DaraModel):
    def __init__(
        self,
        closing_statement: str = None,
        key_words: List[str] = None,
        trigger_type: str = None,
        turn_limit: int = None,
    ):
        # - The message to play when hanging up after reaching the maximum number of rounds.
        self.closing_statement = closing_statement
        # - List of custom interception keywords
        self.key_words = key_words
        # - **TurnLimit**: Maximum interaction rounds check.
        # 
        # - **IntelligentVoiceAssistant**: Voice assistant.
        # 
        # - **InteractiveVoiceResponse**: Extension transfer.
        # 
        # - **KeyWords**: Custom interception.
        self.trigger_type = trigger_type
        # - Hangs up when the number of interaction rounds exceeds x.
        # 
        # - The range is 0 to 100.
        # 
        # - A value of 0 indicates that the hang-up feature for exceeding the round limit is disabled.
        self.turn_limit = turn_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.closing_statement is not None:
            result['ClosingStatement'] = self.closing_statement

        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.turn_limit is not None:
            result['TurnLimit'] = self.turn_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingStatement') is not None:
            self.closing_statement = m.get('ClosingStatement')

        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TurnLimit') is not None:
            self.turn_limit = m.get('TurnLimit')

        return self

class GetScriptResponseBodyDataDraftVersion(DaraModel):
    def __init__(
        self,
        interaction_config: main_models.GetScriptResponseBodyDataDraftVersionInteractionConfig = None,
        label_config: List[main_models.GetScriptResponseBodyDataDraftVersionLabelConfig] = None,
        script_profile: main_models.GetScriptResponseBodyDataDraftVersionScriptProfile = None,
        synthesizer_config: main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfig = None,
        transcriber_config: main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfig = None,
        version_id: str = None,
    ):
        # Interaction configuration
        self.interaction_config = interaction_config
        # List of label objects
        self.label_config = label_config
        # Dialogue capability configuration
        self.script_profile = script_profile
        # TTS configuration
        self.synthesizer_config = synthesizer_config
        # ASR configuration
        self.transcriber_config = transcriber_config
        # Version ID
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
        if self.label_config:
            for v1 in self.label_config:
                 if v1:
                    v1.validate()
        if self.script_profile:
            self.script_profile.validate()
        if self.synthesizer_config:
            self.synthesizer_config.validate()
        if self.transcriber_config:
            self.transcriber_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

        result['LabelConfig'] = []
        if self.label_config is not None:
            for k1 in self.label_config:
                result['LabelConfig'].append(k1.to_map() if k1 else None)

        if self.script_profile is not None:
            result['ScriptProfile'] = self.script_profile.to_map()

        if self.synthesizer_config is not None:
            result['SynthesizerConfig'] = self.synthesizer_config.to_map()

        if self.transcriber_config is not None:
            result['TranscriberConfig'] = self.transcriber_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InteractionConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        self.label_config = []
        if m.get('LabelConfig') is not None:
            for k1 in m.get('LabelConfig'):
                temp_model = main_models.GetScriptResponseBodyDataDraftVersionLabelConfig()
                self.label_config.append(temp_model.from_map(k1))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetScriptResponseBodyDataDraftVersionTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: str = None,
        vocabulary_id: str = None,
    ):
        self.correction_rules = correction_rules
        # Self-learning language model ID (not currently supported)
        self.customization_id = customization_id
        # Voice Activity Detection (VAD) sentence segmentation
        self.end_silence_timeout = end_silence_timeout
        # ASR model
        self.model = model
        # Access account configuration
        self.nls_access_profile = nls_access_profile
        # ASR call method
        self.nls_access_type = nls_access_type
        # ASR engine
        self.nls_engine = nls_engine
        # Noise threshold
        self.speech_noise_threshold = speech_noise_threshold
        # Hotword ID
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
                temp_model = main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile()
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

class GetScriptResponseBodyDataDraftVersionTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party voice configuration ID
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

class GetScriptResponseBodyDataDraftVersionTranscriberConfigCorrectionRules(DaraModel):
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

class GetScriptResponseBodyDataDraftVersionSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfigPronRules] = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        # TTS model
        self.model = model
        # Access account configuration
        self.nls_access_profile = nls_access_profile
        # TTS call method
        self.nls_access_type = nls_access_type
        # TTS engine
        self.nls_engine = nls_engine
        # The speech pitch.
        self.pitch_rate = pitch_rate
        # List of TTS intervention dictionaries
        self.pron_rules = pron_rules
        # Speech rate
        self.speech_rate = speech_rate
        # Voice
        self.voice = voice
        # Volume
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
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile()
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
                temp_model = main_models.GetScriptResponseBodyDataDraftVersionSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class GetScriptResponseBodyDataDraftVersionSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        # Word prone to errors
        self.pattern = pattern
        # Replacement word
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

class GetScriptResponseBodyDataDraftVersionSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party voice configuration
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

class GetScriptResponseBodyDataDraftVersionScriptProfile(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_profile: main_models.GetScriptResponseBodyDataDraftVersionScriptProfileAgentProfile = None,
        chatbot_id: str = None,
        function_meta: main_models.GetScriptResponseBodyDataDraftVersionScriptProfileFunctionMeta = None,
        model: str = None,
        nlu_access_profile: main_models.GetScriptResponseBodyDataDraftVersionScriptProfileNluAccessProfile = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
        omni_model: bool = None,
    ):
        # Chatbot AgentKey
        self.agent_key = agent_key
        # Dialogue agent configuration
        self.agent_profile = agent_profile
        # Chatbot ID
        self.chatbot_id = chatbot_id
        # Function Compute configuration
        self.function_meta = function_meta
        # Dialogue model
        self.model = model
        # Associated configuration
        self.nlu_access_profile = nlu_access_profile
        # Dialogue model call method
        self.nlu_access_type = nlu_access_type
        # NLU engine
        self.nlu_engine = nlu_engine
        # Indicates whether the model is an Omni model.
        self.omni_model = omni_model

    def validate(self):
        if self.agent_profile:
            self.agent_profile.validate()
        if self.function_meta:
            self.function_meta.validate()
        if self.nlu_access_profile:
            self.nlu_access_profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.agent_profile is not None:
            result['AgentProfile'] = self.agent_profile.to_map()

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.function_meta is not None:
            result['FunctionMeta'] = self.function_meta.to_map()

        if self.model is not None:
            result['Model'] = self.model

        if self.nlu_access_profile is not None:
            result['NluAccessProfile'] = self.nlu_access_profile.to_map()

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        if self.omni_model is not None:
            result['OmniModel'] = self.omni_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AgentProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('FunctionMeta') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionScriptProfileFunctionMeta()
            self.function_meta = temp_model.from_map(m.get('FunctionMeta'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NluAccessProfile') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionScriptProfileNluAccessProfile()
            self.nlu_access_profile = temp_model.from_map(m.get('NluAccessProfile'))

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        if m.get('OmniModel') is not None:
            self.omni_model = m.get('OmniModel')

        return self

class GetScriptResponseBodyDataDraftVersionScriptProfileNluAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # Third-party dialogue model configuration ID
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

class GetScriptResponseBodyDataDraftVersionScriptProfileFunctionMeta(DaraModel):
    def __init__(
        self,
        function_id: str = None,
        function_name: str = None,
        http_trigger_name: str = None,
        http_trigger_url: str = None,
        region_id: str = None,
    ):
        # Function service ID
        self.function_id = function_id
        # Function service name
        self.function_name = function_name
        # Function trigger name
        self.http_trigger_name = http_trigger_name
        # Function trigger URL
        self.http_trigger_url = http_trigger_url
        # Region where the function service is located
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_id is not None:
            result['FunctionId'] = self.function_id

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.http_trigger_name is not None:
            result['HttpTriggerName'] = self.http_trigger_name

        if self.http_trigger_url is not None:
            result['HttpTriggerUrl'] = self.http_trigger_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('HttpTriggerName') is not None:
            self.http_trigger_name = m.get('HttpTriggerName')

        if m.get('HttpTriggerUrl') is not None:
            self.http_trigger_url = m.get('HttpTriggerUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetScriptResponseBodyDataDraftVersionScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        # Prompt JSON
        self.prompts_json = prompts_json
        # Scenario template ID
        self.script_profile_template_id = script_profile_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompts_json is not None:
            result['PromptsJson'] = self.prompts_json

        if self.script_profile_template_id is not None:
            result['ScriptProfileTemplateId'] = self.script_profile_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptsJson') is not None:
            self.prompts_json = m.get('PromptsJson')

        if m.get('ScriptProfileTemplateId') is not None:
            self.script_profile_template_id = m.get('ScriptProfileTemplateId')

        return self

class GetScriptResponseBodyDataDraftVersionLabelConfig(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # List of candidate values for the label
        self.candidate_values = candidate_values
        # Label description
        self.description = description
        # Label name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_values is not None:
            result['CandidateValues'] = self.candidate_values

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateValues') is not None:
            self.candidate_values = m.get('CandidateValues')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetScriptResponseBodyDataDraftVersionInteractionConfig(DaraModel):
    def __init__(
        self,
        background_music_id: str = None,
        end_conversation_config: main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfig = None,
        initial_greeting_delay_milliseconds: int = None,
        silence_detection_config: main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig = None,
    ):
        # Background music ID
        self.background_music_id = background_music_id
        # Hang-up configuration
        self.end_conversation_config = end_conversation_config
        # The delay before playing audio after the call is connected, in milliseconds.
        self.initial_greeting_delay_milliseconds = initial_greeting_delay_milliseconds
        # Silence detection configuration
        self.silence_detection_config = silence_detection_config

    def validate(self):
        if self.end_conversation_config:
            self.end_conversation_config.validate()
        if self.silence_detection_config:
            self.silence_detection_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_music_id is not None:
            result['BackgroundMusicId'] = self.background_music_id

        if self.end_conversation_config is not None:
            result['EndConversationConfig'] = self.end_conversation_config.to_map()

        if self.initial_greeting_delay_milliseconds is not None:
            result['InitialGreetingDelayMilliseconds'] = self.initial_greeting_delay_milliseconds

        if self.silence_detection_config is not None:
            result['SilenceDetectionConfig'] = self.silence_detection_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundMusicId') is not None:
            self.background_music_id = m.get('BackgroundMusicId')

        if m.get('EndConversationConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfig()
            self.end_conversation_config = temp_model.from_map(m.get('EndConversationConfig'))

        if m.get('InitialGreetingDelayMilliseconds') is not None:
            self.initial_greeting_delay_milliseconds = m.get('InitialGreetingDelayMilliseconds')

        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class GetScriptResponseBodyDataDraftVersionInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        max_repeats: int = None,
        timeout: int = None,
    ):
        # Hang up after consecutive rounds of silence. This takes effect when NluEngine is set to PROMPTS for the current scenario.
        self.max_repeats = max_repeats
        # Silence timeout period in milliseconds. If the user remains silent for longer than the specified value, a silence timeout message is played. The range is 2000 to 10000.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_repeats is not None:
            result['MaxRepeats'] = self.max_repeats

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRepeats') is not None:
            self.max_repeats = m.get('MaxRepeats')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        triggers: List[main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfigTriggers] = None,
    ):
        # The hang-up action is executed x seconds after the hang-up message is played. The range is 0 to 5.
        self.delay = delay
        # List of special case interceptions
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for v1 in self.triggers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay is not None:
            result['Delay'] = self.delay

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfigTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class GetScriptResponseBodyDataDraftVersionInteractionConfigEndConversationConfigTriggers(DaraModel):
    def __init__(
        self,
        closing_statement: str = None,
        key_words: List[str] = None,
        trigger_type: str = None,
        turn_limit: int = None,
    ):
        # The message to play when hanging up after reaching the maximum number of rounds.
        self.closing_statement = closing_statement
        # List of custom interception keywords
        self.key_words = key_words
        # TurnLimit: Maximum interaction rounds check. IntelligentVoiceAssistant: Voice assistant. InteractiveVoiceResponse: Extension transfer. KeyWords: Custom interception
        self.trigger_type = trigger_type
        # Hangs up when the number of interaction rounds exceeds x. The range is 0 to 100. A value of 0 indicates that the hang-up feature for exceeding the round limit is disabled.
        self.turn_limit = turn_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.closing_statement is not None:
            result['ClosingStatement'] = self.closing_statement

        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.turn_limit is not None:
            result['TurnLimit'] = self.turn_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingStatement') is not None:
            self.closing_statement = m.get('ClosingStatement')

        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TurnLimit') is not None:
            self.turn_limit = m.get('TurnLimit')

        return self

