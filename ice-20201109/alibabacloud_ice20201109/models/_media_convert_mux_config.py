# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertMuxConfig(DaraModel):
    def __init__(
        self,
        segment: main_models.MediaConvertSegment = None,
    ):
        # Shard configuration field. For more information, see Segment details.
        # 
        # This field takes effect only when Container is set to m3u8, hls-fmp4, mpd, or cmaf.
        self.segment = segment

    def validate(self):
        if self.segment:
            self.segment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Segment') is not None:
            temp_model = main_models.MediaConvertSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

