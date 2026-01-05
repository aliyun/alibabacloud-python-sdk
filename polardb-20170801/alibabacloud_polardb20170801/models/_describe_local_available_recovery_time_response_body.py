# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLocalAvailableRecoveryTimeResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        recovery_begin_time: str = None,
        recovery_end_time: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.recovery_begin_time = recovery_begin_time
        self.recovery_end_time = recovery_end_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.recovery_begin_time is not None:
            result['RecoveryBeginTime'] = self.recovery_begin_time

        if self.recovery_end_time is not None:
            result['RecoveryEndTime'] = self.recovery_end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RecoveryBeginTime') is not None:
            self.recovery_begin_time = m.get('RecoveryBeginTime')

        if m.get('RecoveryEndTime') is not None:
            self.recovery_end_time = m.get('RecoveryEndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

