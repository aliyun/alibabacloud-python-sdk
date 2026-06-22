# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PPTDetails(DaraModel):
    def __init__(
        self,
        image_path: str = None,
        pptshot_index: int = None,
        start_time: int = None,
    ):
        # The URL of the captured slide image, which is stored in an Object Storage Service (OSS) bucket.
        self.image_path = image_path
        # The zero-based index of the slide in the sequence of detected slides.
        self.pptshot_index = pptshot_index
        # The start time of the slide, in milliseconds, from the beginning of the video.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_path is not None:
            result['ImagePath'] = self.image_path

        if self.pptshot_index is not None:
            result['PPTShotIndex'] = self.pptshot_index

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagePath') is not None:
            self.image_path = m.get('ImagePath')

        if m.get('PPTShotIndex') is not None:
            self.pptshot_index = m.get('PPTShotIndex')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

