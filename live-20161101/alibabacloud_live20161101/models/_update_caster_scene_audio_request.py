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
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, you can obtain the ID from the CasterId parameter in the response.
        # 
        # - If you create a production studio in the LIVE console, go to the **LIVE Console** > **Production Studio** > **Cloud Production Studio** page to view the ID.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the ID of the production studio.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # Specifies whether to enable the AFV mode. If you leave this parameter empty, the last configuration is retained. Valid values:
        # 
        # - **0**: audio mixing mode.
        # 
        # - **1**: audio-follows-video mode.
        self.follow_enable = follow_enable
        # The list of associated location IDs. The order of the location IDs must be the same as the order of the audio layers.
        self.mix_list = mix_list
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the scene. If you query the list of scenes in a production studio by calling the [DescribeCasterScenes](https://help.aliyun.com/document_detail/2848039.html) operation, you can obtain the ID from the ComponentId parameter in the response.
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
        # Specifies whether to enable the features provided by the 3A audio algorithm. This parameter consists of the following fields:
        # 
        # - **enableAgc**: (Optional) Specifies whether to enable the automatic gain control (AGC) feature of the 3A algorithm. Valid values: **0** (disabled, default) and **1** (enabled).
        # 
        # - **enableAns**: (Optional) Specifies whether to enable the intelligent noise reduction feature of the 3A algorithm. Valid values: **0** (disabled, default) and **1** (enabled).
        # 
        # - **ansMode**: (Optional) The mode of the intelligent noise reduction feature. This field is active only when **enableAns** is set to **1**. Valid values: **0** (speech noise reduction, default) and **1** (music noise reduction).
        # 
        # > For better noise reduction, set ansMode to 1.
        # 
        # - **enableBeautify**: (Optional) Specifies whether to enable voice beautification. Valid values: **0** (disabled, default) and **1** (enabled).
        # 
        # - **voiceBeautifyMode**: (Optional) The voice beautification mode. This field is active only when **enableBeautify** is set to **1**. Valid values: **0** (magnetic male voice, default) and **1** (fresh female voice).
        self.filter = filter
        # The fixed latency of the audio layer. This parameter is used to synchronize the audio with captions.
        # 
        # Unit: milliseconds. Valid values: 0 to **5000**. Default value: **0**.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channels that are used for volume input. Valid values:
        # 
        # - **leftChannel**: the left sound channel.
        # 
        # - **rightChannel**: the right sound channel.
        # 
        # - **all** (default): both sound channels.
        self.valid_channel = valid_channel
        # The volume multiplier for the audio stream. Valid values: 0 to **10.0**. Default value: **1.0**.
        # 
        # - **1.0**: The original volume is used.
        # 
        # - A value less than **1** decreases the volume.
        # 
        # - A value greater than **1** increases the volume.
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

