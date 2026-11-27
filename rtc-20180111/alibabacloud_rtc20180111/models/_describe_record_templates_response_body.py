# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[main_models.DescribeRecordTemplatesResponseBodyTemplates] = None,
        total_num: int = None,
        total_page: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The recording configuration templates.
        self.templates = templates
        # The total number of entries returned.
        self.total_num = total_num
        # The total number of pages returned.
        self.total_page = total_page

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.DescribeRecordTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeRecordTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        background_color: int = None,
        backgrounds: List[main_models.DescribeRecordTemplatesResponseBodyTemplatesBackgrounds] = None,
        clock_widgets: List[main_models.DescribeRecordTemplatesResponseBodyTemplatesClockWidgets] = None,
        create_time: str = None,
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
        oss_file_prefix: str = None,
        task_profile: str = None,
        template_id: str = None,
        watermarks: List[main_models.DescribeRecordTemplatesResponseBodyTemplatesWatermarks] = None,
    ):
        # The RGB value of the background color. Default value: **0** (black). The calculation formula is R + G × 256 + B × 65536. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.background_color = background_color
        # The list of background image information.
        self.backgrounds = backgrounds
        # The list of clock widgets.
        self.clock_widgets = clock_widgets
        # The creation time. The time is displayed in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC time).
        self.create_time = create_time
        # The delay before stopping the recording. Unit: seconds.
        self.delay_stop_time = delay_stop_time
        # Specifies whether to add the timestamp of the TS file to the recorded M3U8 file.
        self.enable_m3u_8date_time = enable_m3u_8date_time
        # The file splitting duration.
        self.file_split_interval = file_split_interval
        # The list of recording file formats. Valid formats include M3U8, FLV, and MP4.
        self.formats = formats
        # The HTTP callback URL for recording events.
        self.http_callback_url = http_callback_url
        # The list of mixed-stream layout IDs used by the recording template.
        self.layout_ids = layout_ids
        # The encoding options.
        self.media_encode = media_encode
        # The name of the Message Service (MNS) queue for recording event callbacks.
        self.mns_queue = mns_queue
        # The name of the recording configuration template.
        self.name = name
        # The name of the Object Storage Service (OSS) bucket where recording files are stored.
        self.oss_bucket = oss_bucket
        # The naming rule for recording files.
        self.oss_file_prefix = oss_file_prefix
        # The task specifications.
        self.task_profile = task_profile
        # The ID of the recording configuration template.
        self.template_id = template_id
        # The list of watermark information.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.oss_file_prefix is not None:
            result['OssFilePrefix'] = self.oss_file_prefix

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
        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')

        self.backgrounds = []
        if m.get('Backgrounds') is not None:
            for k1 in m.get('Backgrounds'):
                temp_model = main_models.DescribeRecordTemplatesResponseBodyTemplatesBackgrounds()
                self.backgrounds.append(temp_model.from_map(k1))

        self.clock_widgets = []
        if m.get('ClockWidgets') is not None:
            for k1 in m.get('ClockWidgets'):
                temp_model = main_models.DescribeRecordTemplatesResponseBodyTemplatesClockWidgets()
                self.clock_widgets.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('OssFilePrefix') is not None:
            self.oss_file_prefix = m.get('OssFilePrefix')

        if m.get('TaskProfile') is not None:
            self.task_profile = m.get('TaskProfile')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.DescribeRecordTemplatesResponseBodyTemplatesWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class DescribeRecordTemplatesResponseBodyTemplatesWatermarks(DaraModel):
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
        # The transparency of the watermark. The value is a normalized percentage. A value of 0 indicates transparent, and a value of 1 indicates completely opaque.
        self.alpha = alpha
        # Specifies whether to display the watermark. Valid values:
        # 
        # - **0** (None): Not displayed.
        # - **1** (Always): Always displayed.
        self.display = display
        # The height of the watermark pane. The value is a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the watermark.
        self.url = url
        # The width of the watermark pane. The value is a normalized percentage.
        self.width = width
        # The X-coordinate of the watermark. The value is a normalized percentage.
        self.x = x
        # The Y-coordinate of the watermark. The value is a normalized percentage.
        self.y = y
        # The stacking order of the watermark. A value of 0 indicates the bottom layer. A value of 1 indicates the layer above the bottom layer, and so on.
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

class DescribeRecordTemplatesResponseBodyTemplatesClockWidgets(DaraModel):
    def __init__(
        self,
        font_color: int = None,
        font_size: int = None,
        font_type: int = None,
        x: float = None,
        y: float = None,
        zorder: int = None,
    ):
        # The text color of the clock (RGB).
        # 
        # The calculation formula is `R + G × 256 + B × 65536`. Valid values for R (red), G (green), and B (blue): **0** to **255**.
        self.font_color = font_color
        # The font size of the clock. Valid values: **(0, 72]**.
        self.font_size = font_size
        # The font type of the clock. Valid values:
        # 
        # - **0** (default): NOTO_SERIF_CJKSC_REGULAR
        # - **1**: ALIBABA_PUHUITI_REGULAR
        # - **2**: ALIBABA_PUHUITI_BOLD
        # - **3**: ALIBABA_PUHUITI_Heavy
        # - **4**: ALIBABA_PUHUITI_LIGHT
        # - **5**: ALIBABA_PUHUITI_MEDIUM
        self.font_type = font_type
        # The X-coordinate of the clock. The value is a normalized percentage.
        self.x = x
        # The Y-coordinate of the clock. The value is a normalized percentage.
        self.y = y
        # The stacking order of the clock. A value of 0 indicates the bottom layer. A value of 1 indicates the layer above the bottom layer, and so on.
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

class DescribeRecordTemplatesResponseBodyTemplatesBackgrounds(DaraModel):
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
        # Specifies whether to display the background image. Valid values:
        # 
        # - **0** (None): Not displayed.
        # - **1** (Always): Always displayed.
        self.display = display
        # The height of the background image pane. The value is a normalized percentage.
        self.height = height
        # The HTTP or HTTPS URL of the background image.
        self.url = url
        # The width of the background image pane. The value is a normalized percentage.
        self.width = width
        # The X-coordinate of the background image. The value is a normalized percentage.
        self.x = x
        # The Y-coordinate of the background image. The value is a normalized percentage.
        self.y = y
        # The stacking order of the background image. A value of 0 indicates the bottom layer. A value of 1 indicates the layer above the bottom layer, and so on.
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

