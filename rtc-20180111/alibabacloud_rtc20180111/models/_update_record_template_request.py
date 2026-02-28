# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class UpdateRecordTemplateRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        background_color: int = None,
        backgrounds: List[main_models.UpdateRecordTemplateRequestBackgrounds] = None,
        clock_widgets: List[main_models.UpdateRecordTemplateRequestClockWidgets] = None,
        delay_stop_time: int = None,
        enable_m3u_8date_time: bool = None,
        file_split_interval: int = None,
        formats: List[str] = None,
        http_callback_url: str = None,
        layout_ids: List[int] = None,
        media_encode: int = None,
        mns_queue: str = None,
        name: str = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_file_prefix: str = None,
        owner_id: int = None,
        task_profile: str = None,
        template_id: str = None,
        watermarks: List[main_models.UpdateRecordTemplateRequestWatermarks] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.background_color = background_color
        self.backgrounds = backgrounds
        self.clock_widgets = clock_widgets
        self.delay_stop_time = delay_stop_time
        self.enable_m3u_8date_time = enable_m3u_8date_time
        # This parameter is required.
        self.file_split_interval = file_split_interval
        # This parameter is required.
        self.formats = formats
        self.http_callback_url = http_callback_url
        # This parameter is required.
        self.layout_ids = layout_ids
        # This parameter is required.
        self.media_encode = media_encode
        self.mns_queue = mns_queue
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint
        # This parameter is required.
        self.oss_file_prefix = oss_file_prefix
        self.owner_id = owner_id
        # This parameter is required.
        self.task_profile = task_profile
        # This parameter is required.
        self.template_id = template_id
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

        if self.delay_stop_time is not None:
            result['DelayStopTime'] = self.delay_stop_time

        if self.enable_m3u_8date_time is not None:
            result['EnableM3u8DateTime'] = self.enable_m3u_8date_time

        if self.file_split_interval is not None:
            result['FileSplitInterval'] = self.file_split_interval

        if self.formats is not None:
            result['Formats'] = self.formats

        if self.http_callback_url is not None:
            result['HttpCallbackUrl'] = self.http_callback_url

        if self.layout_ids is not None:
            result['LayoutIds'] = self.layout_ids

        if self.media_encode is not None:
            result['MediaEncode'] = self.media_encode

        if self.mns_queue is not None:
            result['MnsQueue'] = self.mns_queue

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.task_profile is not None:
            result['TaskProfile'] = self.task_profile

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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
                temp_model = main_models.UpdateRecordTemplateRequestBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.UpdateRecordTemplateRequestClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('DelayStopTime') is not None:
            self.delay_stop_time = m.get('DelayStopTime')

        if m.get('EnableM3u8DateTime') is not None:
            self.enable_m3u_8date_time = m.get('EnableM3u8DateTime')

        if m.get('FileSplitInterval') is not None:
            self.file_split_interval = m.get('FileSplitInterval')

        if m.get('Formats') is not None:
            self.formats = m.get('Formats')

        if m.get('HttpCallbackUrl') is not None:
            self.http_callback_url = m.get('HttpCallbackUrl')

        if m.get('LayoutIds') is not None:
            self.layout_ids = m.get('LayoutIds')

        if m.get('MediaEncode') is not None:
            self.media_encode = m.get('MediaEncode')

        if m.get('MnsQueue') is not None:
            self.mns_queue = m.get('MnsQueue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.UpdateRecordTemplateRequestWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class UpdateRecordTemplateRequestWatermarks(DaraModel):
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

class UpdateRecordTemplateRequestClockWidgets(DaraModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
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

class UpdateRecordTemplateRequestBackgrounds(DaraModel):
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

