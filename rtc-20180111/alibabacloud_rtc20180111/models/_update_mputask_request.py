# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class UpdateMPUTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        background_color: int = None,
        backgrounds: List[main_models.UpdateMPUTaskRequestBackgrounds] = None,
        clock_widgets: List[main_models.UpdateMPUTaskRequestClockWidgets] = None,
        crop_mode: int = None,
        layout_ids: List[int] = None,
        media_encode: int = None,
        mix_mode: int = None,
        owner_id: int = None,
        source_type: str = None,
        stream_type: int = None,
        sub_spec_audio_users: List[str] = None,
        sub_spec_camera_users: List[str] = None,
        sub_spec_share_screen_users: List[str] = None,
        sub_spec_users: List[str] = None,
        task_id: str = None,
        unsub_spec_audio_users: List[str] = None,
        unsub_spec_camera_users: List[str] = None,
        unsub_spec_share_screen_users: List[str] = None,
        user_panes: List[main_models.UpdateMPUTaskRequestUserPanes] = None,
        watermarks: List[main_models.UpdateMPUTaskRequestWatermarks] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.background_color = background_color
        self.backgrounds = backgrounds
        self.clock_widgets = clock_widgets
        self.crop_mode = crop_mode
        self.layout_ids = layout_ids
        self.media_encode = media_encode
        self.mix_mode = mix_mode
        self.owner_id = owner_id
        self.source_type = source_type
        self.stream_type = stream_type
        self.sub_spec_audio_users = sub_spec_audio_users
        self.sub_spec_camera_users = sub_spec_camera_users
        self.sub_spec_share_screen_users = sub_spec_share_screen_users
        self.sub_spec_users = sub_spec_users
        # This parameter is required.
        self.task_id = task_id
        self.unsub_spec_audio_users = unsub_spec_audio_users
        self.unsub_spec_camera_users = unsub_spec_camera_users
        self.unsub_spec_share_screen_users = unsub_spec_share_screen_users
        self.user_panes = user_panes
        self.watermarks = watermarks

    def validate(self):
        if self.backgrounds:
            for v1 in self.backgrounds:
                 if v1:
                    v1.validate()
        if self.clock_widgets:
            for v1 in self.clock_widgets:
                 if v1:
                    v1.validate()
        if self.user_panes:
            for v1 in self.user_panes:
                 if v1:
                    v1.validate()
        if self.watermarks:
            for v1 in self.watermarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color

        result['Backgrounds'] = []
        if self.backgrounds is not None:
            for k1 in self.backgrounds:
                result['Backgrounds'].append(k1.to_map() if k1 else None)

        result['ClockWidgets'] = []
        if self.clock_widgets is not None:
            for k1 in self.clock_widgets:
                result['ClockWidgets'].append(k1.to_map() if k1 else None)

        if self.crop_mode is not None:
            result['CropMode'] = self.crop_mode

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.mix_mode is not None:
            result['MixMode'] = self.mix_mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.sub_spec_audio_users is not None:
            result['SubSpecAudioUsers'] = self.sub_spec_audio_users

        if self.sub_spec_camera_users is not None:
            result['SubSpecCameraUsers'] = self.sub_spec_camera_users

        if self.sub_spec_share_screen_users is not None:
            result['SubSpecShareScreenUsers'] = self.sub_spec_share_screen_users

        if self.sub_spec_users is not None:
            result['SubSpecUsers'] = self.sub_spec_users

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.unsub_spec_audio_users is not None:
            result['UnsubSpecAudioUsers'] = self.unsub_spec_audio_users

        if self.unsub_spec_camera_users is not None:
            result['UnsubSpecCameraUsers'] = self.unsub_spec_camera_users

        if self.unsub_spec_share_screen_users is not None:
            result['UnsubSpecShareScreenUsers'] = self.unsub_spec_share_screen_users

        result['UserPanes'] = []
        if self.user_panes is not None:
            for k1 in self.user_panes:
                result['UserPanes'].append(k1.to_map() if k1 else None)

        result['Watermarks'] = []
        if self.watermarks is not None:
            for k1 in self.watermarks:
                result['Watermarks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.UpdateMPUTaskRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.UpdateMPUTaskRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CropMode') is not None:
            self.crop_mode = m.get('CropMode')

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('MixMode') is not None:
            self.mix_mode = m.get('MixMode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('SubSpecAudioUsers') is not None:
            self.sub_spec_audio_users = m.get('SubSpecAudioUsers')

        if m.get('SubSpecCameraUsers') is not None:
            self.sub_spec_camera_users = m.get('SubSpecCameraUsers')

        if m.get('SubSpecShareScreenUsers') is not None:
            self.sub_spec_share_screen_users = m.get('SubSpecShareScreenUsers')

        if m.get('SubSpecUsers') is not None:
            self.sub_spec_users = m.get('SubSpecUsers')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UnsubSpecAudioUsers') is not None:
            self.unsub_spec_audio_users = m.get('UnsubSpecAudioUsers')

        if m.get('UnsubSpecCameraUsers') is not None:
            self.unsub_spec_camera_users = m.get('UnsubSpecCameraUsers')

        if m.get('UnsubSpecShareScreenUsers') is not None:
            self.unsub_spec_share_screen_users = m.get('UnsubSpecShareScreenUsers')

        self.user_panes = []
        if m.get('UserPanes') is not None:
            for k1 in m.get('UserPanes'):
                temp_model = main_models.UpdateMPUTaskRequestUserPanes()
                self.user_panes.append(temp_model.from_map(k1))

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.UpdateMPUTaskRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class UpdateMPUTaskRequestWatermarks(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.alpha = alpha
        self.display = display
        self.height = height
        self.url = url
        self.width = width
        self.x = x
        self.y = y
        self.zorder = zorder

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

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class UpdateMPUTaskRequestUserPanes(DaraModel):
    def __init__(
        self,
        images: List[main_models.UpdateMPUTaskRequestUserPanesImages] = None,
        pane_id: int = None,
        segment_type: int = None,
        source_type: str = None,
        texts: List[main_models.UpdateMPUTaskRequestUserPanesTexts] = None,
        user_id: str = None,
    ):
        self.images = images
        self.pane_id = pane_id
        self.segment_type = segment_type
        self.source_type = source_type
        self.texts = texts
        self.user_id = user_id

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

        if self.pane_id is not None:
            result['PaneId'] = self.pane_id

        if self.segment_type is not None:
            result['SegmentType'] = self.segment_type

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.UpdateMPUTaskRequestUserPanesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PaneId') is not None:
            self.pane_id = m.get('PaneId')

        if m.get('SegmentType') is not None:
            self.segment_type = m.get('SegmentType')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.UpdateMPUTaskRequestUserPanesTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class UpdateMPUTaskRequestUserPanesTexts(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        border_color: int = None,
        border_width: int = None,
        box: bool = None,
        box_border_width: int = None,
        box_color: int = None,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        text: str = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.alpha = alpha
        self.border_color = border_color
        self.border_width = border_width
        self.box = box
        self.box_border_width = box_border_width
        self.box_color = box_color
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.text = text
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.box is not None:
            result['Box'] = self.box

        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width

        if self.box_color is not None:
            result['BoxColor'] = self.box_color

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.font_type is not None:
            result['FontType'] = self.font_type

        if self.text is not None:
            result['Text'] = self.text

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Box') is not None:
            self.box = m.get('Box')

        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')

        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class UpdateMPUTaskRequestUserPanesImages(DaraModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.display = display
        self.height = height
        self.url = url
        self.width = width
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class UpdateMPUTaskRequestClockWidgets(DaraModel):
    def __init__(
        self,
        alpha: float = None,
        border_color: int = None,
        border_width: int = None,
        box: bool = None,
        box_border_width: int = None,
        box_color: int = None,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.alpha = alpha
        self.border_color = border_color
        self.border_width = border_width
        self.box = box
        self.box_border_width = box_border_width
        self.box_color = box_color
        self.font_color = font_color
        self.font_size = font_size
        self.font_type = font_type
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.box is not None:
            result['Box'] = self.box

        if self.box_border_width is not None:
            result['BoxBorderWidth'] = self.box_border_width

        if self.box_color is not None:
            result['BoxColor'] = self.box_color

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.font_type is not None:
            result['FontType'] = self.font_type

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Box') is not None:
            self.box = m.get('Box')

        if m.get('BoxBorderWidth') is not None:
            self.box_border_width = m.get('BoxBorderWidth')

        if m.get('BoxColor') is not None:
            self.box_color = m.get('BoxColor')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('FontType') is not None:
            self.font_type = m.get('FontType')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

class UpdateMPUTaskRequestBackgrounds(DaraModel):
    def __init__(
        self,
        display: int = None,
        height: float = None,
        url: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        self.display = display
        self.height = height
        self.url = url
        self.width = width
        self.x = x
        self.y = y
        self.zorder = zorder

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.height is not None:
            result['Height'] = self.height

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.zorder is not None:
            result['ZOrder'] = self.zorder

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('ZOrder') is not None:
            self.zorder = m.get('ZOrder')

        return self

