# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertJobOverwiteParams(DaraModel):
    def __init__(
        self,
        subtitles: List[main_models.MediaConvertJobOverwiteParamsSubtitles] = None,
    ):
        self.subtitles = subtitles

    def validate(self):
        if self.subtitles:
            for v1 in self.subtitles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Subtitles'] = []
        if self.subtitles is not None:
            for k1 in self.subtitles:
                result['Subtitles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitles = []
        if m.get('Subtitles') is not None:
            for k1 in m.get('Subtitles'):
                temp_model = main_models.MediaConvertJobOverwiteParamsSubtitles()
                self.subtitles.append(temp_model.from_map(k1))

        return self

class MediaConvertJobOverwiteParamsSubtitles(DaraModel):
    def __init__(
        self,
        codec: str = None,
    ):
        self.codec = codec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codec is not None:
            result['Codec'] = self.codec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        return self

