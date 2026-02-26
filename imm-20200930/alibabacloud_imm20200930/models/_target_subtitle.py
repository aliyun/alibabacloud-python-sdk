# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class TargetSubtitle(DaraModel):
    def __init__(
        self,
        disable_subtitle: bool = None,
        extract_subtitle: main_models.TargetSubtitleExtractSubtitle = None,
        stream: List[int] = None,
    ):
        # Specifies whether to disable subtitle generation. Valid values:
        # 
        # *   true
        # *   false (default)
        # 
        # >  If you call the GenerateVideoPlaylist operation and subtitles are required, you must set this parameter to false.
        self.disable_subtitle = disable_subtitle
        # The subtitle extraction settings.
        # 
        # >  The GenerateVideoPlaylist operation does not support this parameter.
        self.extract_subtitle = extract_subtitle
        # The index numbers of subtitle streams that need to be processed. If you set this parameter to null (default) or a value greater than 100, all subtitle streams are processed.
        # 
        # *   For example, you can set the parameter to `[0,1]` to process subtitle streams with index numbers 0 and 1, `[1]` to process only the subtitle stream with the index number 1, and `[101]` to process all subtitle streams.
        # 
        # >  If you specify an index number but no subtitle stream with the index number is found, the index number is ignored.
        self.stream = stream

    def validate(self):
        if self.extract_subtitle:
            self.extract_subtitle.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_subtitle is not None:
            result['DisableSubtitle'] = self.disable_subtitle

        if self.extract_subtitle is not None:
            result['ExtractSubtitle'] = self.extract_subtitle.to_map()

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableSubtitle') is not None:
            self.disable_subtitle = m.get('DisableSubtitle')

        if m.get('ExtractSubtitle') is not None:
            temp_model = main_models.TargetSubtitleExtractSubtitle()
            self.extract_subtitle = temp_model.from_map(m.get('ExtractSubtitle'))

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

class TargetSubtitleExtractSubtitle(DaraModel):
    def __init__(
        self,
        format: str = None,
        uri: str = None,
    ):
        # The format of the extracted subtitle file. Valid values:
        # 
        # *   ass
        # *   srt
        # *   webvtt
        self.format = format
        # The prefix of the OSS URI where the extracted subtitles are stored. The OSS URI is in the oss://bucket/object format, where bucket specifies the name of the OSS bucket that is in the same region as the current project and object specifies the full file path that includes the file name extension.
        # 
        # *   Example: If the prefix is oss://examplebucket/outputSubtitle, an output subtitle file has a URI in the format of oss://examplebucket/outputSubitile_${index}.${ext}. In the URI format, ${ext} is the file name extension of the output subtitle file, and ${index} is the same 0-based index number as that of the corresponding source subtitle stream file.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

