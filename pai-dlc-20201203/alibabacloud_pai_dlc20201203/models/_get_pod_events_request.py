# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPodEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        max_events_num: int = None,
        pod_uid: str = None,
        start_time: str = None,
    ):
        # The end time (UTC).
        self.end_time = end_time
        # The maximum number of events that can be returned.
        self.max_events_num = max_events_num
        # The node UID. Call [GetJob](https://help.aliyun.com/document_detail/459677.html) to get the node UID.
        self.pod_uid = pod_uid
        # The start time (UTC).
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

        if self.max_events_num is not None:
            result['MaxEventsNum'] = self.max_events_num

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxEventsNum') is not None:
            self.max_events_num = m.get('MaxEventsNum')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

