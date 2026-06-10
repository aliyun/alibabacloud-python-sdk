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
        # The AccessKey (AK) for this namespace.
        # 
        # > Enter the AK when the engine is xunfei.
        self.access_key = access_key
        # Alibaba Cloud custom voice ID
        self.ali_customized_voice = ali_customized_voice
        # Speech service type
        # 
        # - When using **ali** as a custom service, enter the appKey of your Intelligent Speech Interaction project.
        # 
        # - When using **xunfei** as a custom service, enter its appKey.
        self.app_key = app_key
        # Storage engine. Choose from ali, volc, or xunfei.
        # 
        # - Enter **ali** when using the default service or Alibaba Cloud as a custom service.
        # 
        # - Enter **volc** when using the doubao service.
        # 
        # - Enter **xunfei** when using iFLYTEK as a service provider. This option is only available for small-model scenarios.
        self.engine = engine
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Service type
        # Managed: The default Intelligent Speech Interaction service for Intelligent Outbound Calling (public service).
        # Authorized: An Intelligent Speech Interaction service you purchased on Alibaba Cloud public cloud (your private service). You can grant authorization by going to Scenario Management > Edit > Call Service > Custom Service.
        # 
        # > Set this parameter to Authorized when using Alibaba Cloud\\"s Intelligent Speech Interaction as your custom service provider.
        self.nls_service_type = nls_service_type
        # Pitch. An integer between -500 and 500. Default is 0.
        # 
        # A value greater than 0 raises pitch.
        # 
        # A value less than 0 lowers pitch.
        self.pitch_rate = pitch_rate
        # Scenario ID
        self.script_id = script_id
        # The AccessKey secret (SK) for this namespace.
        # 
        # > Enter the SK when the engine is xunfei.
        self.secret_key = secret_key
        # Speech rate. An integer between -500 and 500. Default is 0.
        # 
        # A value greater than 0 increases speech speed.
        # 
        # A value less than 0 decreases speech speed.
        self.speech_rate = speech_rate
        # Text to convert to speech
        # 
        # This parameter is required.
        self.text = text
        # Voice ID. Examples include aixia, siyue, and xiaoyun. For the full list of available voices, see the voice list below.
        # 
        # > Cloned voices use dynamic Voice IDs that are generated during voice cloning. Therefore, specific Voice IDs for cloned voices are not listed here. To get a cloned voice’s Voice ID, call ListVoiceClone from the voice cloning page.
        self.voice = voice
        # Volume. An integer between 0 and 100. Default is 50.
        # 
        # A value greater than 50 increases volume.
        # 
        # A value less than 50 decreases volume.
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

