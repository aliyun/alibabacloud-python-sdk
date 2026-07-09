# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DataFilter(DaraModel):
    def __init__(
        self,
        max_records: int = None,
        provided: Dict[str, Any] = None,
        query: str = None,
        sampling_rate: int = None,
    ):
        # The maximum number of evaluation records. This takes effect for both backfill and continuous runs. If not specified, the backend does not write a default value.
        self.max_records = max_records
        # The one-time temporary evaluation input content, primarily used for oneshot tasks. The value is stored as a string. Object or array values are serialized to a JSON string.
        self.provided = provided
        # The data query filter condition. This takes effect together with the evaluator-level filters.query. In Trace scenarios, you can specify filter expressions such as service name, environment, or labels.
        self.query = query
        # The sampling rate percentage. Valid values: 0 to 100. A value of 0 or not specified indicates no sampling. A value of 100 indicates full data. If the value is less than 100, random sampling is applied first, and then the maxRecords limit is applied.
        self.sampling_rate = sampling_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_records is not None:
            result['maxRecords'] = self.max_records

        if self.provided is not None:
            result['provided'] = self.provided

        if self.query is not None:
            result['query'] = self.query

        if self.sampling_rate is not None:
            result['samplingRate'] = self.sampling_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRecords') is not None:
            self.max_records = m.get('maxRecords')

        if m.get('provided') is not None:
            self.provided = m.get('provided')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('samplingRate') is not None:
            self.sampling_rate = m.get('samplingRate')

        return self

