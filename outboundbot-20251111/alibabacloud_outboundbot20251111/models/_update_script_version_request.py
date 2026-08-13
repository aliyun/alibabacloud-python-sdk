# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class UpdateScriptVersionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        interaction_config: main_models.UpdateScriptVersionRequestInteractionConfig = None,
        label_configs: List[main_models.UpdateScriptVersionRequestLabelConfigs] = None,
        script_id: str = None,
        script_profile: main_models.UpdateScriptVersionRequestScriptProfile = None,
        synthesizer_config: main_models.UpdateScriptVersionRequestSynthesizerConfig = None,
        transcriber_config: main_models.UpdateScriptVersionRequestTranscriberConfig = None,
        version_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The interaction configuration.
        self.interaction_config = interaction_config
        # The label configurations.
        self.label_configs = label_configs
        # The scenario ID.
        self.script_id = script_id
        # The dialogue capability configuration.
        self.script_profile = script_profile
        # The TTS configuration.
        self.synthesizer_config = synthesizer_config
        # The ASR configuration.
        self.transcriber_config = transcriber_config
        # The version ID.
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
        if self.label_configs:
            for v1 in self.label_configs:
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

        result['LabelConfigs'] = []
        if self.label_configs is not None:
            for k1 in self.label_configs:
                result['LabelConfigs'].append(k1.to_map() if k1 else None)

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InteractionConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        self.label_configs = []
        if m.get('LabelConfigs') is not None:
            for k1 in m.get('LabelConfigs'):
                temp_model = main_models.UpdateScriptVersionRequestLabelConfigs()
                self.label_configs.append(temp_model.from_map(k1))

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.UpdateScriptVersionRequestScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class UpdateScriptVersionRequestTranscriberConfig(DaraModel):
    def __init__(
        self,
        correction_rules: List[main_models.UpdateScriptVersionRequestTranscriberConfigCorrectionRules] = None,
        customization_id: str = None,
        end_silence_timeout: int = None,
        model: str = None,
        nls_access_profile: main_models.UpdateScriptVersionRequestTranscriberConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        speech_noise_threshold: int = None,
        vocabulary_id: str = None,
    ):
        # The ASR correction dictionary.
        self.correction_rules = correction_rules
        # The custom language model ID for ASR.
        self.customization_id = customization_id
        # The silence detection threshold. Sentence segmentation is triggered when the speaking interval exceeds x milliseconds, also known as Voice Activity Detection (VAD).
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
        # A value closer to -100 increases the probability that noise is recognized as speech.
        # 
        # A value closer to +100 increases the probability that speech is recognized as noise.
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
                temp_model = main_models.UpdateScriptVersionRequestTranscriberConfigCorrectionRules()
                self.correction_rules.append(temp_model.from_map(k1))

        if m.get('CustomizationId') is not None:
            self.customization_id = m.get('CustomizationId')

        if m.get('EndSilenceTimeout') is not None:
            self.end_silence_timeout = m.get('EndSilenceTimeout')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NlsAccessProfile') is not None:
            temp_model = main_models.UpdateScriptVersionRequestTranscriberConfigNlsAccessProfile()
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

class UpdateScriptVersionRequestTranscriberConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party speech configuration ID. This parameter is required when you use a third-party ASR service such as Doubao or iFLYTEK.
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

class UpdateScriptVersionRequestTranscriberConfigCorrectionRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        # The incorrectly recognized text.
        self.pattern = pattern
        # The corrected text.
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

