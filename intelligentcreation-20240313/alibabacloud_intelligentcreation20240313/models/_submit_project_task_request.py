# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class SubmitProjectTaskRequest(DaraModel):
    def __init__(
        self,
        frames: List[main_models.SubmitProjectTaskRequestFrames] = None,
        scale_type: str = None,
        subtitle_tag: int = None,
        transparent_background: int = None,
    ):
        # frame
        self.frames = frames
        self.scale_type = scale_type
        self.subtitle_tag = subtitle_tag
        self.transparent_background = transparent_background

    def validate(self):
        if self.frames:
            for v1 in self.frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['frames'] = []
        if self.frames is not None:
            for k1 in self.frames:
                result['frames'].append(k1.to_map() if k1 else None)

        if self.scale_type is not None:
            result['scaleType'] = self.scale_type

        if self.subtitle_tag is not None:
            result['subtitleTag'] = self.subtitle_tag

        if self.transparent_background is not None:
            result['transparentBackground'] = self.transparent_background

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frames = []
        if m.get('frames') is not None:
            for k1 in m.get('frames'):
                temp_model = main_models.SubmitProjectTaskRequestFrames()
                self.frames.append(temp_model.from_map(k1))

        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')

        if m.get('subtitleTag') is not None:
            self.subtitle_tag = m.get('subtitleTag')

        if m.get('transparentBackground') is not None:
            self.transparent_background = m.get('transparentBackground')

        return self

class SubmitProjectTaskRequestFrames(DaraModel):
    def __init__(
        self,
        index: int = None,
        layers: List[main_models.SubmitProjectTaskRequestFramesLayers] = None,
        subtitle: main_models.SubmitProjectTaskRequestFramesSubtitle = None,
        video_script: main_models.SubmitProjectTaskRequestFramesVideoScript = None,
    ):
        self.index = index
        self.layers = layers
        self.subtitle = subtitle
        self.video_script = video_script

    def validate(self):
        if self.layers:
            for v1 in self.layers:
                 if v1:
                    v1.validate()
        if self.subtitle:
            self.subtitle.validate()
        if self.video_script:
            self.video_script.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        result['layers'] = []
        if self.layers is not None:
            for k1 in self.layers:
                result['layers'].append(k1.to_map() if k1 else None)

        if self.subtitle is not None:
            result['subtitle'] = self.subtitle.to_map()

        if self.video_script is not None:
            result['videoScript'] = self.video_script.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        self.layers = []
        if m.get('layers') is not None:
            for k1 in m.get('layers'):
                temp_model = main_models.SubmitProjectTaskRequestFramesLayers()
                self.layers.append(temp_model.from_map(k1))

        if m.get('subtitle') is not None:
            temp_model = main_models.SubmitProjectTaskRequestFramesSubtitle()
            self.subtitle = temp_model.from_map(m.get('subtitle'))

        if m.get('videoScript') is not None:
            temp_model = main_models.SubmitProjectTaskRequestFramesVideoScript()
            self.video_script = temp_model.from_map(m.get('videoScript'))

        return self

class SubmitProjectTaskRequestFramesVideoScript(DaraModel):
    def __init__(
        self,
        audio_url: str = None,
        emotion: str = None,
        pitch_rate: str = None,
        speech_open: bool = None,
        speed_rate: str = None,
        text_content: str = None,
        type: str = None,
        voice_language: str = None,
        voice_template_id: int = None,
        volume: int = None,
    ):
        self.audio_url = audio_url
        self.emotion = emotion
        self.pitch_rate = pitch_rate
        self.speech_open = speech_open
        self.speed_rate = speed_rate
        self.text_content = text_content
        self.type = type
        self.voice_language = voice_language
        self.voice_template_id = voice_template_id
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_url is not None:
            result['audioUrl'] = self.audio_url

        if self.emotion is not None:
            result['emotion'] = self.emotion

        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate

        if self.speech_open is not None:
            result['speechOpen'] = self.speech_open

        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate

        if self.text_content is not None:
            result['textContent'] = self.text_content

        if self.type is not None:
            result['type'] = self.type

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioUrl') is not None:
            self.audio_url = m.get('audioUrl')

        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')

        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')

        if m.get('speechOpen') is not None:
            self.speech_open = m.get('speechOpen')

        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')

        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceTemplateId') is not None:
            self.voice_template_id = m.get('voiceTemplateId')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

