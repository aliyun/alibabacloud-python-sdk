# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class CreateScriptVersionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        interaction_config: main_models.CreateScriptVersionRequestInteractionConfig = None,
        label_config: List[main_models.CreateScriptVersionRequestLabelConfig] = None,
        script_id: str = None,
        script_profile: main_models.CreateScriptVersionRequestScriptProfile = None,
        source_version_id: str = None,
        synthesizer_config: main_models.CreateScriptVersionRequestSynthesizerConfig = None,
        transcriber_config: main_models.CreateScriptVersionRequestTranscriberConfig = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The interaction configuration.
        self.interaction_config = interaction_config
        # The custom label configuration.
        self.label_config = label_config
        # The scenario ID.
        self.script_id = script_id
        # The conversation capability configuration.
        self.script_profile = script_profile
        self.source_version_id = source_version_id
        # The TTS configuration.
        self.synthesizer_config = synthesizer_config
        # The ASR configuration.
        self.transcriber_config = transcriber_config

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

        result['LabelConfig'] = []
        if self.label_config is not None:
            for k1 in self.label_config:
                result['LabelConfig'].append(k1.to_map() if k1 else None)

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_profile is not None:
            result['ScriptProfile'] = self.script_profile.to_map()

        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id

        if self.synthesizer_config is not None:
            result['SynthesizerConfig'] = self.synthesizer_config.to_map()

        if self.transcriber_config is not None:
            result['TranscriberConfig'] = self.transcriber_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InteractionConfig') is not None:
            temp_model = main_models.CreateScriptVersionRequestInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        self.label_config = []
        if m.get('LabelConfig') is not None:
            for k1 in m.get('LabelConfig'):
                temp_model = main_models.CreateScriptVersionRequestLabelConfig()
                self.label_config.append(temp_model.from_map(k1))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.CreateScriptVersionRequestScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.CreateScriptVersionRequestSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.CreateScriptVersionRequestTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        return self

class CreateScriptVersionRequestTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.CreateScriptVersionRequestTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.CreateScriptVersionRequestTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: int = None,
        vocabulary_id: str = None,
    ):
        self.correction_rules = correction_rules
        # The custom language model ID for ASR.
        self.customization_id = customization_id
        # The silence detection threshold. When the silence interval between speech segments exceeds x milliseconds, sentence segmentation is triggered (Voice Activity Detection, or VAD).
        self.end_silence_timeout = end_silence_timeout
        # The ASR model.
        self.model = model
        # The associated configuration.
        self.nls_access_profile = nls_access_profile
        # The ASR invocation method.
        self.nls_access_type = nls_access_type
        # The ASR engine.
        self.nls_engine = nls_engine
        # The noise threshold. Valid values: -100 to 100.
        # 
        # A value closer to -100 increases the probability that noise is classified as speech.
        # 
        # A value closer to +100 increases the probability that speech is classified as noise.
        self.speech_noise_threshold = speech_noise_threshold
        # The hot word list ID. You can obtain this ID from the hot word management page.
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
                temp_model = main_models.CreateScriptVersionRequestTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.CreateScriptVersionRequestTranscriberConfigNlsAccessProfile()
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

class CreateScriptVersionRequestTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party voice configuration ID. This parameter is required when you use a third-party ASR service such as Doubao or iFLYTEK.
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

class CreateScriptVersionRequestTranscriberConfigCorrectionRules(DaraModel):
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

class CreateScriptVersionRequestSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.CreateScriptVersionRequestSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.CreateScriptVersionRequestSynthesizerConfigPronRules] = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        # The TTS model.
        self.model = model
        # The associated configuration.
        self.nls_access_profile = nls_access_profile
        # The TTS invocation method.
        self.nls_access_type = nls_access_type
        # The TTS engine.
        self.nls_engine = nls_engine
        # The pitch rate.\\
        # Valid values: -500 to 500.\\
        # Default value: 0.
        self.pitch_rate = pitch_rate
        # The TTS pronunciation correction list.
        self.pron_rules = pron_rules
        # The speech rate.\\
        # Valid values: -500 to 500.\\
        # Default value: 0.
        self.speech_rate = speech_rate
        # The voice speaker.
        self.voice = voice
        # The volume.\\
        # Valid values: 0 to 100.\\
        # Default value: 50.
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
            temp_model = main_models.CreateScriptVersionRequestSynthesizerConfigNlsAccessProfile()
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
                temp_model = main_models.CreateScriptVersionRequestSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class CreateScriptVersionRequestSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        # The commonly mispronounced word.
        self.pattern = pattern
        # The homophone replacement word.
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

class CreateScriptVersionRequestSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party voice configuration ID. This parameter is required when you use a third-party ASR service such as Doubao or iFLYTEK.
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

