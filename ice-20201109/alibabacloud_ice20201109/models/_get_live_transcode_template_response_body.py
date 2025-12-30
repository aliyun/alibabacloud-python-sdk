# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetLiveTranscodeTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_content: main_models.GetLiveTranscodeTemplateResponseBodyTemplateContent = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The content of the template.
        self.template_content = template_content

    def validate(self):
        if self.template_content:
            self.template_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateContent') is not None:
            temp_model = main_models.GetLiveTranscodeTemplateResponseBodyTemplateContent()
            self.template_content = temp_model.from_map(m.get('TemplateContent'))

        return self

class GetLiveTranscodeTemplateResponseBodyTemplateContent(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        name: str = None,
        template_config: main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfig = None,
        template_id: str = None,
        type: str = None,
    ):
        # The category of the template. Valid values:
        # 
        # *   system
        # *   customized
        self.category = category
        # The time when the template was created.
        self.create_time = create_time
        # The name of the template.
        self.name = name
        # The configuration of the template.
        self.template_config = template_config
        # The template ID.
        self.template_id = template_id
        # The type of the template.
        self.type = type

    def validate(self):
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfig(DaraModel):
    def __init__(
        self,
        audio_params: main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigAudioParams = None,
        video_params: main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigVideoParams = None,
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
            temp_model = main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigAudioParams()
            self.audio_params = temp_model.from_map(m.get('AudioParams'))

        if m.get('VideoParams') is not None:
            temp_model = main_models.GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigVideoParams()
            self.video_params = temp_model.from_map(m.get('VideoParams'))

        return self

class GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigVideoParams(DaraModel):
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
        # The bitrate of the output video.
        self.bitrate = bitrate
        # The encoding type.
        self.codec = codec
        # The frame rate of the output video.
        self.fps = fps
        # The group of pictures (GOP) of the output video.
        self.gop = gop
        # The height of the output video.
        self.height = height
        # The encoding profile.
        self.profile = profile
        # The width of the output video.
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

class GetLiveTranscodeTemplateResponseBodyTemplateContentTemplateConfigAudioParams(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        samplerate: str = None,
    ):
        # The bitrate of the output audio.
        self.bitrate = bitrate
        # The number of sound channels.
        self.channels = channels
        # The audio codec.
        self.codec = codec
        # The audio codec profile.
        self.profile = profile
        # The audio sampling rate.
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

