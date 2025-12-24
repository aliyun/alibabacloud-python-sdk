# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class UpdateCasterSceneAudioRequest(DaraModel):
    def __init__(
        self,
        audio_layer: List[main_models.UpdateCasterSceneAudioRequestAudioLayer] = None,
        caster_id: str = None,
        follow_enable: int = None,
        mix_list: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        scene_id: str = None,
    ):
        # The audio configurations.
        self.audio_layer = audio_layer
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The audio mode. By default, the AFV mode is used. If you do not specify this parameter, the scene retains the last configuration. Valid values:
        # 
        # *   **0**: the audio mixing mode.
        # *   **1**: the AFV mode.
        self.follow_enable = follow_enable
        # The location IDs of the audio layers, which are in the same order as the audio layers.
        self.mix_list = mix_list
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the scene. If you call the [DescribeCasterScenes](https://help.aliyun.com/document_detail/2848039.html) operation to query scenes of the production studio, check the value of the response parameter ComponentId to obtain the ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id

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

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.follow_enable is not None:
            result['FollowEnable'] = self.follow_enable

        if self.mix_list is not None:
            result['MixList'] = self.mix_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_layer = []
        if m.get('AudioLayer') is not None:
            for k1 in m.get('AudioLayer'):
                temp_model = main_models.UpdateCasterSceneAudioRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k1))

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('FollowEnable') is not None:
            self.follow_enable = m.get('FollowEnable')

        if m.get('MixList') is not None:
            self.mix_list = m.get('MixList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

class UpdateCasterSceneAudioRequestAudioLayer(DaraModel):
    def __init__(
        self,
        filter: str = None,
        fixed_delay_duration: int = None,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # Specifies whether to enable the features provided by the audio 3A algorithms. This parameter consists of the following fields:
        # 
        # *   **enableAgc**: specifies whether to enable automatic gain control (AGC). This field is optional. Valid values: 0 and 1. **0** is the default value, which specifies that AGC is disabled. **1** specifies that AGC is enabled.
        # *   **enableAns**: specifies whether to enable active noise suppression (ANS). This field is optional. Valid values: 0 and 1. **0** is the default value, which specifies that ANS is disabled. **1** specifies that ANS is enabled.
        # *   **ansMode**: specifies the mode for ANS. This field is optional and takes effect only if you set **enableAns** to **1**. Valid values: 0 and 1. **0** is the default value, which specifies the speech noise reduction mode. **1** specifies the music noise reduction mode.
        # 
        # >  To ensure a better noise reduction effect, we recommend that you set ansMode to 1.
        # 
        # *   **enableBeautify**: specifies whether to enable voice change. This field is optional. Valid values: 0 and 1. **0** is the default value, which specifies that voice change is disabled. **1** specifies that voice change is enabled.
        # *   **voiceBeautifyMode**: specifies the mode for voice change. This field is optional and takes effect only if you set **enableBeautify** to **1**. Valid values: 0 and 1. **0** is the default value, which specifies the magnetic male voice mode. **1** specifies the fresh female voice mode.
        self.filter = filter
        # The fixed delay of the audio layer. This parameter is used to synchronize the audio with subtitles.
        # 
        # Unit: milliseconds. Valid values: **0 to 5000**. Default value: **0**.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channels that are used for volume input in the audio layer. Valid values:
        # 
        # *   **leftChannel**: the left channel
        # *   **rightChannel**: the right channel
        # *   **all** (default): both the left and right channels
        self.valid_channel = valid_channel
        # The multiple of the original volume at which the audio layer plays audio. Valid values: **0 to 10.0**. Default value: **1.0**.
        # 
        # *   **1.0**: specifies that the audio layer plays audio at the original volume.
        # *   A value smaller than **1**: specifies that the audio layer plays audio at a volume that is less than the original volume.
        # *   A value greater than **1**: specifies that the audio layer plays audio at a volume that is more than the original volume.
        self.volume_rate = volume_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.fixed_delay_duration is not None:
            result['FixedDelayDuration'] = self.fixed_delay_duration

        if self.valid_channel is not None:
            result['ValidChannel'] = self.valid_channel

        if self.volume_rate is not None:
            result['VolumeRate'] = self.volume_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('FixedDelayDuration') is not None:
            self.fixed_delay_duration = m.get('FixedDelayDuration')

        if m.get('ValidChannel') is not None:
            self.valid_channel = m.get('ValidChannel')

        if m.get('VolumeRate') is not None:
            self.volume_rate = m.get('VolumeRate')

        return self

