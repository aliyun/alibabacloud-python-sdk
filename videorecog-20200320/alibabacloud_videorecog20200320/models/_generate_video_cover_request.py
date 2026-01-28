# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateVideoCoverRequest(DaraModel):
    def __init__(
        self,
        is_gif: bool = None,
        video_url: str = None,
    ):
        # This parameter is required.
        self.is_gif = is_gif
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_gif is not None:
            result['IsGif'] = self.is_gif

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGif') is not None:
            self.is_gif = m.get('IsGif')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

