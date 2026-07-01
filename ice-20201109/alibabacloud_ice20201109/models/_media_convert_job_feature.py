# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertJobFeature(DaraModel):
    def __init__(
        self,
        clip: main_models.MediaConvertJobFeatureClip = None,
        metadata: Dict[str, str] = None,
        watermarks: List[main_models.MediaConvertJobFeatureWatermarks] = None,
    ):
        # Clip settings.
        self.clip = clip
        # Specifies the metadata for the output video container format, provided as JSON key-value pairs. Example: `{"key1":"value1","key2":"value2"}`.
        # 
        # - Maximum key length: 64 characters.
        # 
        # - Maximum value length: 512 characters.
        # 
        # You can add a maximum of four metadata key-value pairs.
        self.metadata = metadata
        # A list of watermark settings to overlay on the video. If specified, these settings override the corresponding parameters in the specified watermark template.
        # 
        # - You can add a maximum of four watermarks per transcoding job.
        self.watermarks = watermarks

    def validate(self):
        if self.clip:
            self.clip.validate()
        if self.watermarks:
            for v1 in self.watermarks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip is not None:
            result['Clip'] = self.clip.to_map()

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        result['Watermarks'] = []
        if self.watermarks is not None:
            for k1 in self.watermarks:
                result['Watermarks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clip') is not None:
            temp_model = main_models.MediaConvertJobFeatureClip()
            self.clip = temp_model.from_map(m.get('Clip'))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        self.watermarks = []
        if m.get('Watermarks') is not None:
            for k1 in m.get('Watermarks'):
                temp_model = main_models.MediaConvertJobFeatureWatermarks()
                self.watermarks.append(temp_model.from_map(k1))

        return self

