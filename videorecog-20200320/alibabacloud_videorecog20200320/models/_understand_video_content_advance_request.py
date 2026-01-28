# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class UnderstandVideoContentAdvanceRequest(DaraModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
    ):
        # This parameter is required.
        self.video_urlobject = video_urlobject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_urlobject is not None:
            result['VideoURL'] = self.video_urlobject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_urlobject = m.get('VideoURL')

        return self

