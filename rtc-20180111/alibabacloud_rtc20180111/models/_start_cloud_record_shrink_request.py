# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class StartCloudRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        annotation: str = None,
        app_id: str = None,
        backgrounds: List[main_models.StartCloudRecordShrinkRequestBackgrounds] = None,
        bg_color: main_models.StartCloudRecordShrinkRequestBgColor = None,
        channel_id: str = None,
        clock_widgets: List[main_models.StartCloudRecordShrinkRequestClockWidgets] = None,
        crop_mode: int = None,
        images: List[main_models.StartCloudRecordShrinkRequestImages] = None,
        layout_specified_users_shrink: str = None,
        panes: List[main_models.StartCloudRecordShrinkRequestPanes] = None,
        record_mode: int = None,
        region_color: main_models.StartCloudRecordShrinkRequestRegionColor = None,
        reserve_pane_for_no_camera_user: bool = None,
        show_default_background_on_mute: bool = None,
        single_streaming_record_shrink: str = None,
        start_without_channel: bool = None,
        start_without_channel_wait_time: int = None,
        storage_config: main_models.StartCloudRecordShrinkRequestStorageConfig = None,
        sub_high_resolution_stream: bool = None,
        task_id: str = None,
        template_id: str = None,
        texts: List[main_models.StartCloudRecordShrinkRequestTexts] = None,
    ):
        # Specifies whether to enable the annotation feature.
        self.annotation = annotation
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The local background images for the pane.
        self.backgrounds = backgrounds
        # The global background color.
        self.bg_color = bg_color
        # The ID of an existing channel. Only a single ID is supported.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The global clock watermark.
        self.clock_widgets = clock_widgets
        # The crop mode. Valid values:
        # - **1**: Crops the video while keeping the aspect ratio.
        # - **2**: Keeps the aspect ratio and adds padding (default).
        # - **3**: Stretches the video to fill the pane.
        self.crop_mode = crop_mode
        # The global image watermarks.
        self.images = images
        # The specified user list for layout generation, which includes Blacklist/Whitelist.
        # 
        # Whitelist: specifies the users whose video streams are subscribed to in the room.
        # * After the settings are applied, padding is automatically performed in sequence based on this list.
        # * When switching between multiple layouts in a template, only users in the whitelist are calculated.
        # 
        # Blacklist: specifies the users whose video streams are not subscribed to in the room.
        # * When switching between multiple layouts in a template, only users not in the blacklist are calculated.
        self.layout_specified_users_shrink = layout_specified_users_shrink
        # The pane settings. You can configure up to 16 panes.
        self.panes = panes
        # The recording mode. Valid values:
        # - 0: Mixed-stream recording. This is the default value.
        # - 1: Single-stream recording. Single-stream recording does not support updates.
        self.record_mode = record_mode
        # The global frame background color.
        self.region_color = region_color
        # Specifies whether to reserve a pane for a user who does not publish a camera stream. Default value: true. A value of true indicates that a pane is reserved. A value of false indicates that no pane is reserved.
        self.reserve_pane_for_no_camera_user = reserve_pane_for_no_camera_user
        # Specifies whether to display the default background image of the pane when the user is muted. Valid values:
        # - true: Displays the default background image (default).
        # - false: Does not display the default background image. The custom background image of the pane is still displayed.
        self.show_default_background_on_mute = show_default_background_on_mute
        # The parameters for single-stream recording.
        self.single_streaming_record_shrink = single_streaming_record_shrink
        # Specifies whether to allow starting the task when the channel does not exist. Valid values:
        # - true: Yes.
        # - false: No (default).
        self.start_without_channel = start_without_channel
        # The wait time for the task when the channel is not started, in seconds. This parameter takes effect only when the StartWithoutChannel parameter is set to true. Valid values: 30 to 120.
        self.start_without_channel_wait_time = start_without_channel_wait_time
        # The storage configuration.
        # 
        # This parameter is required.
        self.storage_config = storage_config
        # Specifies whether to subscribe to high-resolution streams. Valid values:
        # - false: Subscribes to streams of different resolutions based on the pane area (default).
        # - true: Uses the highest resolution stream published by the client as padding.
        self.sub_high_resolution_stream = sub_high_resolution_stream
        # The task ID of the cloud recording task. Only a single ID is supported. The ID can contain letters, digits, underscores (_), and hyphens (-), and can be up to 55 bytes in length.
        self.task_id = task_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The global text watermarks.
        self.texts = texts

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.bg_color:
            self.bg_color.validate()
        if self.clock_widgets:
            for v1 in self.clock_widgets:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.panes:
            for v1 in self.panes:
                 if v1:
                    v1.validate()
        if self.region_color:
            self.region_color.validate()
        if self.storage_config:
            self.storage_config.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation is not None:
            result['Annotation'] = self.annotation

        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        if self.bg_color is not None:
            result['BgColor'] = self.bg_color.to_map()

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k1 in self.clock_widgets:
                result['ClockWidgets'].append(k1.to_map() if k1 else None)

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.layout_specified_users_shrink is not None:
            result['LayoutSpecifiedUsers'] = self.layout_specified_users_shrink

        result['Panes'] = []
        if self.panes is not None:
            for k1 in self.panes:
                result['Panes'].append(k1.to_map() if k1 else None)

        if self.record_mode is not None:
            result['RecordMode'] = self.record_mode

        if self.region_color is not None:
            result['RegionColor'] = self.region_color.to_map()

        if self.reserve_pane_for_no_camera_user is not None:
            result['ReservePaneForNoCameraUser'] = self.reserve_pane_for_no_camera_user

        if self.show_default_background_on_mute is not None:
            result['ShowDefaultBackgroundOnMute'] = self.show_default_background_on_mute

        if self.single_streaming_record_shrink is not None:
            result['SingleStreamingRecord'] = self.single_streaming_record_shrink

        if self.start_without_channel is not None:
            result['StartWithoutChannel'] = self.start_without_channel

        if self.start_without_channel_wait_time is not None:
            result['StartWithoutChannelWaitTime'] = self.start_without_channel_wait_time

        if self.storage_config is not None:
            result['StorageConfig'] = self.storage_config.to_map()

        if self.sub_high_resolution_stream is not None:
            result['SubHighResolutionStream'] = self.sub_high_resolution_stream

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotation') is not None:
            self.annotation = m.get('Annotation')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.StartCloudRecordShrinkRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        if m.get('BgColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestBgColor()
            self.bg_color = temp_model.from_map(m.get('BgColor'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.StartCloudRecordShrinkRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.StartCloudRecordShrinkRequestImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('LayoutSpecifiedUsers') is not None:
            self.layout_specified_users_shrink = m.get('LayoutSpecifiedUsers')

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.StartCloudRecordShrinkRequestPanes()
                self.panes.append(temp_model.from_map(k1))

        if m.get('RecordMode') is not None:
            self.record_mode = m.get('RecordMode')

        if m.get('RegionColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestRegionColor()
            self.region_color = temp_model.from_map(m.get('RegionColor'))

        if m.get('ReservePaneForNoCameraUser') is not None:
            self.reserve_pane_for_no_camera_user = m.get('ReservePaneForNoCameraUser')

        if m.get('ShowDefaultBackgroundOnMute') is not None:
            self.show_default_background_on_mute = m.get('ShowDefaultBackgroundOnMute')

        if m.get('SingleStreamingRecord') is not None:
            self.single_streaming_record_shrink = m.get('SingleStreamingRecord')

        if m.get('StartWithoutChannel') is not None:
            self.start_without_channel = m.get('StartWithoutChannel')

        if m.get('StartWithoutChannelWaitTime') is not None:
            self.start_without_channel_wait_time = m.get('StartWithoutChannelWaitTime')

        if m.get('StorageConfig') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestStorageConfig()
            self.storage_config = temp_model.from_map(m.get('StorageConfig'))

        if m.get('SubHighResolutionStream') is not None:
            self.sub_high_resolution_stream = m.get('SubHighResolutionStream')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartCloudRecordShrinkRequestTexts()
                self.texts.append(temp_model.from_map(k1))

        return self

class StartCloudRecordShrinkRequestTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordShrinkRequestTextsBoxColor = None,
        font: int = None,
        font_color: main_models.StartCloudRecordShrinkRequestTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the watermark.
        self.alpha = alpha
        # The transparency of the text box.
        self.box_alpha = box_alpha
        # The border width of the text box.
        self.box_borderw = box_borderw
        # The color of the text box.
        self.box_color = box_color
        # The font. Valid values:
        # - **0**: Alibaba PuHuiTi Regular
        # - **1**: Alibaba PuHuiTi Light
        # - **2**: Alibaba PuHuiTi Medium
        # - **3**: Alibaba PuHuiTi Bold
        # - **4**: Alibaba PuHuiTi Heavy
        # - **5**: Alimama ShuHeiTi
        # - **6**: DingTalk JinBuTi
        # - **7**: Alimama DaoLiTi
        # - **8**: Alimama DongFangDaKai
        # - **9**: Alimama FangYuanTi
        self.font = font
        # The font color.
        self.font_color = font_color
        # The font size.
        self.font_size = font_size
        # Specifies whether to display a text box.
        self.has_box = has_box
        # The z-axis layer.
        self.layer = layer
        # The content of the watermark.
        # 
        # This parameter is required.
        self.texture = texture
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.texture is not None:
            result['Texture'] = self.texture

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestTextsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Texture') is not None:
            self.texture = m.get('Texture')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordShrinkRequestTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestStorageConfig(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        bucket: str = None,
        endpoint: str = None,
        region: int = None,
        secret_key: str = None,
        vendor: int = None,
    ):
        # The AccessKey. Make sure that the RAM user associated with the AccessKey pair is granted the **write** permissions on the object storage service of the corresponding cloud provider. Otherwise, the result files fail to be written.
        # 
        # This parameter is required.
        self.access_key = access_key
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The private endpoint for Apsara Stack.
        self.endpoint = endpoint
        # The storage region.
        # 
        # | Region | Alibaba Cloud OSS |
        # |--------|------------|
        # | 0 | CN_Hangzhou |
        # | 1 | CN_Shanghai |
        # | 2 | CN_Qingdao |
        # | 3 | CN_Beijing |
        # | 4 | CN_Zhangjiakou |
        # | 5 | CN_Huhehaote |
        # | 6 | CN_Shenzhen |
        # | 7 | CN_Hongkong |
        # | 8 | US_West_1 |
        # | 9 | US_East_1 |
        # | 10 | AP_Southeast_1 |
        # | 11 | AP_Southeast_2 (Deprecated. Do not use.) |
        # | 12 | AP_Southeast_3 |
        # | 13 | AP_Southeast_5 |
        # | 14 | AP_Northeast_1 |
        # | 15 | AP_South_1 (Deprecated. Do not use.) |
        # | 16 | EU_Central_1 |
        # | 17 | EU_West_1 |
        # | 18 | EU_East_1(ME_East_1) |
        # | 19 | AP_Southeast_6 |
        # | 20 | CN_Heyuan |
        # | 21 | CN_Guangzhou |
        # | 22 | CN_Chengdu |
        # | 23 | CN_Nanjing |
        # | 24 | CN_Fuzhou |
        # | 25 | CN_Wulanchabu |
        # | 26 | CN_Northeast_2 |
        # | 27 | CN_Southeast_7 |
        # | 28 | CN_Wuhan_LR |
        # | 100 | oss-cn-hzjbp |
        # | 101 | oss-cn-shanghai-finance-1 |
        # | 102 | oss-cn-shenzhen-finance-1 |
        # | 103 | oss-cn-beijing-finance-1 |
        # | 104 | oss-cn-hzfinance |
        # | 105 | oss-cn-shanghai-finance-1-pub |
        # | 106 | oss-cn-szfinance |
        # | 107 | oss-cn-beijing-finance-1-pub |
        # 
        # | Region | Apsara Stack OSS |
        # |--------|------------|
        # | 0 | default |
        # 
        # This parameter is required.
        self.region = region
        # secretKey
        # 
        # This parameter is required.
        self.secret_key = secret_key
        # The storage platform. Valid values:
        # 
        # | vendor | Object storage service | Remarks |
        # |--------|---------|---------|
        # | 1 | AliYun OSS | Alibaba Cloud |
        # | 2 | Apsara Stack OSS | Alibaba Cloud Apsara Stack |
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.region is not None:
            result['Region'] = self.region

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class StartCloudRecordShrinkRequestRegionColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestPanes(DaraModel):
    def __init__(
        self,
        backgrounds: List[main_models.StartCloudRecordShrinkRequestPanesBackgrounds] = None,
        images: List[main_models.StartCloudRecordShrinkRequestPanesImages] = None,
        pane_crop_mode: int = None,
        pane_id: int = None,
        reserve_pane_for_offline_user: bool = None,
        source: str = None,
        source_type: str = None,
        texts: List[main_models.StartCloudRecordShrinkRequestPanesTexts] = None,
        video_order: str = None,
        whiteboard: main_models.StartCloudRecordShrinkRequestPanesWhiteboard = None,
    ):
        # The local background images for the pane.
        self.backgrounds = backgrounds
        # The local image watermarks for the pane.
        self.images = images
        # The crop mode of the image. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Maintains the aspect ratio and adds borders.
        # - **3**: Stretches the image to fill the pane.
        self.pane_crop_mode = pane_crop_mode
        # The ID of the pane. The value starts from 0.
        # 
        # This parameter is required.
        self.pane_id = pane_id
        # Specifies whether to reserve the pane as a placeholder for users who have not joined the meeting.
        # Default value: true. A value of true indicates that if the specific user or wildcard user specified for the pane is offline, the pane is forcibly reserved as a placeholder. A value of false indicates that if the specific user or wildcard user specified for the pane is offline, video streams are displayed based on the automatic fill order.
        self.reserve_pane_for_offline_user = reserve_pane_for_offline_user
        # The media source of the pane. You can specify a user ID. To specify a specific user type, you can use wildcard configurations. The following wildcard types are supported:
        # - **$ActiveSpeaker**: the current speaker in the channel.
        # - **$ScreenShare**: the user who is sharing the screen. If multiple users are sharing their screens in the channel, the panes are filled in chronological order.
        self.source = source
        # The media type of the pane. Valid values:
        # - **video**: The user camera or screen sharing stream. This is the default value.
        # - **camera**: The camera stream.
        # - **screen**: The screen sharing stream.
        # - **whiteboard**: The whiteboard.
        self.source_type = source_type
        # The local text watermarks for the pane.
        self.texts = texts
        # The fill order when SourceType is set to video. Valid values:
        # - screenFirst: Screen sharing takes precedence. This is the default value.
        # - cameraFirst: The camera takes precedence.
        self.video_order = video_order
        # The whiteboard configurations.
        self.whiteboard = whiteboard

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()
        if self.whiteboard:
            self.whiteboard.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.pane_crop_mode is not None:
            result['PaneCropMode'] = self.pane_crop_mode

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.reserve_pane_for_offline_user is not None:
            result['ReservePaneForOfflineUser'] = self.reserve_pane_for_offline_user

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        if self.video_order is not None:
            result['VideoOrder'] = self.video_order

        if self.whiteboard is not None:
            result['Whiteboard'] = self.whiteboard.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.StartCloudRecordShrinkRequestPanesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.StartCloudRecordShrinkRequestPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneCropMode') is not None:
            self.pane_crop_mode = m.get('PaneCropMode')

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('ReservePaneForOfflineUser') is not None:
            self.reserve_pane_for_offline_user = m.get('ReservePaneForOfflineUser')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.StartCloudRecordShrinkRequestPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('VideoOrder') is not None:
            self.video_order = m.get('VideoOrder')

        if m.get('Whiteboard') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestPanesWhiteboard()
            self.whiteboard = temp_model.from_map(m.get('Whiteboard'))

        return self

class StartCloudRecordShrinkRequestPanesWhiteboard(DaraModel):
    def __init__(
        self,
        whiteboard_id: str = None,
    ):
        # The ID of the whiteboard. Default value: default.
        self.whiteboard_id = whiteboard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.whiteboard_id is not None:
            result['WhiteboardId'] = self.whiteboard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WhiteboardId') is not None:
            self.whiteboard_id = m.get('WhiteboardId')

        return self

class StartCloudRecordShrinkRequestPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordShrinkRequestPanesTextsBoxColor = None,
        display: str = None,
        font: int = None,
        font_color: main_models.StartCloudRecordShrinkRequestPanesTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the watermark.
        self.alpha = alpha
        # The transparency of the text box.
        self.box_alpha = box_alpha
        # The border width of the text box.
        self.box_borderw = box_borderw
        # The color of the text box.
        self.box_color = box_color
        # The condition for displaying the watermark. Valid values:
        # - streamOnly: The watermark is displayed when the current user has a video stream. This is the default value.
        # - backup: The watermark is displayed when the current user does not have a video stream.
        # - always: The watermark is always displayed.
        self.display = display
        # The font. Valid values:
        # - **0**: Alibaba PuHuiTi Regular
        # - **1**: Alibaba PuHuiTi Light
        # - **2**: Alibaba PuHuiTi Medium
        # - **3**: Alibaba PuHuiTi Bold
        # - **4**: Alibaba PuHuiTi Heavy
        # - **5**: Alimama ShuHeiTi
        # - **6**: DingTalk JinBuTi
        # - **7**: Alimama DaoLiTi
        # - **8**: Alimama DongFangDaKai
        # - **9**: Alimama FangYuanTi
        self.font = font
        # The font color.
        self.font_color = font_color
        # The font size.
        self.font_size = font_size
        # Specifies whether to display a text box.
        self.has_box = has_box
        # The z-axis layer.
        self.layer = layer
        # The content of the watermark.
        # 
        # This parameter is required.
        self.texture = texture
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.display is not None:
            result['Display'] = self.display

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.texture is not None:
            result['Texture'] = self.texture

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestPanesTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestPanesTextsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Texture') is not None:
            self.texture = m.get('Texture')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordShrinkRequestPanesTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestPanesTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestPanesImages(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: str = None,
        height: float = None,
        layer: int = None,
        pane_image_crop_mode: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the image.
        self.alpha = alpha
        # The condition for displaying the watermark. Valid values:
        # - streamOnly: The watermark is displayed when the current user has a video stream. This is the default value.
        # - backup: The watermark is displayed when the current user does not have a video stream.
        # - always: The watermark is always displayed.
        self.display = display
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The z-axis layer.
        self.layer = layer
        # The crop mode of the image. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Maintains the aspect ratio and adds borders.
        # - **3**: Stretches the image to fill the pane.
        self.pane_image_crop_mode = pane_image_crop_mode
        # The URL of the image. The image content cannot be updated during stream ingest.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.pane_image_crop_mode is not None:
            result['PaneImageCropMode'] = self.pane_image_crop_mode

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('PaneImageCropMode') is not None:
            self.pane_image_crop_mode = m.get('PaneImageCropMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordShrinkRequestPanesBackgrounds(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: str = None,
        height: float = None,
        layer: int = None,
        pane_background_crop_mode: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the image.
        self.alpha = alpha
        # The condition for displaying the background image. Valid values:
        # - streamOnly: The background image is displayed when the current user has a video stream. This is the default value.
        # - backup: The background image is displayed when the current user does not have a video stream.
        # - always: The background image is always displayed.
        self.display = display
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The z-axis layer.
        self.layer = layer
        # The crop mode of the image. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Maintains the aspect ratio and adds borders.
        # - **3**: Stretches the image to fill the pane.
        self.pane_background_crop_mode = pane_background_crop_mode
        # The URL of the image.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.pane_background_crop_mode is not None:
            result['PaneBackgroundCropMode'] = self.pane_background_crop_mode

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('PaneBackgroundCropMode') is not None:
            self.pane_background_crop_mode = m.get('PaneBackgroundCropMode')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordShrinkRequestImages(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        height: float = None,
        image_crop_mode: int = None,
        layer: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the image.
        self.alpha = alpha
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The crop mode of the image. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Maintains the aspect ratio and adds borders.
        # - **3**: Stretches the image to fill the pane.
        self.image_crop_mode = image_crop_mode
        # The z-axis layer.
        self.layer = layer
        # The image URL. The image content cannot be updated during stream ingest.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.height is not None:
            result['Height'] = self.height

        if self.image_crop_mode is not None:
            result['ImageCropMode'] = self.image_crop_mode

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageCropMode') is not None:
            self.image_crop_mode = m.get('ImageCropMode')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class StartCloudRecordShrinkRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.StartCloudRecordShrinkRequestClockWidgetsBoxColor = None,
        font: int = None,
        font_color: main_models.StartCloudRecordShrinkRequestClockWidgetsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        x: float = None,
        y: float = None,
        zone: int = None,
    ):
        # The transparency of the image.
        self.alpha = alpha
        # The transparency of the text box.
        self.box_alpha = box_alpha
        # The border width of the text box.
        self.box_borderw = box_borderw
        # The color of the text box.
        self.box_color = box_color
        # The font. Valid values:
        # - **0**: Alibaba PuHuiTi Regular
        # - **1**: Alibaba PuHuiTi Light
        # - **2**: Alibaba PuHuiTi Medium
        # - **3**: Alibaba PuHuiTi Bold
        # - **4**: Alibaba PuHuiTi Heavy
        # - **5**: Alimama ShuHeiTi
        # - **6**: DingTalk JinBuTi
        # - **7**: Alimama DaoLiTi
        # - **8**: Alimama DongFangDaKai
        # - **9**: Alimama FangYuanTi
        self.font = font
        # The font color.
        self.font_color = font_color
        # The font size of the clock.
        self.font_size = font_size
        # Specifies whether to display a text box.
        self.has_box = has_box
        # The z-axis layer.
        self.layer = layer
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y
        # The time zone.
        self.zone = zone

    def validate(self):
        if self.box_color:
            self.box_color.validate()
        if self.font_color:
            self.font_color.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.box_alpha is not None:
            result['BoxAlpha'] = self.box_alpha

        if self.box_borderw is not None:
            result['BoxBorderw'] = self.box_borderw

        if self.box_color is not None:
            result['BoxColor'] = self.box_color.to_map()

        if self.font is not None:
            result['Font'] = self.font

        if self.font_color is not None:
            result['FontColor'] = self.font_color.to_map()

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.has_box is not None:
            result['HasBox'] = self.has_box

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BoxAlpha') is not None:
            self.box_alpha = m.get('BoxAlpha')

        if m.get('BoxBorderw') is not None:
            self.box_borderw = m.get('BoxBorderw')

        if m.get('BoxColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestClockWidgetsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.StartCloudRecordShrinkRequestClockWidgetsFontColor()
            self.font_color = temp_model.from_map(m.get('FontColor'))

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('HasBox') is not None:
            self.has_box = m.get('HasBox')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class StartCloudRecordShrinkRequestClockWidgetsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestClockWidgetsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestBgColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # The blue component.
        self.b = b
        # The green component.
        self.g = g
        # The red component.
        self.r = r

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b is not None:
            result['B'] = self.b

        if self.g is not None:
            result['G'] = self.g

        if self.r is not None:
            result['R'] = self.r

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('B') is not None:
            self.b = m.get('B')

        if m.get('G') is not None:
            self.g = m.get('G')

        if m.get('R') is not None:
            self.r = m.get('R')

        return self

class StartCloudRecordShrinkRequestBackgrounds(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        background_crop_mode: int = None,
        height: float = None,
        layer: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the image.
        self.alpha = alpha
        # The crop mode of the image. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Maintains the aspect ratio and adds borders.
        # - **3**: Stretches the image to fill the pane.
        self.background_crop_mode = background_crop_mode
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The z-axis layer.
        self.layer = layer
        # The URL of the image.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The x-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The y-coordinate.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.background_crop_mode is not None:
            result['BackgroundCropMode'] = self.background_crop_mode

        if self.height is not None:
            result['Height'] = self.height

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BackgroundCropMode') is not None:
            self.background_crop_mode = m.get('BackgroundCropMode')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

