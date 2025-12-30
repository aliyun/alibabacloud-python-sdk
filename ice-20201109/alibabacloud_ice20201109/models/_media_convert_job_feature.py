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
        self.clip = clip
        self.metadata = metadata
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
        self.adaptive = adaptive
        self.border_color = border_color
        self.border_width = border_width
        self.content = content
        self.font_alpha = font_alpha
        self.font_color = font_color
        self.font_name = font_name
        self.font_size = font_size
        self.height = height
        self.template_id = template_id
        self.type = type
        self.width = width
        self.x = x
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
        self.config_to_clip_first_part = config_to_clip_first_part
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
        self.duration = duration
        self.end = end
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

