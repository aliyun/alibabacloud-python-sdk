# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoReadSummaryOption(DaraModel):
    def __init__(
        self,
        summarize: bool = None,
    ):
        self.summarize = summarize

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summarize is not None:
            result['Summarize'] = self.summarize

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summarize') is not None:
            self.summarize = m.get('Summarize')

        return self

