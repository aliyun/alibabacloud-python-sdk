# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationVersionRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        business_unit_id: str = None,
        interaction_config: main_models.UpdateApplicationVersionRequestInteractionConfig = None,
        script_profile: main_models.UpdateApplicationVersionRequestScriptProfile = None,
        synthesizer_config: main_models.UpdateApplicationVersionRequestSynthesizerConfig = None,
        transcriber_config: main_models.UpdateApplicationVersionRequestTranscriberConfig = None,
        version_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.business_unit_id = business_unit_id
        self.interaction_config = interaction_config
        # This parameter is required.
        self.script_profile = script_profile
        self.synthesizer_config = synthesizer_config
        self.transcriber_config = transcriber_config
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        if self.interaction_config:
            self.interaction_config.validate()
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.business_unit_id is not None:
            result['BusinessUnitId'] = self.business_unit_id

        if self.interaction_config is not None:
            result['InteractionConfig'] = self.interaction_config.to_map()

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
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('BusinessUnitId') is not None:
            self.business_unit_id = m.get('BusinessUnitId')

        if m.get('InteractionConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestInteractionConfig()
            self.interaction_config = temp_model.from_map(m.get('InteractionConfig'))

        if m.get('ScriptProfile') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestScriptProfile()
            self.script_profile = temp_model.from_map(m.get('ScriptProfile'))

        if m.get('SynthesizerConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestSynthesizerConfig()
            self.synthesizer_config = temp_model.from_map(m.get('SynthesizerConfig'))

        if m.get('TranscriberConfig') is not None:
            temp_model = main_models.UpdateApplicationVersionRequestTranscriberConfig()
            self.transcriber_config = temp_model.from_map(m.get('TranscriberConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class UpdateApplicationVersionRequestTranscriberConfig(DaraModel):
    def __init__(
        self,
        nls_access_type: str = None,
        nls_engine: str = None,
    ):
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        return self

class UpdateApplicationVersionRequestSynthesizerConfig(DaraModel):
    def __init__(
        self,
        nls_access_type: str = None,
        nls_engine: str = None,
        pitch_rate: int = None,
        speech_rate: int = None,
        voice: str = None,
        volume: int = None,
    ):
        self.nls_access_type = nls_access_type
        self.nls_engine = nls_engine
        self.pitch_rate = pitch_rate
        self.speech_rate = speech_rate
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nls_access_type is not None:
            result['NlsAccessType'] = self.nls_access_type

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NlsAccessType') is not None:
            self.nls_access_type = m.get('NlsAccessType')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

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

