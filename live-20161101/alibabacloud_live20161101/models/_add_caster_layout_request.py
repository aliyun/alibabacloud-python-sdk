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
        # Audio layout.
        # 
        # This parameter is required.
        self.audio_layer = audio_layer
        # The element represents the location ID of the video resource, i.e., LocationId. Refer to [Adding Video Source](https://help.aliyun.com/document_detail/60250.html) for LocationId, which corresponds in order with the VideoLayers elements.
        # 
        # This parameter is required.
        self.blend_list = blend_list
        # The ID of the production studio.
        # 
        # If you create a production studio through the [CreateCaster](~~69338#doc-api-live-CreateCaster~~ "Creates a production studio.") interface, check the value of the CasterId parameter in the response.
        # 
        # If you create a production studio through the ApsaraVideo Live Console, log in to the console, then check the ID of the production studio through the following path:
        # 
        # Production Studios > Production Studio Management
        # 
        # >  The CasterId is reflected in the Name column on the Production Studio Management page.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The element represents the location ID of the audio resource, i.e., LocationId.
        # LocationId is referred to in [Adding Video Source](https://help.aliyun.com/document_detail/60250.html), and corresponds in order with the AudioLayers elements.
        # 
        # This parameter is required.
        self.mix_list = mix_list
        self.owner_id = owner_id
        self.region_id = region_id
        # Video layout.
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
        # The scaling mode of video layer N. Valid values:
        # 
        # *   **none**: The image is not scaled to fill in the specified layout section. Set video layer N based on the image size of the video resource. This is the default value.
        # *   **fit**: The image is scaled with the original aspect ratio to fill in the specified layout section. Set video layer N based on the section size. The image is centered in the layout section with the long side of the image equaling that of the section. If the aspect ratio of the image is inconsistent with that of the section, the short side of the image may be shorter than that of the section. The area outside the image displays the next video layer or the background if no next video layer exists. By default, the background color is black.
        self.fill_mode = fill_mode
        # The fixed delay of video layer N. You can use this parameter to synchronize the video with subtitles. Unit: milliseconds. Valid values: **0 to 5000**. Default value: **0**.
        self.fixed_delay_duration = fixed_delay_duration
        # The normalized value of the height of the image of video layer N.
        # 
        # *   If the FillMode parameter of video layer N is set to none, the width of the video image is scaled based on this parameter. The default value is **0**, which indicates that the video image is displayed in the original size.
        # *   If the FillMode parameter of video layer N is set to fit, you must set this parameter to a value greater than **0**. In this case, the video image is scaled with the original aspect ratio to fill in the specified layout section based on this parameter.
        self.height_normalized = height_normalized
        # The normalized value of the `[x,y]` coordinates of video layer N in the production studio. The default coordinates are `[0,0]`.
        # 
        # >  The coordinates indicate the location of video layer N in the production studio. Set this parameter to the normalized value of the coordinates.
        self.position_normalized = position_normalized
        # The reference coordinates of video layer N in the production studio. Valid values:
        # 
        # *   **topLeft**: the upper-left corner. This is the default value.
        # *   **topRight**: the upper-right corner.
        # *   **bottomLeft**: the lower-left corner.
        # *   **bottomRight**: the lower-right corner.
        # *   **center**: the center position.
        # *   **topCenter**: the upper center position.
        # *   **bottomCenter**: the lower center position.
        # *   **leftCenter**: the left center position.
        # *   **rightCenter**: the right center position.
        self.position_refer = position_refer
        # The normalized value of the width of the image of video layer N.
        # 
        # *   If the FillMode parameter of video layer N is set to none, the height of the video image is scaled based on this parameter. The default value is **0**, which indicates that the video image is displayed in the original size.
        # *   If the FillMode parameter of video layer N is set to fit, you must set this parameter to a value greater than **0**. In this case, the video image is scaled with the original aspect ratio to fill in the specified layout section based on this parameter.
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
        # The fixed delay of audio layer N. You can use this parameter to synchronize the audio with subtitles. Unit: milliseconds. Valid values: **0 to 5000**. Default value: **0**.
        self.fixed_delay_duration = fixed_delay_duration
        # The valid voice channels of audio layer N. Valid values:
        # 
        # *   **leftChannel**: the left channel.
        # *   **rightChannel**: the right channel.
        # *   **all**: both the left and right channels. This is the default value.
        self.valid_channel = valid_channel
        # The multiples of the original volume at which audio layer N plays audio streams. Valid values: **0 to 10.0**.
        # 
        # *   The default value **1.0** indicates that audio layer N plays audio streams at the original volume.
        # *   A value smaller than **1.0** indicates that audio layer N plays audio streams at a lower volume than the original one.
        # *   A value greater than **1.0** indicates that audio layer N plays audio streams at a higher volume than the original one.
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

