# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterSceneAudioResponseBody(DaraModel):
    def __init__(
        self,
        audio_layers: main_models.DescribeCasterSceneAudioResponseBodyAudioLayers = None,
        caster_id: str = None,
        follow_enable: int = None,
        mix_list: main_models.DescribeCasterSceneAudioResponseBodyMixList = None,
        request_id: str = None,
    ):
        # The configurations of the audio layers.
        self.audio_layers = audio_layers
        # The ID of the production studio. You can specify the ID in a request to start a scene in the production studio.
        self.caster_id = caster_id
        # The audio mode. By default, the audio follows video (AFV) mode is used. Valid values:
        # 
        # *   **0**: the audio mixing mode
        # *   **1**: the AFV mode
        self.follow_enable = follow_enable
        self.mix_list = mix_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.audio_layers:
            self.audio_layers.validate()
        if self.mix_list:
            self.mix_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_layers is not None:
            result['AudioLayers'] = self.audio_layers.to_map()

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.follow_enable is not None:
            result['FollowEnable'] = self.follow_enable

        if self.mix_list is not None:
            result['MixList'] = self.mix_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioLayers') is not None:
            temp_model = main_models.DescribeCasterSceneAudioResponseBodyAudioLayers()
            self.audio_layers = temp_model.from_map(m.get('AudioLayers'))

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('FollowEnable') is not None:
            self.follow_enable = m.get('FollowEnable')

        if m.get('MixList') is not None:
            temp_model = main_models.DescribeCasterSceneAudioResponseBodyMixList()
            self.mix_list = temp_model.from_map(m.get('MixList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCasterSceneAudioResponseBodyMixList(DaraModel):
    def __init__(
        self,
        location_id: List[str] = None,
    ):
        self.location_id = location_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location_id is not None:
            result['LocationId'] = self.location_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        return self

class DescribeCasterSceneAudioResponseBodyAudioLayers(DaraModel):
    def __init__(
        self,
        audio_layer: List[main_models.DescribeCasterSceneAudioResponseBodyAudioLayersAudioLayer] = None,
    ):
        self.audio_layer = audio_layer

    def validate(self):
        if self.audio_layer:
            for v1 in self.audio_layer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k1 in self.audio_layer:
                result['AudioLayer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_layer = []
        if m.get('AudioLayer') is not None:
            for k1 in m.get('AudioLayer'):
                temp_model = main_models.DescribeCasterSceneAudioResponseBodyAudioLayersAudioLayer()
                self.audio_layer.append(temp_model.from_map(k1))

        return self

class DescribeCasterSceneAudioResponseBodyAudioLayersAudioLayer(DaraModel):
    def __init__(
        self,
        fixed_delay_duration: int = None,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # The fixed delay of the audio layer. Unit: milliseconds.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channel type of the audio layer. Valid values:
        # 
        # *   **left**: the left channel
        # *   **right**: the right channel
        # *   **all** (default): both the left and right channels
        self.valid_channel = valid_channel
        # The volume of the audio layer.
        self.volume_rate = volume_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_delay_duration is not None:
            result['FixedDelayDuration'] = self.fixed_delay_duration

        if self.valid_channel is not None:
            result['ValidChannel'] = self.valid_channel

        if self.volume_rate is not None:
            result['VolumeRate'] = self.volume_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedDelayDuration') is not None:
            self.fixed_delay_duration = m.get('FixedDelayDuration')

        if m.get('ValidChannel') is not None:
            self.valid_channel = m.get('ValidChannel')

        if m.get('VolumeRate') is not None:
            self.volume_rate = m.get('VolumeRate')

        return self

