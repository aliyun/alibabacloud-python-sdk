# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetDialogAnalysisResultRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        end_time: str = None,
        session_ids: List[str] = None,
        start_time: str = None,
        use_url: bool = None,
    ):
        self.asc = asc
        self.end_time = end_time
        self.session_ids = session_ids
        self.start_time = start_time
        self.use_url = use_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['asc'] = self.asc

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.session_ids is not None:
            result['sessionIds'] = self.session_ids

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.use_url is not None:
            result['useUrl'] = self.use_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asc') is not None:
            self.asc = m.get('asc')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('sessionIds') is not None:
            self.session_ids = m.get('sessionIds')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('useUrl') is not None:
            self.use_url = m.get('useUrl')

        return self

