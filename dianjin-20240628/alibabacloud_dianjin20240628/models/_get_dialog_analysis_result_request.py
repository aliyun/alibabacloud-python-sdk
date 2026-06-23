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
        # Whether to sort in ascending order. Default is true, which sorts by session creation time in ascending order. If false, sorts in descending order.
        self.asc = asc
        # The end time, which must be in yyyy-MM-dd HH:mm:ss format. If sessionIds are provided, the system queries session analysis results based on these IDs.
        self.end_time = end_time
        # Session ID list. When useUrl is true, the response includes OSS URLs. You can specify up to 1000 sessions. If you specify more than 1000, only the first 1000 are processed. When useUrl is false, the response includes full analysis results. You can specify up to 10 sessions. If you specify more than 10, only the first 10 are processed. This parameter is optional. If sessionIds is empty, the API retrieves results for sessions created between startTime and endTime. If sessionIds is not empty, the API retrieves results for the specified sessions. You cannot leave both sessionIds and the time range empty.
        self.session_ids = session_ids
        # Start time in yyyy-MM-dd HH:mm:ss format. If sessionIds is not empty, you can query the session analysis results using the specified session IDs.
        self.start_time = start_time
        # Whether to return an OSS URL instead of full analysis results. If true, the response includes an OSS URL that expires in one hour. Default is true. Supports up to 1000 sessions. If you specify more than 1000, only the first 1000 are processed. If false, the response includes full analysis results. Supports up to 10 sessions. If you specify more than 10, only the first 10 are processed.
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

