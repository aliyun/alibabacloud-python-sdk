# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateLiveAISubtitleRequest(DaraModel):
    def __init__(
        self,
        bg_color: str = None,
        bg_width_normalized: float = None,
        border_width_normalized: float = None,
        description: str = None,
        dst_language: str = None,
        font_color: str = None,
        font_name: str = None,
        font_size_normalized: float = None,
        height: str = None,
        max_lines: int = None,
        owner_id: int = None,
        position_normalized: List[float] = None,
        region_id: str = None,
        show_source_lan: bool = None,
        src_language: str = None,
        subtitle_id: str = None,
        subtitle_name: str = None,
        width: str = None,
        word_per_line: int = None,
    ):
        # The background color of the subtitles. Color format: RGBA.
        self.bg_color = bg_color
        # The size of the background box. Valid values: [0,1].
        self.bg_width_normalized = bg_width_normalized
        # The font weight. Valid values: [0,1].
        self.border_width_normalized = border_width_normalized
        # The description of the subtitle template. The description can be up to 128 characters in length and can contain letters, digits, and special characters.
        self.description = description
        # The target language. Valid values:
        # 
        # *   en-US: English
        # *   zh-CN: Chinese
        # *   es-ES: Spanish
        # *   ru-RU: Russian
        self.dst_language = dst_language
        # The font color. Color format: RGBA.
        self.font_color = font_color
        # The font. Valid values:
        # 
        # *   KaiTi (default)
        # *   AlibabaPuHuiTi-Regular
        # *   AlibabaPuHuiTi-Bold
        # *   AlibabaPuHuiTi-Light
        # *   NotoSansHans-Regular
        # *   NotoSansHans-Bold
        # *   NotoSansHans-Light
        self.font_name = font_name
        # The font size. Valid values: [0,1].
        self.font_size_normalized = font_size_normalized
        # The height of the preview. Unit: pixels.
        # 
        # The following preview specifications (width x height) are supported:
        # 
        # *   360p (640 x 360)
        # *   360p (360 x 640)
        # *   480p (854 x 480)
        # *   480p (480 x 854)
        # *   720p (1280 x 720)
        # *   720p (720 x 1280)
        # *   1080p (1920 x 1080)
        # *   1080p (1080 x 1920)
        self.height = height
        # The number of displayed lines.
        self.max_lines = max_lines
        self.owner_id = owner_id
        # The position of the subtitles relative to the lower-left corner of the screen. The value is a pair of coordinates.
        self.position_normalized = position_normalized
        self.region_id = region_id
        # Specifies whether to display the source language. Valid values: true and false. Default value: false.
        self.show_source_lan = show_source_lan
        # The source language. Valid values:
        # 
        # *   en-US: English
        # *   zh-CN: Chinese
        # *   ru-RU: Russian
        self.src_language = src_language
        # The ID of the subtitle template.
        # 
        # This parameter is required.
        self.subtitle_id = subtitle_id
        # The name of the subtitle template. The name can contain digits, letters, and hyphens (-) but cannot start with a hyphen (-).
        self.subtitle_name = subtitle_name
        # The width of the preview. Unit: pixels.
        self.width = width
        # The number of characters per line. Valid values: 1 to 500.
        self.word_per_line = word_per_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bg_color is not None:
            result['BgColor'] = self.bg_color

        if self.bg_width_normalized is not None:
            result['BgWidthNormalized'] = self.bg_width_normalized

        if self.border_width_normalized is not None:
            result['BorderWidthNormalized'] = self.border_width_normalized

        if self.description is not None:
            result['Description'] = self.description

        if self.dst_language is not None:
            result['DstLanguage'] = self.dst_language

        if self.font_color is not None:
            result['FontColor'] = self.font_color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.font_size_normalized is not None:
            result['FontSizeNormalized'] = self.font_size_normalized

        if self.height is not None:
            result['Height'] = self.height

        if self.max_lines is not None:
            result['MaxLines'] = self.max_lines

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.position_normalized is not None:
            result['PositionNormalized'] = self.position_normalized

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_source_lan is not None:
            result['ShowSourceLan'] = self.show_source_lan

        if self.src_language is not None:
            result['SrcLanguage'] = self.src_language

        if self.subtitle_id is not None:
            result['SubtitleId'] = self.subtitle_id

        if self.subtitle_name is not None:
            result['SubtitleName'] = self.subtitle_name

        if self.width is not None:
            result['Width'] = self.width

        if self.word_per_line is not None:
            result['WordPerLine'] = self.word_per_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgColor') is not None:
            self.bg_color = m.get('BgColor')

        if m.get('BgWidthNormalized') is not None:
            self.bg_width_normalized = m.get('BgWidthNormalized')

        if m.get('BorderWidthNormalized') is not None:
            self.border_width_normalized = m.get('BorderWidthNormalized')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DstLanguage') is not None:
            self.dst_language = m.get('DstLanguage')

        if m.get('FontColor') is not None:
            self.font_color = m.get('FontColor')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('FontSizeNormalized') is not None:
            self.font_size_normalized = m.get('FontSizeNormalized')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MaxLines') is not None:
            self.max_lines = m.get('MaxLines')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PositionNormalized') is not None:
            self.position_normalized = m.get('PositionNormalized')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowSourceLan') is not None:
            self.show_source_lan = m.get('ShowSourceLan')

        if m.get('SrcLanguage') is not None:
            self.src_language = m.get('SrcLanguage')

        if m.get('SubtitleId') is not None:
            self.subtitle_id = m.get('SubtitleId')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WordPerLine') is not None:
            self.word_per_line = m.get('WordPerLine')

        return self

