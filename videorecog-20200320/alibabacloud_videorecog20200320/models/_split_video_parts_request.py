# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SplitVideoPartsRequest(DaraModel):
    def __init__(
        self,
        max_time: int = None,
        min_time: int = None,
        template: str = None,
        video_url: str = None,
    ):
        self.max_time = max_time
        self.min_time = min_time
        self.template = template
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_time is not None:
            result['MaxTime'] = self.max_time

        if self.min_time is not None:
            result['MinTime'] = self.min_time

        if self.template is not None:
            result['Template'] = self.template

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')

        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

