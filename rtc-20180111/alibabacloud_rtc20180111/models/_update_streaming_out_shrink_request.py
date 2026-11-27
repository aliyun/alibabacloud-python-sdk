# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class UpdateStreamingOutShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        backgrounds: List[main_models.UpdateStreamingOutShrinkRequestBackgrounds] = None,
        bg_color: main_models.UpdateStreamingOutShrinkRequestBgColor = None,
        channel_id: str = None,
        clock_widgets: List[main_models.UpdateStreamingOutShrinkRequestClockWidgets] = None,
        crop_mode: int = None,
        images: List[main_models.UpdateStreamingOutShrinkRequestImages] = None,
        layout_specified_users_shrink: str = None,
        panes: List[main_models.UpdateStreamingOutShrinkRequestPanes] = None,
        region_color: main_models.UpdateStreamingOutShrinkRequestRegionColor = None,
        spec_mixed_user_list: List[str] = None,
        task_id: str = None,
        template_id: str = None,
        texts: List[main_models.UpdateStreamingOutShrinkRequestTexts] = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The background image.
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
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.crop_mode = crop_mode
        # The global image watermark.
        self.images = images
        # The specified user list for layout generation, which includes two types: blacklist and whitelist.
        # 
        # Whitelist: specifies the users in the room whose video streams are subscribed to.
        # * After the setting is applied, automatic padding is performed in sequence based on this list.
        # * When switching between multiple layouts in a template, only users in the whitelist are considered.
        # 
        # Blacklist: specifies the users in the room whose video streams are not subscribed to.
        # * When switching between multiple layouts in a template, only users not in the blacklist are considered.
        self.layout_specified_users_shrink = layout_specified_users_shrink
        # The pane settings. You can configure up to 16 panes.
        self.panes = panes
        # The global region background color.
        self.region_color = region_color
        # The list of specified users for audio mixing.
        self.spec_mixed_user_list = spec_mixed_user_list
        # The ID of the bypass live streaming task. Only a single ID is supported. The ID can contain uppercase and lowercase letters, digits, underscores (_), and hyphens (-), and can be up to 55 bytes in length.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The template ID.
        # >Notice: When you update the template ID, you can only update the layout. The resolution cannot be updated.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The global text watermark.
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
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.region_color is not None:
            result['RegionColor'] = self.region_color.to_map()

        if self.spec_mixed_user_list is not None:
            result['SpecMixedUserList'] = self.spec_mixed_user_list

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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        if m.get('BgColor') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestBgColor()
            self.bg_color = temp_model.from_map(m.get('BgColor'))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('LayoutSpecifiedUsers') is not None:
            self.layout_specified_users_shrink = m.get('LayoutSpecifiedUsers')

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestPanes()
                self.panes.append(temp_model.from_map(k1))

        if m.get('RegionColor') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestRegionColor()
            self.region_color = temp_model.from_map(m.get('RegionColor'))

        if m.get('SpecMixedUserList') is not None:
            self.spec_mixed_user_list = m.get('SpecMixedUserList')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestTexts()
                self.texts.append(temp_model.from_map(k1))

        return self

class UpdateStreamingOutShrinkRequestTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.UpdateStreamingOutShrinkRequestTextsBoxColor = None,
        font: int = None,
        font_color: main_models.UpdateStreamingOutShrinkRequestTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the watermark.
        self.alpha = alpha
        # The transparency of the rectangle.
        self.box_alpha = box_alpha
        # The border width of the rectangle.
        self.box_borderw = box_borderw
        # The color of the rectangle.
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
        # Specifies whether to display the rectangle.
        self.has_box = has_box
        # The Z-axis layer.
        self.layer = layer
        # The watermark content.
        # 
        # This parameter is required.
        self.texture = texture
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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
            temp_model = main_models.UpdateStreamingOutShrinkRequestTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestTextsFontColor()
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

class UpdateStreamingOutShrinkRequestTextsFontColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestTextsBoxColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestRegionColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestPanes(DaraModel):
    def __init__(
        self,
        backgrounds: List[main_models.UpdateStreamingOutShrinkRequestPanesBackgrounds] = None,
        images: List[main_models.UpdateStreamingOutShrinkRequestPanesImages] = None,
        pane_crop_mode: int = None,
        pane_id: int = None,
        reserve_pane_for_offline_user: bool = None,
        source: str = None,
        source_type: str = None,
        texts: List[main_models.UpdateStreamingOutShrinkRequestPanesTexts] = None,
        video_order: str = None,
        whiteboard: main_models.UpdateStreamingOutShrinkRequestPanesWhiteboard = None,
    ):
        # The background image of the pane.
        self.backgrounds = backgrounds
        # The local image watermarks for the pane.
        self.images = images
        # The crop mode. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.pane_crop_mode = pane_crop_mode
        # The pane ID.
        self.pane_id = pane_id
        # Specifies whether to reserve the pane as a placeholder for offline users. Default value: true. A value of true indicates that the pane is forcibly reserved as a placeholder when the specific user or wildcard user specified for the grid is offline. A value of false indicates that video streams are displayed in the automatic fill order when the specific user or wildcard user specified for the grid is offline.
        self.reserve_pane_for_offline_user = reserve_pane_for_offline_user
        # The media source of the pane. You can specify a userId. To specify a specific user type, you can use wildcard configurations. The following types are supported:
        # - **$ActiveSpeaker**: The current speaker in the channel.
        # - **$ScreenShare**: The user who is sharing their screen. If multiple users are sharing their screens in the channel, the panes are filled in chronological order.
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
                temp_model = main_models.UpdateStreamingOutShrinkRequestPanesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.UpdateStreamingOutShrinkRequestPanesImages()
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
                temp_model = main_models.UpdateStreamingOutShrinkRequestPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('VideoOrder') is not None:
            self.video_order = m.get('VideoOrder')

        if m.get('Whiteboard') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestPanesWhiteboard()
            self.whiteboard = temp_model.from_map(m.get('Whiteboard'))

        return self

