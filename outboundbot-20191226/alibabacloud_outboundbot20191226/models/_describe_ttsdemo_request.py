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
        sample_rate: int = None,
        script_id: str = None,
        secret_key: str = None,
        speech_rate: int = None,
        text: str = None,
        voice: str = None,
        volume: int = None,
    ):
        # The AccessKey ID of the namespace.
        # > When the engine is xunfei, you must enter the AccessKey ID.
        self.access_key = access_key
        # The Alibaba Cloud custom voice, which is the voice invocation ID.
        self.ali_customized_voice = ali_customized_voice
        # The speech service type. 
        # 
        # - When **ali** is used as the custom service, this field stores the appKey of the interactive voice response product project.
        # 
        # - When **xunfei** is used as the custom service provider, this field stores the corresponding appKey.
        self.app_key = app_key
        # The storage engine. Valid values: **ali**, **volc**, and **xunfei**.
        # 
        # - To use traditional voices, CosyVoice, or Alibaba Cloud as the custom service, enter **ali**.
        # - To use the doubao service, enter **volc**.
        # - To use xunfei as the service provider, enter **xunfei**. This option is only available for small model scenarios.
        # - To use a self-managed service, enter **dock** and set NlsServiceType to Authorized.
        # - To use CV-v3-flash and Qwen voices, enter **bailian**.
        self.engine = engine
        # The extended parameters. When Engine is set to **dock**, you must enter the configuration ID.
        self.ext_params = ext_params
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The service type.
        # Managed: the default service (public service) for the outbound robot product.
        # Authorized: the interactive voice response service purchased by public cloud customers (custom service). You can configure it in system administration > Third-party Speech Configuration.
        # 
        # > When you need to use Alibaba Cloud interactive voice response, that is, when you use Alibaba Cloud as the custom service provider, you must enter Authorized.
        self.nls_service_type = nls_service_type
        # The intonation.
        self.pitch_rate = pitch_rate
        # The sample rate.
        self.sample_rate = sample_rate
        # The scenario ID.
        self.script_id = script_id
        # The AccessKey secret of the namespace.
        # 
        # > When the engine is xunfei, you must enter the AccessKey secret.
        self.secret_key = secret_key
        # The speech rate.
        # Valid values: integers from -500 to 500. Default value: 0.
        # 
        # A value greater than 0 increases the pitch.
        # 
        # A value less than 0 decreases the pitch.
        self.speech_rate = speech_rate
        # The text content.
        # 
        # This parameter is required.
        self.text = text
        # The voice information, such as aixia, siyue, or xiaoyun. For the complete list of voices, refer to the voice list below.
        # 
        # > Because the Voice value for cloned voices is not fixed and is generated during voice cloning, a specific Voice value cannot be provided at this stage. You must obtain the specific Voice ID from the ListVoiceClone request on the voice cloning page.
        self.voice = voice
        # The volume.
        # Valid values: integers from 0 to 100. Default value: 50.
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

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

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

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

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

