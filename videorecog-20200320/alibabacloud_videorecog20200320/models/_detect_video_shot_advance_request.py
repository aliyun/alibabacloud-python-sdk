# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class DetectVideoShotAdvanceRequest(DaraModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.video_url_object = video_url_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_url_object is not None:
            result['VideoUrl'] = self.video_url_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url_object = m.get('VideoUrl')

        return self