class UpdateStreamingOutShrinkRequestPanesWhiteboard(DaraModel):
    def __init__(
        self,
        whiteboard_id: str = None,
    ):
        # The whiteboard ID. Default value: default.
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

class UpdateStreamingOutShrinkRequestPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.UpdateStreamingOutShrinkRequestPanesTextsBoxColor = None,
        display: str = None,
        font: int = None,
        font_color: main_models.UpdateStreamingOutShrinkRequestPanesTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        # The transparency of the watermark.
        self.alpha = alpha
        # The transparency of the rectangle.
        self.box_alpha = box_alpha
        # The border width of the rectangle.
        self.box_borderw = box_borderw
        # The color of the rectangle.
        self.box_color = box_color
        # The condition for displaying the watermark. Valid values:
        # - streamOnly: Displayed when the current user has a video stream. This is the default value.
        # - backup: Displayed when the current user does not have a video stream.
        # - always: Always displayed.
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
        # Specifies whether to display the rectangle.
        self.has_box = has_box
        # The Z-axis layer.
        self.layer = layer
        # The watermark content.
        # 
        # This parameter is required.
        self.texture = texture
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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
            temp_model = main_models.UpdateStreamingOutShrinkRequestPanesTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestPanesTextsFontColor()
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

class UpdateStreamingOutShrinkRequestPanesTextsFontColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestPanesTextsBoxColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestPanesImages(DaraModel):
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
        # The transparency.
        self.alpha = alpha
        # The condition for displaying the watermark. Valid values:
        # - streamOnly: Displayed when the current user has a video stream. This is the default value.
        # - backup: Displayed when the current user does not have a video stream.
        # - always: Always displayed.
        self.display = display
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The Z-axis layer.
        self.layer = layer
        # The crop mode. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.pane_image_crop_mode = pane_image_crop_mode
        # The image URL. The image content cannot be updated during stream ingest.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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

class UpdateStreamingOutShrinkRequestPanesBackgrounds(DaraModel):
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
        # The transparency.
        self.alpha = alpha
        # The condition for displaying the watermark. Valid values:
        # - streamOnly: Displayed when the current user has a video stream. This is the default value.
        # - backup: Displayed when the current user does not have a video stream.
        # - always: Always displayed.
        self.display = display
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The Z-axis layer.
        self.layer = layer
        # The crop mode. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.pane_background_crop_mode = pane_background_crop_mode
        # The image URL.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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

class UpdateStreamingOutShrinkRequestImages(DaraModel):
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
        # The transparency.
        self.alpha = alpha
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The crop mode. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.image_crop_mode = image_crop_mode
        # The Z-axis layer.
        self.layer = layer
        # The image URL. The image content cannot be updated during stream ingest.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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

class UpdateStreamingOutShrinkRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.UpdateStreamingOutShrinkRequestClockWidgetsBoxColor = None,
        font: int = None,
        font_color: main_models.UpdateStreamingOutShrinkRequestClockWidgetsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        x: float = None,
        y: float = None,
        zone: int = None,
    ):
        # The transparency.
        self.alpha = alpha
        # The transparency of the rectangle.
        self.box_alpha = box_alpha
        # The border width of the rectangle.
        self.box_borderw = box_borderw
        # The color of the rectangle.
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
        # The clock font size.
        self.font_size = font_size
        # Specifies whether to display the rectangle.
        self.has_box = has_box
        # The Z-axis layer.
        self.layer = layer
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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
            temp_model = main_models.UpdateStreamingOutShrinkRequestClockWidgetsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.UpdateStreamingOutShrinkRequestClockWidgetsFontColor()
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

class UpdateStreamingOutShrinkRequestClockWidgetsFontColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestClockWidgetsBoxColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestBgColor(DaraModel):
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

class UpdateStreamingOutShrinkRequestBackgrounds(DaraModel):
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
        # The transparency.
        self.alpha = alpha
        # The crop mode. Valid values:
        # - **1**: Crops the image while maintaining the aspect ratio.
        # - **2**: Adds padding to the image while maintaining the aspect ratio.
        # - **3**: Stretches the image to fill the area.
        self.background_crop_mode = background_crop_mode
        # The height.
        # 
        # This parameter is required.
        self.height = height
        # The Z-axis layer.
        self.layer = layer
        # The image URL.
        # 
        # This parameter is required.
        self.url = url
        # The width.
        # 
        # This parameter is required.
        self.width = width
        # The X-coordinate.
        # 
        # This parameter is required.
        self.x = x
        # The Y-coordinate.
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

