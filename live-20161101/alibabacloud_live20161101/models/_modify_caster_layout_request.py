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
        # The audio layers.
        # 
        # This parameter is required.
        self.audio_layer = audio_layer
        # The location IDs of the video layers, which are in the same order as the video layers.
        # 
        # For more information, see [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html).
        # 
        # This parameter is required.
        self.blend_list = blend_list
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The ID of the layout. If the layout was added by calling the [AddCasterLayout](https://help.aliyun.com/document_detail/2848025.html) operation, check the value of the response parameter LayoutId to obtain the ID.
        # 
        # This parameter is required.
        self.layout_id = layout_id
        # The location IDs of the audio layers, which are in the same order as the audio layers.
        # 
        # For more information, see [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html).
        # 
        # This parameter is required.
        self.mix_list = mix_list
        self.owner_id = owner_id
        self.region_id = region_id
        # The video layers.
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
        # The scaling mode of the video layer. Valid values:
        # 
        # *   **none** (default): indicates that the video layer is not scaled. The video layer is displayed based on its original size.
        # *   **fit**: indicates that the video layer is adapted to the fill area. In this case, the video layer is scaled proportionally, with its original aspect ratio retained. The video layer is placed in the center, with its longer sides aligned with the fill area. If the aspect ratio of the video layer is different from that of the fill area, the content of the lower layer is displayed alongside the shorter sides. If there is no lower layer, black bars are displayed instead.
        self.fill_mode = fill_mode
        # The fixed delay of the video layer. This parameter is used to synchronize the video with subtitles. Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The normalized value of the height of the video layer.
        # 
        # *   If the FillMode parameter of the video layer is set to none, the width of the video layer is proportionally scaled based on this parameter. The default value is **0**, which indicates that the video layer is not scaled.
        # *   If the FillMode parameter of the video layer is set to fit, the value of this parameter is greater than **0**.
        self.height_normalized = height_normalized
        # The normalized value of the position of the video layer, in the format of `[x,y]`. Default value: `[0,0]`.
        # 
        # >  The values of x and y are normalized.
        self.position_normalized = position_normalized
        # The reference coordinates of the video layer. Valid values:
        # 
        # *   **topLeft** (default): the upper-left corner
        # *   **topRight**: the upper-right corner
        # *   **bottomLeft**: the lower-left corner
        # *   **bottomRight**: the lower-right corner
        # *   **center**: the center
        # *   **topCenter**: the upper center
        # *   **bottomCenter**: the lower center
        # *   **leftCenter**: the left center
        # *   **rightCenter**: the right center
        self.position_refer = position_refer
        # The normalized value of the width of the video layer.
        # 
        # *   If the FillMode parameter of the video layer is set to none, the height of the video layer is proportionally scaled based on this parameter. The default value is **0**, which indicates that the video layer is not scaled.
        # *   If the FillMode parameter of the video layer is set to fit, the value of this parameter is greater than **0**.
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
        # The fixed delay of the audio layer. This parameter is used to synchronize the audio with subtitles. Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channels that are used for volume input in the audio layer. Valid values:
        # 
        # *   **leftChannel**: the left channel
        # *   **rightChannel**: the right channel
        # *   **all** (default): both the left and right channels
        self.valid_channel = valid_channel
        # The normalized value of the height of the audio layer. The width of the audio layer is proportionally scaled based on this parameter.
        # 
        # The default value is **0**, which indicates that the audio layer is not scaled.
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

