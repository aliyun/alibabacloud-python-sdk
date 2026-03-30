# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class CreateVoiceAccessProfileRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        nls_engine: str = None,
        profile: main_models.CreateVoiceAccessProfileRequestProfile = None,
    ):
        self.instance_id = instance_id
        self.nls_engine = nls_engine
        self.profile = profile

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('Profile') is not None:
            temp_model = main_models.CreateVoiceAccessProfileRequestProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        return self

class CreateVoiceAccessProfileRequestProfile(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        api_key: str = None,
        api_secret: str = None,
        app_id: str = None,
        app_key: str = None,
        asr_app_key: str = None,
        tts_api_key: str = None,
    ):
        self.access_key = access_key
        self.api_key = api_key
        self.api_secret = api_secret
        self.app_id = app_id
        self.app_key = app_key
        self.asr_app_key = asr_app_key
        self.tts_api_key = tts_api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_secret is not None:
            result['ApiSecret'] = self.api_secret

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.asr_app_key is not None:
            result['AsrAppKey'] = self.asr_app_key

        if self.tts_api_key is not None:
            result['TtsApiKey'] = self.tts_api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiSecret') is not None:
            self.api_secret = m.get('ApiSecret')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AsrAppKey') is not None:
            self.asr_app_key = m.get('AsrAppKey')

        if m.get('TtsApiKey') is not None:
            self.tts_api_key = m.get('TtsApiKey')

        return self

