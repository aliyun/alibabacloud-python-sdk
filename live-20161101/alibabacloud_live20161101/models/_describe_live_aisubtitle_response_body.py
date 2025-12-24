# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveAISubtitleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        subtitle_configs: main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigs = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the subtitle templates.
        self.subtitle_configs = subtitle_configs

    def validate(self):
        if self.subtitle_configs:
            self.subtitle_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subtitle_configs is not None:
            result['SubtitleConfigs'] = self.subtitle_configs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubtitleConfigs') is not None:
            temp_model = main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigs()
            self.subtitle_configs = temp_model.from_map(m.get('SubtitleConfigs'))

        return self

class DescribeLiveAISubtitleResponseBodySubtitleConfigs(DaraModel):
    def __init__(
        self,
        subtitle_config: List[main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfig] = None,
    ):
        self.subtitle_config = subtitle_config

    def validate(self):
        if self.subtitle_config:
            for v1 in self.subtitle_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubtitleConfig'] = []
        if self.subtitle_config is not None:
            for k1 in self.subtitle_config:
                result['SubtitleConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle_config = []
        if m.get('SubtitleConfig') is not None:
            for k1 in m.get('SubtitleConfig'):
                temp_model = main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfig()
                self.subtitle_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfig(DaraModel):
    def __init__(
        self,
        bg_color: str = None,
        bg_width_normalized: float = None,
        border_width_normalized: float = None,
        description: str = None,
        dst_language: str = None,
        font_color: str = None,
        font_name: str = None,
        font_size_normalized: str = None,
        height: str = None,
        max_lines: int = None,
        position_normalized: main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigPositionNormalized = None,
        rules_refer: main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigRulesRefer = None,
        show_source_lan: int = None,
        src_language: str = None,
        subtitle_id: str = None,
        subtitle_name: str = None,
        width: str = None,
        word_perline: int = None,
    ):
        # The background color of the subtitles.
        self.bg_color = bg_color
        # The size of the background image.
        self.bg_width_normalized = bg_width_normalized
        # The font weight.
        self.border_width_normalized = border_width_normalized
        # The description of the template.
        self.description = description
        # The language to which the subtitles are translated.
        self.dst_language = dst_language
        # The font color.
        self.font_color = font_color
        # The font.
        self.font_name = font_name
        # The font size.
        self.font_size_normalized = font_size_normalized
        # The height of the preview image.
        self.height = height
        # The number of displayed lines.
        self.max_lines = max_lines
        # The position of the subtitles.
        self.position_normalized = position_normalized
        # The ID of the subtitle rule.
        self.rules_refer = rules_refer
        # Indicates whether the source language of the subtitle is displayed.
        self.show_source_lan = show_source_lan
        # The source language of the subtitles.
        self.src_language = src_language
        # The ID of the subtitle template.
        self.subtitle_id = subtitle_id
        # The name of the subtitle template.
        self.subtitle_name = subtitle_name
        # The width of the preview image.
        self.width = width
        # The number of words per line.
        self.word_perline = word_perline

    def validate(self):
        if self.position_normalized:
            self.position_normalized.validate()
        if self.rules_refer:
            self.rules_refer.validate()

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

        if self.position_normalized is not None:
            result['PositionNormalized'] = self.position_normalized.to_map()

        if self.rules_refer is not None:
            result['RulesRefer'] = self.rules_refer.to_map()

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

        if self.word_perline is not None:
            result['WordPerline'] = self.word_perline

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

        if m.get('PositionNormalized') is not None:
            temp_model = main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigPositionNormalized()
            self.position_normalized = temp_model.from_map(m.get('PositionNormalized'))

        if m.get('RulesRefer') is not None:
            temp_model = main_models.DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigRulesRefer()
            self.rules_refer = temp_model.from_map(m.get('RulesRefer'))

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

        if m.get('WordPerline') is not None:
            self.word_perline = m.get('WordPerline')

        return self

class DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigRulesRefer(DaraModel):
    def __init__(
        self,
        rules_id: List[str] = None,
    ):
        self.rules_id = rules_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rules_id is not None:
            result['RulesId'] = self.rules_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RulesId') is not None:
            self.rules_id = m.get('RulesId')

        return self

class DescribeLiveAISubtitleResponseBodySubtitleConfigsSubtitleConfigPositionNormalized(DaraModel):
    def __init__(
        self,
        position: List[float] = None,
    ):
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

