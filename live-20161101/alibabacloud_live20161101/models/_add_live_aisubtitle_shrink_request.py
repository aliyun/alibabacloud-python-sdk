# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveAISubtitleShrinkRequest(DaraModel):
    def __init__(
        self,
        bg_color: str = None,
        bg_width_normalized: float = None,
        border_width_normalized: float = None,
        copy_from: str = None,
        description: str = None,
        dst_language: str = None,
        font_color: str = None,
        font_name: str = None,
        font_size_normalized: float = None,
        height: str = None,
        max_lines: int = None,
        owner_id: int = None,
        position_normalized_shrink: str = None,
        region_id: str = None,
        show_source_lan: bool = None,
        src_language: str = None,
        subtitle_name: str = None,
        width: str = None,
        word_per_line: int = None,
    ):
        # The background color of the subtitles, which is an RGBA value.
        self.bg_color = bg_color
        # The background size of the subtitles. Valid values: [0,1].
        self.bg_width_normalized = bg_width_normalized
        # The font weight. Valid values: [0,1].
        self.border_width_normalized = border_width_normalized
        # The subtitle template that you copy. Set the value to the name of the subtitle template.
        self.copy_from = copy_from
        # The custom description of the subtitle template. The description can be up to 128 characters in length and can contain letters, digits, and special characters.
        self.description = description
        # The target language. Valid values:
        #  - en-US: English 
        # - zh-CN: Chinese 
        # - es-ES: Spanish 
        # - ru-RU: Russian
        self.dst_language = dst_language
        # The font color, which is an RGBA value.
        self.font_color = font_color
        # The font. Valid values:
        # - KaiTi (default)
        # - AlibabaPuHuiTi-Regular
        # - AlibabaPuHuiTi-Bold
        # - AlibabaPuHuiTi-Light
        # - NotoSansHans-Regular
        # - NotoSansHans-Bold
        # - NotoSansHans-Light
        self.font_name = font_name
        # The font size. Valid values: [0,1].
        # 
        # This parameter is required.
        self.font_size_normalized = font_size_normalized
        # The preview height. Unit: pixels.
        # The following specifications of preview width × preview height are supported: 
        # - Landscape low definition 360p (640×360) 
        # - Portrait low definition 360p (360×640)
        # - Landscape standard definition 480p (854×480)
        # - Portrait standard definition 480p (480×854)
        # - Landscape high definition 720p (1280×720)
        # - Portrait high definition 720p (720×1280)
        # - Landscape ultra-high definition 1080p (1920×1080)
        # - Portrait ultra-high definition 1080p (1080×1920)
        self.height = height
        # The number of displayed lines.
        self.max_lines = max_lines
        self.owner_id = owner_id
        # The position of the subtitles. The value is a pair of coordinates for which the origin of the x and y axes is the lower-left corner of the screen.
        # 
        # This parameter is required.
        self.position_normalized_shrink = position_normalized_shrink
        self.region_id = region_id
        # Specifies whether to display the source language. Default value: false.
        self.show_source_lan = show_source_lan
        # The source language. Valid values:
        #  - en-US: English 
        # - zh-CN: Chinese 
        # - ru-RU: Russian
        # 
        # This parameter is required.
        self.src_language = src_language
        # The name of the subtitle template. The name can contain only digits, letters, and hyphens (-). The name cannot start with a hyphen.
        # 
        # This parameter is required.
        self.subtitle_name = subtitle_name
        # The preview width. Unit: pixels.
        self.width = width
        # The number of words displayed per line. Valid values: integers from 1 to 500.
        # 
        # This parameter is required.
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

        if self.copy_from is not None:
            result['CopyFrom'] = self.copy_from

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

        if self.position_normalized_shrink is not None:
            result['PositionNormalized'] = self.position_normalized_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_source_lan is not None:
            result['ShowSourceLan'] = self.show_source_lan

        if self.src_language is not None:
            result['SrcLanguage'] = self.src_language

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

        if m.get('CopyFrom') is not None:
            self.copy_from = m.get('CopyFrom')

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
            self.position_normalized_shrink = m.get('PositionNormalized')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowSourceLan') is not None:
            self.show_source_lan = m.get('ShowSourceLan')

        if m.get('SrcLanguage') is not None:
            self.src_language = m.get('SrcLanguage')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('WordPerLine') is not None:
            self.word_per_line = m.get('WordPerLine')

        return self

