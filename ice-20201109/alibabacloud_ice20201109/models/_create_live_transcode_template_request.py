# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateLiveTranscodeTemplateRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        template_config: main_models.CreateLiveTranscodeTemplateRequestTemplateConfig = None,
        type: str = None,
    ):
        # The name of the template.
        # 
        # This parameter is required.
        self.name = name
        # The configuration of the template.
        self.template_config = template_config
        # The type of the template. Valid values:
        # 
        # *   normal
        # *   narrow-band
        # *   audio-only
        # *   origin
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.CreateLiveTranscodeTemplateRequestTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateLiveTranscodeTemplateRequestTemplateConfig(DaraModel):
    def __init__(
        self,
        audio_params: main_models.CreateLiveTranscodeTemplateRequestTemplateConfigAudioParams = None,
        video_params: main_models.CreateLiveTranscodeTemplateRequestTemplateConfigVideoParams = None,
    ):
        # The audio parameters.
        self.audio_params = audio_params
        # The video parameters.
        self.video_params = video_params

    def validate(self):
        if self.audio_params:
            self.audio_params.validate()
        if self.video_params:
            self.video_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_params is not None:
            result['AudioParams'] = self.audio_params.to_map()

        if self.video_params is not None:
            result['VideoParams'] = self.video_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioParams') is not None:
            temp_model = main_models.CreateLiveTranscodeTemplateRequestTemplateConfigAudioParams()
            self.audio_params = temp_model.from_map(m.get('AudioParams'))

        if m.get('VideoParams') is not None:
            temp_model = main_models.CreateLiveTranscodeTemplateRequestTemplateConfigVideoParams()
            self.video_params = temp_model.from_map(m.get('VideoParams'))

        return self

class CreateLiveTranscodeTemplateRequestTemplateConfigVideoParams(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        codec: str = None,
        fps: str = None,
        gop: str = None,
        height: str = None,
        profile: str = None,
        width: str = None,
    ):
        # The bitrate of the output video. Unit: Kbit/s. Valid values: 1 to 6000.
        self.bitrate = bitrate
        # The encoding type. Valid values:
        # 
        # *   H.264
        # *   H.265
        self.codec = codec
        # The frame rate of the output video. Unit: frames per second (FPS). Valid values: 1 to 60.
        self.fps = fps
        # The group of pictures (GOP) of the output video. Unit: frame. Valid values: 1 to 3000.
        self.gop = gop
        # The height of the output video. Valid values: Height ≥ 128 max (Height,Width) ≤ 2560 min (Height,Width) ≤ 1440
        # 
        # Note: The resolution of the output video that is transcoded by using the H.265 Narrowband HD transcoding template cannot exceed 1280 × 720 pixels.
        self.height = height
        # The encoding profile. The profile determines how a video is encoded. In most cases, a greater value indicates better image quality and higher resource consumption. Valid values: 1: baseline. This value is suitable for mobile devices. 2: main. This value is suitable for standard-definition devices. 3: high. This value is suitable for high-definition devices.
        self.profile = profile
        # The width of the output video. Valid values: Width ≥ 128 max (Height,Width) ≤ 2560 min (Height,Width) ≤ 1440
        # 
        # Note: The resolution of the output video that is transcoded by using the H.265 Narrowband HD transcoding template cannot exceed 1280 × 720 pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class CreateLiveTranscodeTemplateRequestTemplateConfigAudioParams(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        samplerate: str = None,
    ):
        # The bitrate of the output audio. Unit: Kbit/s. Valid values: 1 to 1000.
        self.bitrate = bitrate
        # The number of sound channels. Valid values: 1: mono 2: binaural
        self.channels = channels
        # The audio codec. Valid values:
        # 
        # *   AAC
        # *   MP3
        self.codec = codec
        # The audio codec profile. Valid values when the Codec parameter is set to AAC:
        # 
        # *   aac_low
        # *   aac_he
        # *   aac_he_v2
        # *   aac_ld
        self.profile = profile
        # The audio sampling rate. Valid values: 22050 to 96000.
        # 
        # Note: If you set AudioProfile to aac_ld, the audio sampling rate cannot exceed 44,100.
        self.samplerate = samplerate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        return self

