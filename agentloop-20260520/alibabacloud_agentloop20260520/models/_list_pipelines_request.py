# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelinesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pipeline_name: str = None,
        schedule_status: str = None,
        schedule_type: str = None,
        sink_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.pipeline_name = pipeline_name
        self.schedule_status = schedule_status
        self.schedule_type = schedule_type
        self.sink_name = sink_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.schedule_status is not None:
            result['scheduleStatus'] = self.schedule_status

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.sink_name is not None:
            result['sinkName'] = self.sink_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('scheduleStatus') is not None:
            self.schedule_status = m.get('scheduleStatus')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('sinkName') is not None:
            self.sink_name = m.get('sinkName')

        return self

