# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class AddCasterLayoutRequest(DaraModel):
    def __init__(
        self,
        audio_layer: List[main_models.AddCasterLayoutRequestAudioLayer] = None,
        blend_list: List[str] = None,
        caster_id: str = None,
        mix_list: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        video_layer: List[main_models.AddCasterLayoutRequestVideoLayer] = None,
    ):
        # The audio layouts.
        # 
        # This parameter is required.
        self.audio_layer = audio_layer
        # The location IDs of the video sources. The order of the location IDs corresponds to the order of the video layers specified in the **VideoLayer** parameter. For more information about location IDs, see [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html).
        # 
        # For LocationId, see [Add a video source](https://help.aliyun.com/document_detail/2848020.html). This ID corresponds to the order of the VideoLayers elements.
        # 
        # This parameter is required.
        self.blend_list = blend_list
        # The ID of the production studio.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, the CasterId is returned in the response.
        # 
        # - If you create a production studio in the LIVE console, go to **Production Studio** > **Cloud Production Studio** to view the name of the production studio.
        # 
        # > The name of the production studio on the Cloud Production Studio page is the ID of the production studio.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The location IDs of the audio sources. The order of the location IDs corresponds to the order of the audio layers specified in the **AudioLayer** parameter. For more information about location IDs, see [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html).
        # 
        # For \\`LocationId\\`, see [Add a video source](https://help.aliyun.com/document_detail/2848020.html). It corresponds to the order of the \\`AudioLayers\\` elements.
        # 
        # This parameter is required.
        self.mix_list = mix_list
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The video layouts.
        # 
        # This parameter is required.
        self.video_layer = video_layer

    def validate(self):
        if self.audio_layer:
            for v1 in self.audio_layer:
                 if v1:
                    v1.validate()
        if self.video_layer:
            for v1 in self.video_layer:
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

        if self.blend_list is not None:
            result['BlendList'] = self.blend_list

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.mix_list is not None:
            result['MixList'] = self.mix_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['VideoLayer'] = []
        if self.video_layer is not None:
            for k1 in self.video_layer:
                result['VideoLayer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_layer = []
        if m.get('AudioLayer') is not None:
            for k1 in m.get('AudioLayer'):
                temp_model = main_models.AddCasterLayoutRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k1))

        if m.get('BlendList') is not None:
            self.blend_list = m.get('BlendList')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('MixList') is not None:
            self.mix_list = m.get('MixList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.video_layer = []
        if m.get('VideoLayer') is not None:
            for k1 in m.get('VideoLayer'):
                temp_model = main_models.AddCasterLayoutRequestVideoLayer()
                self.video_layer.append(temp_model.from_map(k1))

        return self

class AddCasterLayoutRequestVideoLayer(DaraModel):
    def __init__(
        self,
        fill_mode: str = None,
        fixed_delay_duration: int = None,
        height_normalized: float = None,
        position_normalized: List[float] = None,
        position_refer: str = None,
        width_normalized: float = None,
    ):
        # The fill mode of the element. Valid values:
        # 
        # - **none** (default): No scaling. The video is displayed in its original size.
        # 
        # - **fit**: The video is scaled to fit the fill area while maintaining its aspect ratio. The video is centered in the fill area. If the aspect ratio of the fill area is different from that of the video, the area along the shorter edge is not filled. This area displays the video of the underlying layer. If no underlying layer is configured, this area is black.
        self.fill_mode = fill_mode
        # The fixed latency for the video layer. Use this parameter to synchronize the video with captions. Unit: milliseconds. Default value: 0. Valid values: **0** to **5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The normalized height of the layer.
        # 
        # - If you set FillMode to none, the width of the layer is scaled in proportion to the height. The default value is **0**. A value of 0 indicates that the video is displayed in its original size.
        # 
        # - If you set FillMode to fit, this parameter is required and its value must be greater than **0**. The value specifies the normalized height of the fill area.
        self.height_normalized = height_normalized
        # The position of the video layer. The value is a normalized coordinate `[x,y]`. Default value: `[0,0]`.
        # 
        # Note: The x and y coordinates must be normalized.
        self.position_normalized = position_normalized
        # The reference point for the position of the layer. Valid values:
        # 
        # - **topLeft** (default): Top-left.
        # 
        # - **topRight**: Top-right.
        # 
        # - **bottomLeft**: Bottom-left.
        # 
        # - **bottomRight**: Bottom-right.
        # 
        # - **center**: Center.
        # 
        # - **topCenter**: Top-center.
        # 
        # - **bottomCenter**: Bottom-center.
        # 
        # - **leftCenter**: Left-center.
        # 
        # - **rightCenter**: Right-center.
        self.position_refer = position_refer
        # The normalized width of the layer.
        # 
        # - If you set FillMode to none, the height of the layer is scaled in proportion to the width. The default value is **0**. A value of 0 indicates that the video is displayed in its original size.
        # 
        # - If you set FillMode to fit, this parameter is required and its value must be greater than **0**. The value specifies the normalized width of the fill area.
        self.width_normalized = width_normalized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fill_mode is not None:
            result['FillMode'] = self.fill_mode

        if self.fixed_delay_duration is not None:
            result['FixedDelayDuration'] = self.fixed_delay_duration

        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.position_normalized is not None:
            result['PositionNormalized'] = self.position_normalized

        if self.position_refer is not None:
            result['PositionRefer'] = self.position_refer

        if self.width_normalized is not None:
            result['WidthNormalized'] = self.width_normalized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FillMode') is not None:
            self.fill_mode = m.get('FillMode')

        if m.get('FixedDelayDuration') is not None:
            self.fixed_delay_duration = m.get('FixedDelayDuration')

        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('PositionNormalized') is not None:
            self.position_normalized = m.get('PositionNormalized')

        if m.get('PositionRefer') is not None:
            self.position_refer = m.get('PositionRefer')

        if m.get('WidthNormalized') is not None:
            self.width_normalized = m.get('WidthNormalized')

        return self

class AddCasterLayoutRequestAudioLayer(DaraModel):
    def __init__(
        self,
        fixed_delay_duration: int = None,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # The fixed latency for the audio layer. Use this parameter to synchronize the audio with captions. Unit: milliseconds. Default value: 0. Valid values: **0** to **5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channels that are used for audio input. Valid values:
        # 
        # - **leftChannel**: Left channel.
        # 
        # - **rightChannel**: Right channel.
        # 
        # - **all** (default): Both channels.
        self.valid_channel = valid_channel
        # The volume multiplication factor for the audio stream. Valid values: 0 to **10.0**.
        # 
        # - **1.0** (default): The original volume is used.
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

