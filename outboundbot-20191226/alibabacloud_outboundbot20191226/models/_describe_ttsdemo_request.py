# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTTSDemoRequest(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        ali_customized_voice: str = None,
        app_key: str = None,
        engine: str = None,
        ext_params: str = None,
        instance_id: str = None,
        nls_service_type: str = None,
        pitch_rate: int = None,
        script_id: str = None,
        secret_key: str = None,
        speech_rate: int = None,
        text: str = None,
        voice: str = None,
        volume: int = None,
    ):
        # The AccessKey (AK) of the namespace.
        # > When the engine is xunfei, enter the AK here.
        self.access_key = access_key
        # The Alibaba Cloud custom voice, which is the voice invocation ID.
        self.ali_customized_voice = ali_customized_voice
        # The speech service type.
        # 
        # - When you use **ali** as the custom service, this field stores the appKey of the interactive voice response product project.
        # 
        # - When you use **xunfei** as the custom service provider, this field stores the corresponding appKey.
        self.app_key = app_key
        # The storage engine. Valid values: ali, volc, xunfei.
        # 
        # - When using traditional voices, CosyVoice, or selecting Alibaba Cloud as the custom service, set this to **ali**.
        # - When using the doubao service, set this to **volc**.
        # - When using xunfei as the service provider, set this to **xunfei** (can only be used in small model scenarios).
        # - When using your own service, set this to **dock**, and set NlsServiceType to Authorized.
        # - When using CV-v3-flash and Qwen voices, set this to **bailian**.
        self.engine = engine
        # The extended parameter. When Engine is set to **dock**, enter the configuration ID.
        self.ext_params = ext_params
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The service type.
        # Managed: the default service (public service) of the outbound robot product.
        # Authorized: the interactive voice response service purchased by the public cloud customer (custom service), configured through system administration > Third-party Voice Configuration.
        # 
        # > When using Alibaba Cloud interactive voice response as the custom service provider, set this to Authorized.
        self.nls_service_type = nls_service_type
        # The pitch.
        self.pitch_rate = pitch_rate
        # The scenario ID.
        self.script_id = script_id
        # The AccessKey Secret (SK) of the namespace.
        # 
        # > When the engine is xunfei, enter the SK here.
        self.secret_key = secret_key
        # The speech rate. The value is an integer in the range of [-500, 500]. Default value: 0.
        # 
        # A value greater than 0 increases the pitch.
        # 
        # A value less than 0 decreases the pitch.
        self.speech_rate = speech_rate
        # The text content.
        # 
        # This parameter is required.
        self.text = text
        # The voice information, such as aixia, siyue, or xiaoyun. For the complete list of available voices, refer to the voice list below.
        # 
        # > Because the Voice value for cloned voices is a non-fixed value generated during voice cloning, a specific Voice value cannot be provided at this stage. You can obtain the specific VoiceID from the voice cloning page by calling the ListVoiceClone operation.
        self.voice = voice
        # The volume. The value is an integer in the range of [0, 100]. Default value: 50.
        # 
        # A value greater than 50 increases the volume.
        # 
        # A value less than 50 decreases the volume.
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.ali_customized_voice is not None:
            result['AliCustomizedVoice'] = self.ali_customized_voice

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nls_service_type is not None:
            result['NlsServiceType'] = self.nls_service_type

        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate

        if self.text is not None:
            result['Text'] = self.text

        if self.voice is not None:
            result['Voice'] = self.voice

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AliCustomizedVoice') is not None:
            self.ali_customized_voice = m.get('AliCustomizedVoice')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NlsServiceType') is not None:
            self.nls_service_type = m.get('NlsServiceType')

        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Voice') is not None:
            self.voice = m.get('Voice')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