class MediaConvertJobFeatureWatermarks(DaraModel):
    def __init__(
        self,
        adaptive: str = None,
        border_color: str = None,
        border_width: str = None,
        content: str = None,
        font_alpha: str = None,
        font_color: str = None,
        font_name: str = None,
        font_size: str = None,
        height: str = None,
        template_id: str = None,
        type: str = None,
        width: str = None,
        x: str = None,
        y: str = None,
    ):
        # Specifies whether the font size of the text watermark adapts to the output video resolution.
        # 
        # - `true`: The font size is adaptive.
        # 
        # - `false`: The font size is fixed.
        # 
        # - Default value: `false`.
        self.adaptive = adaptive
        # The border color of the text watermark.
        # 
        # - Default value: `black`.
        self.border_color = border_color
        # The border width of the text watermark.
        # 
        # - Unit: pixels.
        # 
        # - Value range: [0, 4096].
        # 
        # - Default value: `0`.
        self.border_width = border_width
        # The content of the text watermark.
        self.content = content
        # The opacity of the font.
        # 
        # - Value range: (0, 1].
        # 
        # - Default value: `1.0`.
        self.font_alpha = font_alpha
        # The font color of the text watermark.
        # 
        # - Default value: `black`.
        self.font_color = font_color
        # The font name for the text watermark.
        # 
        # - Default value: `SimSun`.
        self.font_name = font_name
        # The font size of the text watermark.
        # 
        # - Value range: (4, 120).
        # 
        # - Default value: `16`.
        self.font_size = font_size
        # The height of the watermark. If specified, this value overrides the corresponding parameter in the watermark template. You can specify the value in two ways:
        # 
        # - As an integer, representing the height in pixels.
        # 
        #   - Unit: pixels.
        # 
        #   - Value range: [8, 4096].
        # 
        # - As a decimal, representing the ratio of the height to the height of the output video.
        # 
        #   - Value range: (0, 1).
        # 
        #   - Supports up to four decimal places, such as `0.9999`. The system truncates additional digits.
        self.height = height
        # The ID of the watermark template.
        self.template_id = template_id
        # The type of the watermark.
        # 
        # - `Text`: A text watermark. You must also set the text watermark parameters.
        # 
        # - `Image`: An image watermark. You must also set the image watermark parameters.
        # 
        # Default value: The system automatically determines the type based on the watermark template.
        self.type = type
        # The width of the watermark. If specified, this value overrides the corresponding parameter in the watermark template. You can specify the value in two ways:
        # 
        # - As an integer, representing the width in pixels.
        # 
        #   - Unit: pixels.
        # 
        #   - Value range: [8, 4096].
        # 
        # - As a decimal, representing the ratio of the width to the width of the output video.
        # 
        #   - Value range: (0, 1).
        # 
        #   - Supports up to four decimal places, such as `0.9999`. The system truncates additional digits.
        self.width = width
        # The horizontal offset of the watermark relative to the output video. If specified, this value overrides the corresponding parameter in the watermark template. You can specify the value in two ways:
        # 
        # - As an integer, representing the offset in pixels.
        # 
        #   - Unit: pixels.
        # 
        #   - Value range: [8, 4096].
        # 
        # - As a decimal, representing the ratio of the offset to the width of the output video.
        # 
        #   - Value range: (0, 1).
        # 
        #   - Supports up to four decimal places, such as `0.9999`. The system truncates additional digits.
        self.x = x
        # The vertical offset of the watermark relative to the output video. If specified, this value overrides the corresponding parameter in the watermark template. You can specify the value in two ways:
        # 
        # - As an integer, representing the offset in pixels.
        # 
        #   - Unit: pixels.
        # 
        #   - Value range: [8, 4096].
        # 
        # - As a decimal, representing the ratio of the offset to the height of the output video.
        # 
        #   - Value range: (0, 1).
        # 
        #   - Supports up to four decimal places, such as `0.9999`. The system truncates additional digits.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive is not None:
            result['Adaptive'] = self.adaptive

        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width is not None:
            result['BorderWidth'] = self.border_width

        if self.content is not None:
            result['Content'] = self.content

        if self.font_alpha is not None:
            result['FontAlpha'] = self.font_alpha

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.font_size is not None:
            result['FontSize'] = self.font_size

        if self.height is not None:
            result['Height'] = self.height

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adaptive') is not None:
            self.adaptive = m.get('Adaptive')

        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidth') is not None:
            self.border_width = m.get('BorderWidth')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FontAlpha') is not None:
            self.font_alpha = m.get('FontAlpha')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('FontSize') is not None:
            self.font_size = m.get('FontSize')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class MediaConvertJobFeatureClip(DaraModel):
    def __init__(
        self,
        config_to_clip_first_part: str = None,
        time_span: main_models.MediaConvertJobFeatureClipTimeSpan = None,
    ):
        # Specifies whether to clip the first segment before concatenation.
        # 
        # - `true`: The system clips the first segment before concatenation and transcoding.
        # 
        # - `false`: The system first concatenates and transcodes the segments, and then clips the resulting video.
        # 
        # - Default value: `false`.
        self.config_to_clip_first_part = config_to_clip_first_part
        # The time span for the clip.
        self.time_span = time_span

    def validate(self):
        if self.time_span:
            self.time_span.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_to_clip_first_part is not None:
            result['ConfigToClipFirstPart'] = self.config_to_clip_first_part

        if self.time_span is not None:
            result['TimeSpan'] = self.time_span.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigToClipFirstPart') is not None:
            self.config_to_clip_first_part = m.get('ConfigToClipFirstPart')

        if m.get('TimeSpan') is not None:
            temp_model = main_models.MediaConvertJobFeatureClipTimeSpan()
            self.time_span = temp_model.from_map(m.get('TimeSpan'))

        return self

class MediaConvertJobFeatureClipTimeSpan(DaraModel):
    def __init__(
        self,
        duration: str = None,
        end: str = None,
        seek: str = None,
    ):
        # Specifies the duration of the clip, relative to the `Seek` time. By default, the clip extends to the end of the video. You can specify either `Duration` or `End`, but not both. If `End` is specified, `Duration` is ignored.
        # 
        # - Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # 
        # - Value range: `[00:00:00.000, 23:59:59.999]` or `[0.000, 86399.999]`.
        # 
        # - Example: `00:01:59.999` or `180.30`.
        self.duration = duration
        # Specifies the end time of the clip. You can specify either `End` or `Duration`, but not both. If `End` is specified, `Duration` is ignored.
        # 
        # - Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # 
        # - Value range: `[00:00:00.000, 23:59:59.999]` or `[0.000, 86399.999]`.
        # 
        # - Example: `00:01:59.999` or `180.30`.
        self.end = end
        # Specifies the start time of the clip. If this parameter is not set, the clip starts from the beginning of the video.
        # 
        # - Format: `hh:mm:ss[.SSS]` or `sssss[.SSS]`.
        # 
        # - Value range: `[00:00:00.000, 23:59:59.999]` or `[0.000, 86399.999]`.
        # 
        # - Example: `00:01:59.999` or `180.30`.
        self.seek = seek

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end is not None:
            result['End'] = self.end

        if self.seek is not None:
            result['Seek'] = self.seek

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Seek') is not None:
            self.seek = m.get('Seek')

        return self