class UpdateScriptVersionRequestSynthesizerConfig(DaraModel):
    def __init__(
        self,
        model: str = None,
        nls_access_profile: main_models.UpdateScriptVersionRequestSynthesizerConfigNlsAccessProfile = None,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        pron_rules: List[main_models.UpdateScriptVersionRequestSynthesizerConfigPronRules] = None,
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
        # The pitch rate.
        self.pitch_rate = pitch_rate
        # The TTS correction dictionary.
        self.pron_rules = pron_rules
        # The speech rate.
        self.speech_rate = speech_rate
        # The voice.
        self.voice = voice
        # The volume.
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
            temp_model = main_models.UpdateScriptVersionRequestSynthesizerConfigNlsAccessProfile()
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
                temp_model = main_models.UpdateScriptVersionRequestSynthesizerConfigPronRules()
                self.pron_rules.append(temp_model.from_map(k1))

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

class UpdateScriptVersionRequestSynthesizerConfigPronRules(DaraModel):
    def __init__(
        self,
        pattern: str = None,
        replacement: str = None,
    ):
        # The easily mispronounced word or phrase.
        self.pattern = pattern
        # The homophonic word or phrase.
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

class UpdateScriptVersionRequestSynthesizerConfigNlsAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party speech configuration ID. This parameter is required when you use a third-party ASR service such as Doubao or iFLYTEK.
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

class UpdateScriptVersionRequestScriptProfile(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        agent_profile: main_models.UpdateScriptVersionRequestScriptProfileAgentProfile = None,
        builder_type: str = None,
        chatbot_id: str = None,
        function_meta: main_models.UpdateScriptVersionRequestScriptProfileFunctionMeta = None,
        model: str = None,
        nlu_access_profile: main_models.UpdateScriptVersionRequestScriptProfileNluAccessProfile = None,
        nlu_access_type: str = None,
        omni_model: bool = None,
    ):
        # The chatbot AgentKey.
        self.agent_key = agent_key
        # The dialogue agent configuration.
        self.agent_profile = agent_profile
        # The chatbot type.
        self.builder_type = builder_type
        # The chatbot ID.
        self.chatbot_id = chatbot_id
        # The function compute configuration.
        self.function_meta = function_meta
        # The dialogue model.
        self.model = model
        # The associated configuration.
        self.nlu_access_profile = nlu_access_profile
        # The dialogue model invocation method.
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

        if self.builder_type is not None:
            result['BuilderType'] = self.builder_type

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
            temp_model = main_models.UpdateScriptVersionRequestScriptProfileAgentProfile()
            self.agent_profile = temp_model.from_map(m.get('AgentProfile'))

        if m.get('BuilderType') is not None:
            self.builder_type = m.get('BuilderType')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('FunctionMeta') is not None:
            temp_model = main_models.UpdateScriptVersionRequestScriptProfileFunctionMeta()
            self.function_meta = temp_model.from_map(m.get('FunctionMeta'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('NluAccessProfile') is not None:
            temp_model = main_models.UpdateScriptVersionRequestScriptProfileNluAccessProfile()
            self.nlu_access_profile = temp_model.from_map(m.get('NluAccessProfile'))

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('OmniModel') is not None:
            self.omni_model = m.get('OmniModel')

        return self

class UpdateScriptVersionRequestScriptProfileNluAccessProfile(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
    ):
        # The third-party dialogue model configuration ID.
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

class UpdateScriptVersionRequestScriptProfileFunctionMeta(DaraModel):
    def __init__(
        self,
        function_id: str = None,
        function_name: str = None,
        http_trigger_name: str = None,
        http_trigger_url: str = None,
        region_id: str = None,
    ):
        # The function service ID.
        self.function_id = function_id
        # The function service name.
        self.function_name = function_name
        # The function trigger name.
        self.http_trigger_name = http_trigger_name
        # The function trigger URL.
        self.http_trigger_url = http_trigger_url
        # The region where the function service resides.
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

class UpdateScriptVersionRequestScriptProfileAgentProfile(DaraModel):
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

class UpdateScriptVersionRequestLabelConfigs(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # The candidate values for the label.
        self.candidate_values = candidate_values
        # The description.
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

class UpdateScriptVersionRequestInteractionConfig(DaraModel):
    def __init__(
        self,
        background_music_id: str = None,
        barge_in_config: main_models.UpdateScriptVersionRequestInteractionConfigBargeInConfig = None,
        end_conversation_config: main_models.UpdateScriptVersionRequestInteractionConfigEndConversationConfig = None,
        initial_greeting_delay_milliseconds: int = None,
        silence_detection_config: main_models.UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfig = None,
        transition_config: main_models.UpdateScriptVersionRequestInteractionConfigTransitionConfig = None,
    ):
        # The background music ID.
        self.background_music_id = background_music_id
        # The barge-in configuration.
        self.barge_in_config = barge_in_config
        # The hang-up configuration.
        self.end_conversation_config = end_conversation_config
        # The delay in milliseconds before playing audio after the call is connected.
        self.initial_greeting_delay_milliseconds = initial_greeting_delay_milliseconds
        # The silence detection configuration.
        self.silence_detection_config = silence_detection_config
        # The transition phrase model configuration.
        self.transition_config = transition_config

    def validate(self):
        if self.barge_in_config:
            self.barge_in_config.validate()
        if self.end_conversation_config:
            self.end_conversation_config.validate()
        if self.silence_detection_config:
            self.silence_detection_config.validate()
        if self.transition_config:
            self.transition_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_music_id is not None:
            result['BackgroundMusicId'] = self.background_music_id

        if self.barge_in_config is not None:
            result['BargeInConfig'] = self.barge_in_config.to_map()

        if self.end_conversation_config is not None:
            result['EndConversationConfig'] = self.end_conversation_config.to_map()

        if self.initial_greeting_delay_milliseconds is not None:
            result['InitialGreetingDelayMilliseconds'] = self.initial_greeting_delay_milliseconds

        if self.silence_detection_config is not None:
            result['SilenceDetectionConfig'] = self.silence_detection_config.to_map()

        if self.transition_config is not None:
            result['TransitionConfig'] = self.transition_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundMusicId') is not None:
            self.background_music_id = m.get('BackgroundMusicId')

        if m.get('BargeInConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestInteractionConfigBargeInConfig()
            self.barge_in_config = temp_model.from_map(m.get('BargeInConfig'))

        if m.get('EndConversationConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestInteractionConfigEndConversationConfig()
            self.end_conversation_config = temp_model.from_map(m.get('EndConversationConfig'))

        if m.get('InitialGreetingDelayMilliseconds') is not None:
            self.initial_greeting_delay_milliseconds = m.get('InitialGreetingDelayMilliseconds')

        if m.get('SilenceDetectionConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfig()
            self.silence_detection_config = temp_model.from_map(m.get('SilenceDetectionConfig'))

        if m.get('TransitionConfig') is not None:
            temp_model = main_models.UpdateScriptVersionRequestInteractionConfigTransitionConfig()
            self.transition_config = temp_model.from_map(m.get('TransitionConfig'))

        return self

class UpdateScriptVersionRequestInteractionConfigTransitionConfig(DaraModel):
    def __init__(
        self,
        ai_phrase_prompt: str = None,
        fixed_phrase_list: List[str] = None,
        phrase_source: str = None,
        transition_switch: bool = None,
    ):
        # The prompt for model-generated transition phrases.
        self.ai_phrase_prompt = ai_phrase_prompt
        # The list of fixed transition phrases.
        self.fixed_phrase_list = fixed_phrase_list
        # The method for generating transition phrases.
        self.phrase_source = phrase_source
        # Specifies whether to enable transition phrases.
        self.transition_switch = transition_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_phrase_prompt is not None:
            result['AiPhrasePrompt'] = self.ai_phrase_prompt

        if self.fixed_phrase_list is not None:
            result['FixedPhraseList'] = self.fixed_phrase_list

        if self.phrase_source is not None:
            result['PhraseSource'] = self.phrase_source

        if self.transition_switch is not None:
            result['TransitionSwitch'] = self.transition_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiPhrasePrompt') is not None:
            self.ai_phrase_prompt = m.get('AiPhrasePrompt')

        if m.get('FixedPhraseList') is not None:
            self.fixed_phrase_list = m.get('FixedPhraseList')

        if m.get('PhraseSource') is not None:
            self.phrase_source = m.get('PhraseSource')

        if m.get('TransitionSwitch') is not None:
            self.transition_switch = m.get('TransitionSwitch')

        return self

class UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfig(DaraModel):
    def __init__(
        self,
        fallback_control_params_list: List[main_models.UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfigFallbackControlParamsList] = None,
        max_repeats: int = None,
        prompt: str = None,
        timeout: int = None,
    ):
        # The list of actions to perform during consecutive silence.
        self.fallback_control_params_list = fallback_control_params_list
        # The number of consecutive silence rounds before hanging up.
        self.max_repeats = max_repeats
        # The silence prompt.
        self.prompt = prompt
        # The silence timeout period, in milliseconds. When the user remains silent for longer than the specified value, the silence timeout prompt is played. Valid range: 2000 to 10000.
        self.timeout = timeout

    def validate(self):
        if self.fallback_control_params_list:
            for v1 in self.fallback_control_params_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FallbackControlParamsList'] = []
        if self.fallback_control_params_list is not None:
            for k1 in self.fallback_control_params_list:
                result['FallbackControlParamsList'].append(k1.to_map() if k1 else None)

        if self.max_repeats is not None:
            result['MaxRepeats'] = self.max_repeats

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fallback_control_params_list = []
        if m.get('FallbackControlParamsList') is not None:
            for k1 in m.get('FallbackControlParamsList'):
                temp_model = main_models.UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfigFallbackControlParamsList()
                self.fallback_control_params_list.append(temp_model.from_map(k1))

        if m.get('MaxRepeats') is not None:
            self.max_repeats = m.get('MaxRepeats')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class UpdateScriptVersionRequestInteractionConfigSilenceDetectionConfigFallbackControlParamsList(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The action to perform during consecutive silence.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateScriptVersionRequestInteractionConfigEndConversationConfig(DaraModel):
    def __init__(
        self,
        barge_in_enabled: bool = None,
        delay: int = None,
        triggers: List[main_models.UpdateScriptVersionRequestInteractionConfigEndConversationConfigTriggers] = None,
    ):
        # Specifies whether barge-in is supported during the delayed hang-up waiting period.
        self.barge_in_enabled = barge_in_enabled
        # The number of seconds to wait after the hang-up script finishes playing before executing the hang-up action. Valid values: 0 to 5.
        self.delay = delay
        # The special condition interception configuration.
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
        if self.barge_in_enabled is not None:
            result['BargeInEnabled'] = self.barge_in_enabled

        if self.delay is not None:
            result['Delay'] = self.delay

        result['Triggers'] = []
        if self.triggers is not None:
            for k1 in self.triggers:
                result['Triggers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BargeInEnabled') is not None:
            self.barge_in_enabled = m.get('BargeInEnabled')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        self.triggers = []
        if m.get('Triggers') is not None:
            for k1 in m.get('Triggers'):
                temp_model = main_models.UpdateScriptVersionRequestInteractionConfigEndConversationConfigTriggers()
                self.triggers.append(temp_model.from_map(k1))

        return self

class UpdateScriptVersionRequestInteractionConfigEndConversationConfigTriggers(DaraModel):
    def __init__(
        self,
        closing_statement: str = None,
        keywords: List[str] = None,
        trigger_type: str = None,
        turn_limit: int = None,
    ):
        # The closing script to play when the turn limit is reached and hang-up is executed.
        self.closing_statement = closing_statement
        # The list of custom interception keywords.
        self.keywords = keywords
        # Valid values:
        # 
        # - TurnLimit: maximum interaction turn limit check.
        self.trigger_type = trigger_type
        # The maximum number of interaction turns before executing hang-up. Valid values: 0 to 100. A value of 0 indicates that the turn-limit hang-up is not enabled.
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

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.turn_limit is not None:
            result['TurnLimit'] = self.turn_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingStatement') is not None:
            self.closing_statement = m.get('ClosingStatement')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('TurnLimit') is not None:
            self.turn_limit = m.get('TurnLimit')

        return self

class UpdateScriptVersionRequestInteractionConfigBargeInConfig(DaraModel):
    def __init__(
        self,
        closing_barge_in_enabled: bool = None,
        global_barge_in_enabled: bool = None,
        opening_barge_in_enabled: bool = None,
    ):
        # Specifies whether barge-in is supported during the closing statement.
        self.closing_barge_in_enabled = closing_barge_in_enabled
        # Specifies whether barge-in is supported during the conversation.
        self.global_barge_in_enabled = global_barge_in_enabled
        # Specifies whether barge-in is supported during the opening greeting.
        self.opening_barge_in_enabled = opening_barge_in_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.closing_barge_in_enabled is not None:
            result['ClosingBargeInEnabled'] = self.closing_barge_in_enabled

        if self.global_barge_in_enabled is not None:
            result['GlobalBargeInEnabled'] = self.global_barge_in_enabled

        if self.opening_barge_in_enabled is not None:
            result['OpeningBargeInEnabled'] = self.opening_barge_in_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingBargeInEnabled') is not None:
            self.closing_barge_in_enabled = m.get('ClosingBargeInEnabled')

        if m.get('GlobalBargeInEnabled') is not None:
            self.global_barge_in_enabled = m.get('GlobalBargeInEnabled')

        if m.get('OpeningBargeInEnabled') is not None:
            self.opening_barge_in_enabled = m.get('OpeningBargeInEnabled')

        return self