class CreateScriptVersionRequestScriptProfile(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_profile: main_models.CreateScriptVersionRequestScriptProfileAgentProfile = None,
        chatbot_id: str = None,
        function_meta: main_models.CreateScriptVersionRequestScriptProfileFunctionMeta = None,
        model: str = None,
        nlu_access_profile: main_models.CreateScriptVersionRequestScriptProfileNluAccessProfile = None,
        nlu_access_type: str = None,
        omni_model: bool = None,
    ):
        # The AgentKey of the chatbot.\\
        # This parameter is required when NluEngine is set to BEEBOT for the current scenario.
        self.agent_key = agent_key
        # The conversation agent configuration.
        self.agent_profile = agent_profile
        # The chatbot ID.\\
        # This parameter is required when NluEngine is set to BEEBOT for the current scenario.
        self.chatbot_id = chatbot_id
        # The Function Compute configuration.
        self.function_meta = function_meta
        # The conversation model.\\
        # This parameter is required when NluEngine is set to PROMPTS for the current scenario.
        self.model = model
        # The associated configuration.
        self.nlu_access_profile = nlu_access_profile
        # The conversation model invocation method.
        self.nlu_access_type = nlu_access_type
        # Specifies whether the model is an Omni model.
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

        if self.omni_model is not None:
            result['OmniModel'] = self.omni_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('AgentProfile') is not None:
            temp_model = main_models.CreateScriptVersionRequestScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('FunctionMeta') is not None:
            temp_model = main_models.CreateScriptVersionRequestScriptProfileFunctionMeta()
            self.function_meta = temp_model.from_map(m.get('FunctionMeta'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NluAccessProfile') is not None:
            temp_model = main_models.CreateScriptVersionRequestScriptProfileNluAccessProfile()
            self.nlu_access_profile = temp_model.from_map(m.get('NluAccessProfile'))

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('OmniModel') is not None:
            self.omni_model = m.get('OmniModel')

        return self

class CreateScriptVersionRequestScriptProfileNluAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party conversation model configuration ID.
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

class CreateScriptVersionRequestScriptProfileFunctionMeta(DaraModel):
    def __init__(
        self,
        function_id: str = None,
        function_name: str = None,
        http_trigger_name: str = None,
        http_trigger_url: str = None,
        region_id: str = None,
    ):
        # The function service ID.\\
        # This parameter is required when NluEngine is set to FUNCTION for the current scenario.
        self.function_id = function_id
        # The function service name.\\
        # This parameter is required when NluEngine is set to FUNCTION for the current scenario.
        self.function_name = function_name
        # The HTTP trigger name.\\
        # This parameter is required when NluEngine is set to FUNCTION for the current scenario.
        self.http_trigger_name = http_trigger_name
        # The HTTP trigger URL.\\
        # This parameter is required when NluEngine is set to FUNCTION for the current scenario.
        self.http_trigger_url = http_trigger_url
        # The region where the function service resides.\\
        # This parameter is required when NluEngine is set to FUNCTION for the current scenario.
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

class CreateScriptVersionRequestScriptProfileAgentProfile(DaraModel):
    def __init__(
        self,
        prompts_json: str = None,
        script_profile_template_id: str = None,
    ):
        # The prompt in JSON format.
        self.prompts_json = prompts_json
        # The scenario template ID.
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

class CreateScriptVersionRequestLabelConfig(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # The list of candidate values for the label.
        self.candidate_values = candidate_values
        # The label description.
        self.description = description
        # The label name.
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

class CreateScriptVersionRequestInteractionConfig(DaraModel):
    def __init__(
        self,
        background_music_id: str = None,
        end_conversation_config: main_models.CreateScriptVersionRequestInteractionConfigEndConversationConfig = None,
        initial_greeting_delay_milliseconds: int = None,
        silence_detection_config: main_models.CreateScriptVersionRequestInteractionConfigSilenceDetectionConfig = None,
    ):
        # The background music ID.
        self.background_music_id = background_music_id
        # The hang-up configuration.
        self.end_conversation_config = end_conversation_config
        # The delay before playing the greeting after the call is connected. Unit: milliseconds.
        self.initial_greeting_delay_milliseconds = initial_greeting_delay_milliseconds
        # The silence detection configuration.
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
            temp_model = main_models.CreateScriptVersionRequestInteractionConfigEndConversationConfig()
            self.end_conversation_config = temp_model.from_map(m.get('EndConversationConfig'))

        if m.get('InitialGreetingDelayMilliseconds') is not None:
            self.initial_greeting_delay_milliseconds = m.get('InitialGreetingDelayMilliseconds')

        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.CreateScriptVersionRequestInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        return self

class CreateScriptVersionRequestInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        max_repeats: int = None,
        timeout: int = None,
    ):
        # The number of consecutive silence turns before the hang-up action is executed.\\
        # This parameter takes effect when NluEngine is set to PROMPTS for the current scenario.
        self.max_repeats = max_repeats
        # The silence timeout period, in milliseconds.\\
        # When the user remains silent for longer than the specified value, the silence timeout script is played.\\
        # Valid values: 2000 to 10000.
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

class CreateScriptVersionRequestInteractionConfigEndConversationConfig(DaraModel):
    def __init__(
        self,
        delay: int = None,
        triggers: List[main_models.CreateScriptVersionRequestInteractionConfigEndConversationConfigTriggers] = None,
    ):
        # The number of seconds to wait after the hang-up script finishes playing before executing the hang-up action. Valid values: 0 to 5.
        self.delay = delay
        # The special case interception rules.
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
                temp_model = main_models.CreateScriptVersionRequestInteractionConfigEndConversationConfigTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class CreateScriptVersionRequestInteractionConfigEndConversationConfigTriggers(DaraModel):
    def __init__(
        self,
        closing_statement: str = None,
        key_words: List[str] = None,
        trigger_type: str = None,
        turn_limit: int = None,
    ):
        # The closing statement played when the turn limit is reached and the hang-up action is executed.
        self.closing_statement = closing_statement
        # The list of custom interception keywords.
        self.key_words = key_words
        # Valid values:\\
        # - TurnLimit: Maximum interaction turn check.\\
        # - IntelligentVoiceAssistant: Voice assistant.\\
        # - InteractiveVoiceResponse: Extension transfer.\\
        # - KeyWords: Custom interception.
        self.trigger_type = trigger_type
        # The maximum number of interaction turns before the hang-up action is executed. Valid values: 0 to 100. A value of 0 indicates that the turn-limit hang-up feature is disabled.
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

