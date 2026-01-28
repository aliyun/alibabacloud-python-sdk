# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnderstandVideoContentRequest(DaraModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_url is not None:
            result['VideoURL'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')

        return self

