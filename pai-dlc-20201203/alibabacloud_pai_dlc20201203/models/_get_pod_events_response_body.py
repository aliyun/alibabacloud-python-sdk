# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetPodEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[str] = None,
        job_id: str = None,
        pod_id: str = None,
        pod_uid: str = None,
        request_id: str = None,
    ):
        # The events returned.
        self.events = events
        # The job ID.
        self.job_id = job_id
        # The node ID.
        # 
        # This parameter is required.
        self.pod_id = pod_id
        # The node UID.
        self.pod_uid = pod_uid
        # The request ID, which can be used for troubleshooting.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.events is not None:
            result['Events'] = self.events

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

