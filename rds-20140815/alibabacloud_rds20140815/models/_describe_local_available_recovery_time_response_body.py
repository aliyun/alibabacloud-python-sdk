# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLocalAvailableRecoveryTimeResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        recovery_begin_time: str = None,
        recovery_end_time: str = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The start of the time range to which the instance can be restored.
        self.recovery_begin_time = recovery_begin_time
        # The end of the time range to which the instance can be restored.
        self.recovery_end_time = recovery_end_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.recovery_begin_time is not None:
            result['RecoveryBeginTime'] = self.recovery_begin_time

        if self.recovery_end_time is not None:
            result['RecoveryEndTime'] = self.recovery_end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RecoveryBeginTime') is not None:
            self.recovery_begin_time = m.get('RecoveryBeginTime')

        if m.get('RecoveryEndTime') is not None:
            self.recovery_end_time = m.get('RecoveryEndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

