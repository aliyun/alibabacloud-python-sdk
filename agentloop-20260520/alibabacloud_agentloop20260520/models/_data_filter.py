# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DataFilter(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        max_records: int = None,
        provided: Dict[str, Any] = None,
        query: str = None,
        sampling_rate: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.max_records = max_records
        self.provided = provided
        self.query = query
        self.sampling_rate = sampling_rate
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.max_records is not None:
            result['maxRecords'] = self.max_records

        if self.provided is not None:
            result['provided'] = self.provided

        if self.query is not None:
            result['query'] = self.query

        if self.sampling_rate is not None:
            result['samplingRate'] = self.sampling_rate

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('maxRecords') is not None:
            self.max_records = m.get('maxRecords')

        if m.get('provided') is not None:
            self.provided = m.get('provided')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('samplingRate') is not None:
            self.sampling_rate = m.get('samplingRate')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

