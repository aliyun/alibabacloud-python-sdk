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
        # 应用并发请求数
        # 
        # This parameter is required.
        self.application_cps = application_cps
        # 模型应用名称
        # 
        # This parameter is required.
        self.application_name = application_name
        self.call_connected_trigger_model = call_connected_trigger_model
        # 场景名称
        self.dyvms_scene_name = dyvms_scene_name
        # 模型编码
        # 
        # This parameter is required.
        self.model_code = model_code
        # 模型版本
        self.model_version = model_version
        # 第一个静音是否唤起模型
        self.mute_active = mute_active
        # 静音时长
        self.mute_duration = mute_duration
        # 连续多少个静音事件主动挂机
        self.mute_hangup_num = mute_hangup_num
        self.owner_id = owner_id
        # 提示词
        self.prompt = prompt
        # 资质ID
        self.qualification_id = qualification_id
        # 资质名称
        self.qualification_name = qualification_name
        self.recording_file = recording_file
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 来源
        self.source = source
        # 话术内容
        self.speech_content = speech_content
        # 话束id
        self.speech_id = speech_id
        # 开场白
        # 
        # This parameter is required.
        self.start_word = start_word
        self.start_word_type = start_word_type
        # tts配置，包括音色、音量、音速等。
        # 
        # This parameter is required.
        self.tts_config_shrink = tts_config_shrink
        # 用途
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

