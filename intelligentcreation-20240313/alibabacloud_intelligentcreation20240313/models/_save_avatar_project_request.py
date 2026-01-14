# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class SaveAvatarProjectRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        bit_rate: str = None,
        frame_rate: str = None,
        frames: List[main_models.SaveAvatarProjectRequestFrames] = None,
        operate_type: str = None,
        project_id: str = None,
        project_name: str = None,
        res_spec_type: str = None,
        resolution: str = None,
        scale_type: str = None,
        script_model_tag: str = None,
        synchronized_display: str = None,
    ):
        self.agent_id = agent_id
        self.bit_rate = bit_rate
        self.frame_rate = frame_rate
        self.frames = frames
        self.operate_type = operate_type
        self.project_id = project_id
        self.project_name = project_name
        self.res_spec_type = res_spec_type
        self.resolution = resolution
        self.scale_type = scale_type
        self.script_model_tag = script_model_tag
        self.synchronized_display = synchronized_display

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
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.bit_rate is not None:
            result['bitRate'] = self.bit_rate

        if self.frame_rate is not None:
            result['frameRate'] = self.frame_rate

        result['frames'] = []
        if self.frames is not None:
            for k1 in self.frames:
                result['frames'].append(k1.to_map() if k1 else None)

        if self.operate_type is not None:
            result['operateType'] = self.operate_type

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.res_spec_type is not None:
            result['resSpecType'] = self.res_spec_type

        if self.resolution is not None:
            result['resolution'] = self.resolution

        if self.scale_type is not None:
            result['scaleType'] = self.scale_type

        if self.script_model_tag is not None:
            result['scriptModelTag'] = self.script_model_tag

        if self.synchronized_display is not None:
            result['synchronizedDisplay'] = self.synchronized_display

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('bitRate') is not None:
            self.bit_rate = m.get('bitRate')

        if m.get('frameRate') is not None:
            self.frame_rate = m.get('frameRate')

        self.frames = []
        if m.get('frames') is not None:
            for k1 in m.get('frames'):
                temp_model = main_models.SaveAvatarProjectRequestFrames()
                self.frames.append(temp_model.from_map(k1))

        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('resSpecType') is not None:
            self.res_spec_type = m.get('resSpecType')

        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')

        if m.get('scaleType') is not None:
            self.scale_type = m.get('scaleType')

        if m.get('scriptModelTag') is not None:
            self.script_model_tag = m.get('scriptModelTag')

        if m.get('synchronizedDisplay') is not None:
            self.synchronized_display = m.get('synchronizedDisplay')

        return self

class SaveAvatarProjectRequestFrames(DaraModel):
    def __init__(
        self,
        index: int = None,
        layers: List[main_models.SaveAvatarProjectRequestFramesLayers] = None,
        video_script: main_models.SaveAvatarProjectRequestFramesVideoScript = None,
    ):
        self.index = index
        self.layers = layers
        self.video_script = video_script

    def validate(self):
        if self.layers:
            for v1 in self.layers:
                 if v1:
                    v1.validate()
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
                temp_model = main_models.SaveAvatarProjectRequestFramesLayers()
                self.layers.append(temp_model.from_map(k1))

        if m.get('videoScript') is not None:
            temp_model = main_models.SaveAvatarProjectRequestFramesVideoScript()
            self.video_script = temp_model.from_map(m.get('videoScript'))

        return self

class SaveAvatarProjectRequestFramesVideoScript(DaraModel):
    def __init__(
        self,
        emotion: str = None,
        pitch_rate: str = None,
        speed_rate: str = None,
        text_content: str = None,
        voice_language: str = None,
        voice_template_id: str = None,
        volume: str = None,
    ):
        self.emotion = emotion
        self.pitch_rate = pitch_rate
        self.speed_rate = speed_rate
        self.text_content = text_content
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
        if self.emotion is not None:
            result['emotion'] = self.emotion

        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate

        if self.speed_rate is not None:
            result['speedRate'] = self.speed_rate

        if self.text_content is not None:
            result['textContent'] = self.text_content

        if self.voice_language is not None:
            result['voiceLanguage'] = self.voice_language

        if self.voice_template_id is not None:
            result['voiceTemplateId'] = self.voice_template_id

        if self.volume is not None:
            result['volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emotion') is not None:
            self.emotion = m.get('emotion')

        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')

        if m.get('speedRate') is not None:
            self.speed_rate = m.get('speedRate')

        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')

        if m.get('voiceLanguage') is not None:
            self.voice_language = m.get('voiceLanguage')

        if m.get('voiceTemplateId') is not None:
            self.voice_template_id = m.get('voiceTemplateId')

        if m.get('volume') is not None:
            self.volume = m.get('volume')

        return self

class SaveAvatarProjectRequestFramesLayers(DaraModel):
    def __init__(
        self,
        height: int = None,
        index: int = None,
        material: main_models.SaveAvatarProjectRequestFramesLayersMaterial = None,
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
            temp_model = main_models.SaveAvatarProjectRequestFramesLayersMaterial()
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

class SaveAvatarProjectRequestFramesLayersMaterial(DaraModel):
    def __init__(
        self,
        format: str = None,
        id: str = None,
        url: str = None,
    ):
        self.format = format
        self.id = id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['format'] = self.format

        if self.id is not None:
            result['id'] = self.id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

