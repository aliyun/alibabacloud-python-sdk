# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ModifyCasterLayoutRequest(DaraModel):
    def __init__(
        self,
        audio_layer: List[main_models.ModifyCasterLayoutRequestAudioLayer] = None,
        blend_list: List[str] = None,
        caster_id: str = None,
        layout_id: str = None,
        mix_list: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        video_layer: List[main_models.ModifyCasterLayoutRequestVideoLayer] = None,
    ):
        # The audio information.
        # 
        # This parameter is required.
        self.audio_layer = audio_layer
        # The location ID (LocationId) of the video resource element.
        # 
        # For the LocationId, see [Add a video source](https://help.aliyun.com/document_detail/2848020.html). The elements correspond to the VideoLayers elements in order.
        # 
        # This parameter is required.
        self.blend_list = blend_list
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster operation](https://help.aliyun.com/document_detail/2848009.html), check the CasterId parameter returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** to view the ID.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page of the ApsaraVideo Live console is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The layout ID. If you added the production studio layout by calling the [AddCasterLayout operation](https://help.aliyun.com/document_detail/2848025.html), check the LayoutId parameter returned by the AddCasterLayout operation.
        # 
        # This parameter is required.
        self.layout_id = layout_id
        # The location ID (LocationId) of the audio resource element.
        # 
        # For the LocationId, see [Add a video source](https://help.aliyun.com/document_detail/2848020.html). The elements correspond to the AudioLayers elements in order.
        # 
        # This parameter is required.
        self.mix_list = mix_list
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The video information.
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

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

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
                temp_model = main_models.ModifyCasterLayoutRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k1))

        if m.get('BlendList') is not None:
            self.blend_list = m.get('BlendList')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('MixList') is not None:
            self.mix_list = m.get('MixList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.video_layer = []
        if m.get('VideoLayer') is not None:
            for k1 in m.get('VideoLayer'):
                temp_model = main_models.ModifyCasterLayoutRequestVideoLayer()
                self.video_layer.append(temp_model.from_map(k1))

        return self

class ModifyCasterLayoutRequestVideoLayer(DaraModel):
    def __init__(
        self,
        fill_mode: str = None,
        fixed_delay_duration: int = None,
        height_normalized: float = None,
        position_normalized: List[float] = None,
        position_refer: str = None,
        width_normalized: float = None,
    ):
        # The element fill mode. 
        # 
        # - **none** (default): no fill. The Layer settings are configured with the image as the target.
        # - **fit**: adaptive. The Layer settings are configured with the fill area (box) as the target. The image is scaled based on the original aspect ratio and centered within the fill area (box) using a long-edge alignment method. If the aspect ratio of the fill area does not match the image, the short edges are not filled (the lower Layer image is displayed. If no lower Layer is configured, the default black background is displayed).
        self.fill_mode = fill_mode
        # The fixed delay for the video. This can be used for subtitle synchronization. Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The normalized height ratio of the Layer element. 
        #           
        # - If the no-fill mode is used, the width of the element is proportionally scaled based on this height. Default value: **0**, which indicates that the image is displayed at its original size.
        # - If the adaptive mode is used, this field is required and must be greater than **0**. It specifies the normalized height ratio of the fill area (box).
        self.height_normalized = height_normalized
        # The normalized position values `[x,y]` of the Layer element. Default value: `[0,0]`.
        # 
        # >Note: The x and y values must be normalized.
        self.position_normalized = position_normalized
        # The reference coordinate for the position of the element. Valid values:
        # - **topLeft** (default): top-left.
        # - **topRight**: top-right.
        # - **bottomLeft**: bottom-left.
        # - **bottomRight**: bottom-right.
        # - **center**: center.
        # - **topCenter**: top-center.
        # - **bottomCenter**: bottom-center.
        # - **leftCenter**: left-center.
        # - **rightCenter**: right-center.
        self.position_refer = position_refer
        # The normalized width ratio of the Layer element. 
        # 
        # - If the no-fill mode is used, the height of the element is proportionally scaled based on this width. Default value: **0**, which indicates that the image is displayed at its original size.
        # - If the adaptive mode is used, this field is required and must be greater than **0**. It specifies the normalized width ratio of the fill area (box).
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

class ModifyCasterLayoutRequestAudioLayer(DaraModel):
    def __init__(
        self,
        fixed_delay_duration: int = None,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # The fixed delay for the audio. This can be used for subtitle synchronization. Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The audio channels that can be used as volume input. Valid values:
        # - **leftChannel**: left channel.
        # - **rightChannel**: right channel.
        # - **all** (default): both channels.
        self.valid_channel = valid_channel
        # The normalized height ratio of the Layer element. The width of the element is proportionally scaled based on this height. 
        # 
        # Default value: **0**, which indicates that the element is displayed at its original size.
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

