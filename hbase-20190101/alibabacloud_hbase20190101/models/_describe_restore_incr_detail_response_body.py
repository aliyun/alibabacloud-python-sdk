# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreIncrDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restore_incr_detail: main_models.DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The incremental restoration details.
        self.restore_incr_detail = restore_incr_detail

    def validate(self):
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoreIncrDetail') is not None:
            temp_model = main_models.DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m.get('RestoreIncrDetail'))

        return self

class DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        process: str = None,
        restore_delay: str = None,
        restore_start_ts: str = None,
        restored_ts: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The progress.
        self.process = process
        # The synchronization latency.
        self.restore_delay = restore_delay
        # The synchronization start point.
        self.restore_start_ts = restore_start_ts
        # The synchronization point.
        self.restored_ts = restored_ts
        # The start time.
        self.start_time = start_time
        # The status.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.process is not None:
            result['Process'] = self.process

        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay

        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts

        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')

        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')

        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

