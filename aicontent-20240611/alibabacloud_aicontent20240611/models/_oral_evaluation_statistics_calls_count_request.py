# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OralEvaluationStatisticsCallsCountRequest(DaraModel):
    def __init__(
        self,
        application_access_id: str = None,
        end_time: str = None,
        granularity: str = None,
        project_id: str = None,
        start_time: str = None,
    ):
        # appId,appkey
        self.application_access_id = application_access_id
        self.end_time = end_time
        self.granularity = granularity
        self.project_id = project_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_access_id is not None:
            result['applicationAccessId'] = self.application_access_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationAccessId') is not None:
            self.application_access_id = m.get('applicationAccessId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

