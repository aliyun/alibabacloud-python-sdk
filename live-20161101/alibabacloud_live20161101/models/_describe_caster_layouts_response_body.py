# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterLayoutsResponseBody(DaraModel):
    def __init__(
        self,
        layouts: main_models.DescribeCasterLayoutsResponseBodyLayouts = None,
        request_id: str = None,
        total: int = None,
    ):
        # The layouts.
        self.layouts = layouts
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.layouts:
            self.layouts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.layouts is not None:
            result['Layouts'] = self.layouts.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layouts') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayouts()
            self.layouts = temp_model.from_map(m.get('Layouts'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterLayoutsResponseBodyLayouts(DaraModel):
    def __init__(
        self,
        layout: List[main_models.DescribeCasterLayoutsResponseBodyLayoutsLayout] = None,
    ):
        self.layout = layout

    def validate(self):
        if self.layout:
            for v1 in self.layout:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Layout'] = []
        if self.layout is not None:
            for k1 in self.layout:
                result['Layout'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layout = []
        if m.get('Layout') is not None:
            for k1 in m.get('Layout'):
                temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayout()
                self.layout.append(temp_model.from_map(k1))

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayout(DaraModel):
    def __init__(
        self,
        audio_layers: main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayers = None,
        blend_list: main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutBlendList = None,
        layout_id: str = None,
        mix_list: main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutMixList = None,
        video_layers: main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayers = None,
    ):
        # The configurations of the audio layers.
        self.audio_layers = audio_layers
        # The location IDs of the video layers, which are in the same order as the video layers.
        self.blend_list = blend_list
        # The ID of the layout.
        self.layout_id = layout_id
        # The location IDs of the audio layers, which are in the same order as the audio layers.
        self.mix_list = mix_list
        # The configurations of the video layers, which are in the default array sequence.
        self.video_layers = video_layers

    def validate(self):
        if self.audio_layers:
            self.audio_layers.validate()
        if self.blend_list:
            self.blend_list.validate()
        if self.mix_list:
            self.mix_list.validate()
        if self.video_layers:
            self.video_layers.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_layers is not None:
            result['AudioLayers'] = self.audio_layers.to_map()

        if self.blend_list is not None:
            result['BlendList'] = self.blend_list.to_map()

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.mix_list is not None:
            result['MixList'] = self.mix_list.to_map()

        if self.video_layers is not None:
            result['VideoLayers'] = self.video_layers.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioLayers') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayers()
            self.audio_layers = temp_model.from_map(m.get('AudioLayers'))

        if m.get('BlendList') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutBlendList()
            self.blend_list = temp_model.from_map(m.get('BlendList'))

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('MixList') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutMixList()
            self.mix_list = temp_model.from_map(m.get('MixList'))

        if m.get('VideoLayers') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayers()
            self.video_layers = temp_model.from_map(m.get('VideoLayers'))

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayers(DaraModel):
    def __init__(
        self,
        video_layer: List[main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayer] = None,
    ):
        self.video_layer = video_layer

    def validate(self):
        if self.video_layer:
            for v1 in self.video_layer:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoLayer'] = []
        if self.video_layer is not None:
            for k1 in self.video_layer:
                result['VideoLayer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_layer = []
        if m.get('VideoLayer') is not None:
            for k1 in m.get('VideoLayer'):
                temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayer()
                self.video_layer.append(temp_model.from_map(k1))

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayer(DaraModel):
    def __init__(
        self,
        fill_mode: str = None,
        fixed_delay_duration: int = None,
        height_normalized: float = None,
        position_normalizeds: main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds = None,
        position_refer: str = None,
        width_normalized: float = None,
    ):
        # The scaling mode of the video layer. Valid values:
        # 
        # *   **none** (default): specifies that the video layer is not scaled. The video layer is displayed based on its original size.
        # *   **fit**: specifies that the video layer is adapted to the fill area. The video layer is displayed based on the fill area. In this case, the video layer is scaled proportionally, with its original aspect ratio retained. The video layer is placed in the center, with its longer sides aligned with the fill area. If the aspect ratio of the video layer is different from that of the fill area, the content of the lower layer is displayed alongside the shorter sides. If there is no lower layer, black bars are displayed instead.
        self.fill_mode = fill_mode
        # The fixed delay of the video layer. This parameter is used to synchronize the video with subtitles.
        # 
        # Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The normalized value of the height of the video layer.
        # 
        # *   If the FillMode parameter of the video layer is set to none, the width of the video layer is proportionally scaled based on this parameter. The default value is **0**, which indicates that the video layer is not scaled.
        # *   If the FillMode parameter of the video layer is set to fit, the value of this parameter is greater than **0**.
        self.height_normalized = height_normalized
        # The normalized value of the position of the video layer, in the format of `[x,y]`. Default value: `[0,0]`.
        # 
        # >  The values of x and y are normalized.
        self.position_normalizeds = position_normalizeds
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
        # *   If the FillMode parameter of the video layer is set to none, the height of the video layer is scaled based on this parameter. The default value is **0**, which indicates that the video layer is not scaled.
        # *   If the FillMode parameter of the video layer is set to fit, the value of this parameter is greater than **0**.
        self.width_normalized = width_normalized

    def validate(self):
        if self.position_normalizeds:
            self.position_normalizeds.validate()

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

        if self.position_normalizeds is not None:
            result['PositionNormalizeds'] = self.position_normalizeds.to_map()

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

        if m.get('PositionNormalizeds') is not None:
            temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds()
            self.position_normalizeds = temp_model.from_map(m.get('PositionNormalizeds'))

        if m.get('PositionRefer') is not None:
            self.position_refer = m.get('PositionRefer')

        if m.get('WidthNormalized') is not None:
            self.width_normalized = m.get('WidthNormalized')

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds(DaraModel):
    def __init__(
        self,
        position: List[float] = None,
    ):
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayoutMixList(DaraModel):
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

class DescribeCasterLayoutsResponseBodyLayoutsLayoutBlendList(DaraModel):
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

class DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayers(DaraModel):
    def __init__(
        self,
        audio_layer: List[main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayersAudioLayer] = None,
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
                temp_model = main_models.DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayersAudioLayer()
                self.audio_layer.append(temp_model.from_map(k1))

        return self

class DescribeCasterLayoutsResponseBodyLayoutsLayoutAudioLayersAudioLayer(DaraModel):
    def __init__(
        self,
        fixed_delay_duration: int = None,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # The fixed delay of the audio layer. This parameter is used to synchronize the audio with subtitles.
        # 
        # Unit: milliseconds. Default value: **0**. Valid values: **0 to 5000**.
        self.fixed_delay_duration = fixed_delay_duration
        # The sound channels that are used for volume input in the audio layer. Valid values:
        # 
        # *   **leftChannel**: the left channel
        # *   **rightChannel**: the right channel
        # *   **all** (default): both the left and right channels
        self.valid_channel = valid_channel
        # The normalized value of the height of the audio layer. The width of the audio layer is proportionally scaled based on this parameter.
        # 
        # >  The default value is **0**, which indicates that the audio layer is not scaled.
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

