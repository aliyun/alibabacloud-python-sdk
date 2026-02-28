# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class ModifyViewLayoutShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        backgrounds: List[main_models.ModifyViewLayoutShrinkRequestBackgrounds] = None,
        channel_id: str = None,
        clock_widgets: List[main_models.ModifyViewLayoutShrinkRequestClockWidgets] = None,
        images: List[main_models.ModifyViewLayoutShrinkRequestImages] = None,
        layout_specified_users_shrink: str = None,
        panes: List[main_models.ModifyViewLayoutShrinkRequestPanes] = None,
        task_id: str = None,
        template_id: str = None,
        texts: List[main_models.ModifyViewLayoutShrinkRequestTexts] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.backgrounds = backgrounds
        # This parameter is required.
        self.channel_id = channel_id
        self.clock_widgets = clock_widgets
        self.images = images
        self.layout_specified_users_shrink = layout_specified_users_shrink
        self.panes = panes
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.template_id = template_id
        self.texts = texts

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
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

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k1 in self.clock_widgets:
                result['ClockWidgets'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.ModifyViewLayoutShrinkRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('LayoutSpecifiedUsers') is not None:
            self.layout_specified_users_shrink = m.get('LayoutSpecifiedUsers')

        self.panes = []
        if m.get('Panes') is not None:
            for k1 in m.get('Panes'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestPanes()
                self.panes.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestTexts()
                self.texts.append(temp_model.from_map(k1))

        return self

class ModifyViewLayoutShrinkRequestTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.ModifyViewLayoutShrinkRequestTextsBoxColor = None,
        font: int = None,
        font_color: main_models.ModifyViewLayoutShrinkRequestTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.texture = texture
        # This parameter is required.
        self.x = x
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
            temp_model = main_models.ModifyViewLayoutShrinkRequestTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.ModifyViewLayoutShrinkRequestTextsFontColor()
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

class ModifyViewLayoutShrinkRequestTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestPanes(DaraModel):
    def __init__(
        self,
        images: List[main_models.ModifyViewLayoutShrinkRequestPanesImages] = None,
        pane_crop_mode: int = None,
        pane_id: str = None,
        source: str = None,
        source_type: str = None,
        texts: List[main_models.ModifyViewLayoutShrinkRequestPanesTexts] = None,
    ):
        self.images = images
        self.pane_crop_mode = pane_crop_mode
        # This parameter is required.
        self.pane_id = pane_id
        self.source = source
        self.source_type = source_type
        self.texts = texts

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.pane_crop_mode is not None:
            result['PaneCropMode'] = self.pane_crop_mode

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneCropMode') is not None:
            self.pane_crop_mode = m.get('PaneCropMode')

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.ModifyViewLayoutShrinkRequestPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        return self

class ModifyViewLayoutShrinkRequestPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.ModifyViewLayoutShrinkRequestPanesTextsBoxColor = None,
        font: int = None,
        font_color: main_models.ModifyViewLayoutShrinkRequestPanesTextsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        texture: str = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.texture = texture
        # This parameter is required.
        self.x = x
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
            temp_model = main_models.ModifyViewLayoutShrinkRequestPanesTextsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.ModifyViewLayoutShrinkRequestPanesTextsFontColor()
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

class ModifyViewLayoutShrinkRequestPanesTextsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestPanesTextsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestPanesImages(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        height: float = None,
        layer: int = None,
        pane_image_crop_mode: int = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.alpha = alpha
        # This parameter is required.
        self.height = height
        self.layer = layer
        self.pane_image_crop_mode = pane_image_crop_mode
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
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

class ModifyViewLayoutShrinkRequestImages(DaraModel):
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
        self.alpha = alpha
        # This parameter is required.
        self.height = height
        self.image_crop_mode = image_crop_mode
        self.layer = layer
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
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

class ModifyViewLayoutShrinkRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        box_alpha: float = None,
        box_borderw: int = None,
        box_color: main_models.ModifyViewLayoutShrinkRequestClockWidgetsBoxColor = None,
        font: int = None,
        font_color: main_models.ModifyViewLayoutShrinkRequestClockWidgetsFontColor = None,
        font_size: int = None,
        has_box: bool = None,
        layer: int = None,
        x: float = None,
        y: float = None,
        zone: int = None,
    ):
        self.alpha = alpha
        self.box_alpha = box_alpha
        self.box_borderw = box_borderw
        self.box_color = box_color
        self.font = font
        self.font_color = font_color
        self.font_size = font_size
        self.has_box = has_box
        self.layer = layer
        # This parameter is required.
        self.x = x
        # This parameter is required.
        self.y = y
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
            temp_model = main_models.ModifyViewLayoutShrinkRequestClockWidgetsBoxColor()
            self.box_color = temp_model.from_map(m.get('BoxColor'))

        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('FontColor') is not None:
            temp_model = main_models.ModifyViewLayoutShrinkRequestClockWidgetsFontColor()
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

class ModifyViewLayoutShrinkRequestClockWidgetsFontColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestClockWidgetsBoxColor(DaraModel):
    def __init__(
        self,
        b: int = None,
        g: int = None,
        r: int = None,
    ):
        # B。
        self.b = b
        # G。
        self.g = g
        # R。
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

class ModifyViewLayoutShrinkRequestBackgrounds(DaraModel):
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
        self.alpha = alpha
        self.background_crop_mode = background_crop_mode
        # This parameter is required.
        self.height = height
        self.layer = layer
        # This parameter is required.
        self.url = url
        # This parameter is required.
        self.width = width
        # This parameter is required.
        self.x = x
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

