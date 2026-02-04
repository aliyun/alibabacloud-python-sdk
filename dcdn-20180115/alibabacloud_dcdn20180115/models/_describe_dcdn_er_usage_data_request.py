# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnErUsageDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        routine_id: str = None,
        spec: str = None,
        split_by: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The ID of the routine.
        self.routine_id = routine_id
        # The specification of the routine. Valid values:
        # 
        # *   5ms
        # *   50ms
        # *   100ms
        self.spec = spec
        # Specifies how the results are grouped. If you set this parameter to routine, the returned results are grouped based on the routine ID. If you set this parameter to spec, the returned results are grouped based on the routine specification.
        # 
        # > If you leave this parameter empty, the returned results are not grouped.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.routine_id is not None:
            result['RoutineID'] = self.routine_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RoutineID') is not None:
            self.routine_id = m.get('RoutineID')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

