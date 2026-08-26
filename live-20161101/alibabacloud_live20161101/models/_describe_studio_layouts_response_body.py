# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeStudioLayoutsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        studio_layouts: List[main_models.DescribeStudioLayoutsResponseBodyStudioLayouts] = None,
        total: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The layout information.
        self.studio_layouts = studio_layouts
        # The number of layouts.
        self.total = total

    def validate(self):
        if self.studio_layouts:
            for v1 in self.studio_layouts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StudioLayouts'] = []
        if self.studio_layouts is not None:
            for k1 in self.studio_layouts:
                result['StudioLayouts'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.studio_layouts = []
        if m.get('StudioLayouts') is not None:
            for k1 in m.get('StudioLayouts'):
                temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayouts()
                self.studio_layouts.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayouts(DaraModel):
    def __init__(
        self,
        bg_image_config: main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsBgImageConfig = None,
        common_config: main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsCommonConfig = None,
        layer_order_config_list: List[main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsLayerOrderConfigList] = None,
        layout_id: str = None,
        layout_name: str = None,
        layout_type: str = None,
        media_input_config_list: List[main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsMediaInputConfigList] = None,
        screen_input_config_list: List[main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigList] = None,
    ):
        # The background resource configuration.
        self.bg_image_config = bg_image_config
        # The common layout information. This field is returned when the layout is a common layout.
        self.common_config = common_config
        # The layer order configuration.
        self.layer_order_config_list = layer_order_config_list
        # The studio layout ID.
        self.layout_id = layout_id
        # The studio layout name.
        self.layout_name = layout_name
        # The studio layout type. Valid values:
        # 
        # - **common**: common layout.
        # - **studio**: studio layout.
        self.layout_type = layout_type
        # The multimedia input resource configuration.
        self.media_input_config_list = media_input_config_list
        # The chroma key input configuration.
        self.screen_input_config_list = screen_input_config_list

    def validate(self):
        if self.bg_image_config:
            self.bg_image_config.validate()
        if self.common_config:
            self.common_config.validate()
        if self.layer_order_config_list:
            for v1 in self.layer_order_config_list:
                 if v1:
                    v1.validate()
        if self.media_input_config_list:
            for v1 in self.media_input_config_list:
                 if v1:
                    v1.validate()
        if self.screen_input_config_list:
            for v1 in self.screen_input_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bg_image_config is not None:
            result['BgImageConfig'] = self.bg_image_config.to_map()

        if self.common_config is not None:
            result['CommonConfig'] = self.common_config.to_map()

        result['LayerOrderConfigList'] = []
        if self.layer_order_config_list is not None:
            for k1 in self.layer_order_config_list:
                result['LayerOrderConfigList'].append(k1.to_map() if k1 else None)

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.layout_name is not None:
            result['LayoutName'] = self.layout_name

        if self.layout_type is not None:
            result['LayoutType'] = self.layout_type

        result['MediaInputConfigList'] = []
        if self.media_input_config_list is not None:
            for k1 in self.media_input_config_list:
                result['MediaInputConfigList'].append(k1.to_map() if k1 else None)

        result['ScreenInputConfigList'] = []
        if self.screen_input_config_list is not None:
            for k1 in self.screen_input_config_list:
                result['ScreenInputConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgImageConfig') is not None:
            temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsBgImageConfig()
            self.bg_image_config = temp_model.from_map(m.get('BgImageConfig'))

        if m.get('CommonConfig') is not None:
            temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsCommonConfig()
            self.common_config = temp_model.from_map(m.get('CommonConfig'))

        self.layer_order_config_list = []
        if m.get('LayerOrderConfigList') is not None:
            for k1 in m.get('LayerOrderConfigList'):
                temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsLayerOrderConfigList()
                self.layer_order_config_list.append(temp_model.from_map(k1))

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('LayoutName') is not None:
            self.layout_name = m.get('LayoutName')

        if m.get('LayoutType') is not None:
            self.layout_type = m.get('LayoutType')

        self.media_input_config_list = []
        if m.get('MediaInputConfigList') is not None:
            for k1 in m.get('MediaInputConfigList'):
                temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsMediaInputConfigList()
                self.media_input_config_list.append(temp_model.from_map(k1))

        self.screen_input_config_list = []
        if m.get('ScreenInputConfigList') is not None:
            for k1 in m.get('ScreenInputConfigList'):
                temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigList()
                self.screen_input_config_list.append(temp_model.from_map(k1))

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigList(DaraModel):
    def __init__(
        self,
        audio_config: main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigListAudioConfig = None,
        channel_id: str = None,
        color: str = None,
        height_normalized: float = None,
        id: str = None,
        index: int = None,
        only_audio: bool = None,
        portrait_type: int = None,
        position_x: str = None,
        position_y: str = None,
        video_resource_id: str = None,
    ):
        # The audio configuration information.
        self.audio_config = audio_config
        # The channel location ID to which the video resource is bound.
        self.channel_id = channel_id
        # The chroma key color gamut. Valid values:
        # 
        # - **blue**: blue screen background.
        # - **green**: green screen background.
        # - **auto**: automatic detection.
        # - **complex**: real-scene chroma keying.
        self.color = color
        # The normalized height. This is the height ratio of the extracted portrait to the background. Valid values: **0 to 1**.
        self.height_normalized = height_normalized
        # The unique ID of the chroma key source material.
        self.id = id
        # The chroma key source number. Used for frontend display only and has no logical function.
        self.index = index
        # Indicates whether only audio is used.
        self.only_audio = only_audio
        # The portrait type. Valid values:
        # 
        # - **0**: half-body.
        # - **1**: full-body.
        self.portrait_type = portrait_type
        # The position parameter, x coordinate. Valid values: **0 to 1**. The material position is based on the upper-left corner.
        self.position_x = position_x
        # The position parameter, y coordinate. Valid values: **0 to 1**. The material position is based on the upper-left corner.
        self.position_y = position_y
        # The video resource ID.
        self.video_resource_id = video_resource_id

    def validate(self):
        if self.audio_config:
            self.audio_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_config is not None:
            result['AudioConfig'] = self.audio_config.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.color is not None:
            result['Color'] = self.color

        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.id is not None:
            result['Id'] = self.id

        if self.index is not None:
            result['Index'] = self.index

        if self.only_audio is not None:
            result['OnlyAudio'] = self.only_audio

        if self.portrait_type is not None:
            result['PortraitType'] = self.portrait_type

        if self.position_x is not None:
            result['PositionX'] = self.position_x

        if self.position_y is not None:
            result['PositionY'] = self.position_y

        if self.video_resource_id is not None:
            result['VideoResourceId'] = self.video_resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioConfig') is not None:
            temp_model = main_models.DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigListAudioConfig()
            self.audio_config = temp_model.from_map(m.get('AudioConfig'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('OnlyAudio') is not None:
            self.only_audio = m.get('OnlyAudio')

        if m.get('PortraitType') is not None:
            self.portrait_type = m.get('PortraitType')

        if m.get('PositionX') is not None:
            self.position_x = m.get('PositionX')

        if m.get('PositionY') is not None:
            self.position_y = m.get('PositionY')

        if m.get('VideoResourceId') is not None:
            self.video_resource_id = m.get('VideoResourceId')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsScreenInputConfigListAudioConfig(DaraModel):
    def __init__(
        self,
        valid_channel: str = None,
        volume_rate: float = None,
    ):
        # The corresponding channel.
        self.valid_channel = valid_channel
        # The volume.
        self.volume_rate = volume_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.valid_channel is not None:
            result['ValidChannel'] = self.valid_channel

        if self.volume_rate is not None:
            result['VolumeRate'] = self.volume_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValidChannel') is not None:
            self.valid_channel = m.get('ValidChannel')

        if m.get('VolumeRate') is not None:
            self.volume_rate = m.get('VolumeRate')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsMediaInputConfigList(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        fill_mode: str = None,
        height_normalized: float = None,
        id: str = None,
        image_material_id: str = None,
        index: int = None,
        position_normalized: List[float] = None,
        position_refer: str = None,
        video_resource_id: str = None,
        width_normalized: float = None,
    ):
        # The channel location ID to which the video resource is bound.
        self.channel_id = channel_id
        # The fill type. Default value: none.
        self.fill_mode = fill_mode
        # The normalized height of the material. This is the height ratio of the material to the background. Valid values: **0 to 1**.
        self.height_normalized = height_normalized
        # The unique ID of the multimedia material.
        self.id = id
        # The video-on-demand image material ID.
        self.image_material_id = image_material_id
        # The multimedia material number. Used for frontend display only and has no logical function.
        self.index = index
        # The normalized position of the material fill area [x,y]. The values of x and y range from **0 to 1**. For example, [0.1,0.2] indicates a horizontal offset of 10% and a vertical offset of 20% from the upper-left corner.
        self.position_normalized = position_normalized
        # The position reference coordinate of the material. Default value: topLeft, which indicates that the position is set based on the upper-left corner.
        self.position_refer = position_refer
        # The video resource ID.
        self.video_resource_id = video_resource_id
        # The normalized width of the material. This is the width ratio of the material to the background. Valid values: **0 to 1**.
        self.width_normalized = width_normalized

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.fill_mode is not None:
            result['FillMode'] = self.fill_mode

        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.id is not None:
            result['Id'] = self.id

        if self.image_material_id is not None:
            result['ImageMaterialId'] = self.image_material_id

        if self.index is not None:
            result['Index'] = self.index

        if self.position_normalized is not None:
            result['PositionNormalized'] = self.position_normalized

        if self.position_refer is not None:
            result['PositionRefer'] = self.position_refer

        if self.video_resource_id is not None:
            result['VideoResourceId'] = self.video_resource_id

        if self.width_normalized is not None:
            result['WidthNormalized'] = self.width_normalized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('FillMode') is not None:
            self.fill_mode = m.get('FillMode')

        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageMaterialId') is not None:
            self.image_material_id = m.get('ImageMaterialId')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('PositionNormalized') is not None:
            self.position_normalized = m.get('PositionNormalized')

        if m.get('PositionRefer') is not None:
            self.position_refer = m.get('PositionRefer')

        if m.get('VideoResourceId') is not None:
            self.video_resource_id = m.get('VideoResourceId')

        if m.get('WidthNormalized') is not None:
            self.width_normalized = m.get('WidthNormalized')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsLayerOrderConfigList(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The unique ID of the resource.
        self.id = id
        # The type of the resource configuration. Valid values:
        # 
        # - **background**: background material.
        # - **media**: multimedia material.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsCommonConfig(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        video_resource_id: str = None,
    ):
        # The channel location ID to which the video resource is bound.
        self.channel_id = channel_id
        # The video resource ID.
        self.video_resource_id = video_resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.video_resource_id is not None:
            result['VideoResourceId'] = self.video_resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('VideoResourceId') is not None:
            self.video_resource_id = m.get('VideoResourceId')

        return self

class DescribeStudioLayoutsResponseBodyStudioLayoutsBgImageConfig(DaraModel):
    def __init__(
        self,
        id: str = None,
        image_url: str = None,
        location_id: str = None,
        material_id: str = None,
    ):
        # The unique ID of the background material.
        self.id = id
        # The URL of the material.
        self.image_url = image_url
        # The location ID.
        self.location_id = location_id
        # The video-on-demand material ID.
        self.material_id = material_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        return self