class SubmitProjectTaskRequestFramesSubtitle(DaraModel):
    def __init__(
        self,
        alignment: str = None,
        background_color: str = None,
        font: str = None,
        font_color: str = None,
        font_size: int = None,
        max_char_length: int = None,
        position_x: int = None,
        position_y: int = None,
        text_height: int = None,
        text_width: int = None,
    ):
        self.alignment = alignment
        self.background_color = background_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.max_char_length = max_char_length
        self.position_x = position_x
        self.position_y = position_y
        self.text_height = text_height
        self.text_width = text_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alignment is not None:
            result['alignment'] = self.alignment

        if self.background_color is not None:
            result['backgroundColor'] = self.background_color

        if self.font is not None:
            result['font'] = self.font

        if self.font_color is not None:
            result['fontColor'] = self.font_color

        if self.font_size is not None:
            result['fontSize'] = self.font_size

        if self.max_char_length is not None:
            result['maxCharLength'] = self.max_char_length

        if self.position_x is not None:
            result['positionX'] = self.position_x

        if self.position_y is not None:
            result['positionY'] = self.position_y

        if self.text_height is not None:
            result['textHeight'] = self.text_height

        if self.text_width is not None:
            result['textWidth'] = self.text_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignment') is not None:
            self.alignment = m.get('alignment')

        if m.get('backgroundColor') is not None:
            self.background_color = m.get('backgroundColor')

        if m.get('font') is not None:
            self.font = m.get('font')

        if m.get('fontColor') is not None:
            self.font_color = m.get('fontColor')

        if m.get('fontSize') is not None:
            self.font_size = m.get('fontSize')

        if m.get('maxCharLength') is not None:
            self.max_char_length = m.get('maxCharLength')

        if m.get('positionX') is not None:
            self.position_x = m.get('positionX')

        if m.get('positionY') is not None:
            self.position_y = m.get('positionY')

        if m.get('textHeight') is not None:
            self.text_height = m.get('textHeight')

        if m.get('textWidth') is not None:
            self.text_width = m.get('textWidth')

        return self

class SubmitProjectTaskRequestFramesLayers(DaraModel):
    def __init__(
        self,
        height: int = None,
        index: int = None,
        material: main_models.SubmitProjectTaskRequestFramesLayersMaterial = None,
        position_x: int = None,
        position_y: int = None,
        type: str = None,
        width: int = None,
    ):
        self.height = height
        self.index = index
        self.material = material
        self.position_x = position_x
        self.position_y = position_y
        self.type = type
        self.width = width

    def validate(self):
        if self.material:
            self.material.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['height'] = self.height

        if self.index is not None:
            result['index'] = self.index

        if self.material is not None:
            result['material'] = self.material.to_map()

        if self.position_x is not None:
            result['positionX'] = self.position_x

        if self.position_y is not None:
            result['positionY'] = self.position_y

        if self.type is not None:
            result['type'] = self.type

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('material') is not None:
            temp_model = main_models.SubmitProjectTaskRequestFramesLayersMaterial()
            self.material = temp_model.from_map(m.get('material'))

        if m.get('positionX') is not None:
            self.position_x = m.get('positionX')

        if m.get('positionY') is not None:
            self.position_y = m.get('positionY')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class SubmitProjectTaskRequestFramesLayersMaterial(DaraModel):
    def __init__(
        self,
        anchor_style_level: str = None,
        format: str = None,
        id: str = None,
        mask: main_models.SubmitProjectTaskRequestFramesLayersMaterialMask = None,
        speed: str = None,
        url: str = None,
        volume: int = None,
    ):
        self.anchor_style_level = anchor_style_level
        self.format = format
        self.id = id
        self.mask = mask
        self.speed = speed
        self.url = url
        self.volume = volume

    def validate(self):
        if self.mask:
            self.mask.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_style_level is not None:
            result['anchorStyleLevel'] = self.anchor_style_level

        if self.format is not None:
            result['format'] = self.format

        if self.id is not None:
            result['id'] = self.id

        if self.mask is not None:
            result['mask'] = self.mask.to_map()

        if self.speed is not None:
            result['speed'] = self.speed

        if self.url is not None:
            result['url'] = self.url

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorStyleLevel') is not None:
            self.anchor_style_level = m.get('anchorStyleLevel')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('mask') is not None:
            temp_model = main_models.SubmitProjectTaskRequestFramesLayersMaterialMask()
            self.mask = temp_model.from_map(m.get('mask'))

        if m.get('speed') is not None:
            self.speed = m.get('speed')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

class SubmitProjectTaskRequestFramesLayersMaterialMask(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

