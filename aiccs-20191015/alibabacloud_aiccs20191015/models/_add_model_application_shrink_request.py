# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddModelApplicationShrinkRequest(DaraModel):
    def __init__(
        self,
        application_cps: int = None,
        application_name: str = None,
        call_connected_trigger_model: bool = None,
        dyvms_scene_name: str = None,
        model_code: str = None,
        model_version: str = None,
        mute_active: bool = None,
        mute_duration: int = None,
        mute_hangup_num: int = None,
        owner_id: int = None,
        prompt: str = None,
        qualification_id: int = None,
        qualification_name: str = None,
        recording_file: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        source: str = None,
        speech_content: str = None,
        speech_id: int = None,
        start_word: str = None,
        start_word_type: int = None,
        tts_config_shrink: str = None,
        usage_desc: str = None,
    ):
        # The number of concurrent requests per second (CPS).
        # 
        # This parameter is required.
        self.application_cps = application_cps
        # The name of the model application.
        # 
        # This parameter is required.
        self.application_name = application_name
        # Specifies whether to push an event notification when a call is connected. The default value is false.
        self.call_connected_trigger_model = call_connected_trigger_model
        # The scene name.
        self.dyvms_scene_name = dyvms_scene_name
        # The model code.
        # 
        # This parameter is required.
        self.model_code = model_code
        # The model version.
        self.model_version = model_version
        # Specifies whether the first mute event triggers the model.
        self.mute_active = mute_active
        # The mute duration.
        self.mute_duration = mute_duration
        # The number of consecutive mute events that trigger an automatic hang-up.
        self.mute_hangup_num = mute_hangup_num
        self.owner_id = owner_id
        # The prompt.
        self.prompt = prompt
        # The qualification ID.
        self.qualification_id = qualification_id
        # The name of the qualification.
        self.qualification_name = qualification_name
        # The URL of the audio file for the opening line. This parameter is required if `StartWordType` is set to `1`.
        self.recording_file = recording_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source. The value must be `USER`.
        self.source = source
        # The speech script content.
        self.speech_content = speech_content
        # The speech script ID.
        self.speech_id = speech_id
        # The opening line.
        # 
        # This parameter is required.
        self.start_word = start_word
        # The type of the opening line.
        self.start_word_type = start_word_type
        # The TTS configuration, including voice, volume, speech speed, and more.
        # 
        # This parameter is required.
        self.tts_config_shrink = tts_config_shrink
        # The purpose of the application.
        self.usage_desc = usage_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_cps is not None:
            result['ApplicationCps'] = self.application_cps

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.call_connected_trigger_model is not None:
            result['CallConnectedTriggerModel'] = self.call_connected_trigger_model

        if self.dyvms_scene_name is not None:
            result['DyvmsSceneName'] = self.dyvms_scene_name

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.mute_active is not None:
            result['MuteActive'] = self.mute_active

        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration

        if self.mute_hangup_num is not None:
            result['MuteHangupNum'] = self.mute_hangup_num

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.qualification_name is not None:
            result['QualificationName'] = self.qualification_name

        if self.recording_file is not None:
            result['RecordingFile'] = self.recording_file

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source is not None:
            result['Source'] = self.source

        if self.speech_content is not None:
            result['SpeechContent'] = self.speech_content

        if self.speech_id is not None:
            result['SpeechId'] = self.speech_id

        if self.start_word is not None:
            result['StartWord'] = self.start_word

        if self.start_word_type is not None:
            result['StartWordType'] = self.start_word_type

        if self.tts_config_shrink is not None:
            result['TtsConfig'] = self.tts_config_shrink

        if self.usage_desc is not None:
            result['UsageDesc'] = self.usage_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCps') is not None:
            self.application_cps = m.get('ApplicationCps')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CallConnectedTriggerModel') is not None:
            self.call_connected_trigger_model = m.get('CallConnectedTriggerModel')

        if m.get('DyvmsSceneName') is not None:
            self.dyvms_scene_name = m.get('DyvmsSceneName')

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('MuteActive') is not None:
            self.mute_active = m.get('MuteActive')

        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')

        if m.get('MuteHangupNum') is not None:
            self.mute_hangup_num = m.get('MuteHangupNum')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('QualificationName') is not None:
            self.qualification_name = m.get('QualificationName')

        if m.get('RecordingFile') is not None:
            self.recording_file = m.get('RecordingFile')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpeechContent') is not None:
            self.speech_content = m.get('SpeechContent')

        if m.get('SpeechId') is not None:
            self.speech_id = m.get('SpeechId')

        if m.get('StartWord') is not None:
            self.start_word = m.get('StartWord')

        if m.get('StartWordType') is not None:
            self.start_word_type = m.get('StartWordType')

        if m.get('TtsConfig') is not None:
            self.tts_config_shrink = m.get('TtsConfig')

        if m.get('UsageDesc') is not None:
            self.usage_desc = m.get('UsageDesc')

        return self

