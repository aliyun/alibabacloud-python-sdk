# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableRecoveryTimeResponseBody(DaraModel):
    def __init__(
        self,
        cross_backup_id: int = None,
        recovery_begin_time: str = None,
        recovery_end_time: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The ID of the cross-region data backup file.
        self.cross_backup_id = cross_backup_id
        # The start time from which data can be restored. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.recovery_begin_time = recovery_begin_time
        # The end time to which data can be restored. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.recovery_end_time = recovery_end_time
        # The region where the source instance resides.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_backup_id is not None:
            result['CrossBackupId'] = self.cross_backup_id

        if self.recovery_begin_time is not None:
            result['RecoveryBeginTime'] = self.recovery_begin_time

        if self.recovery_end_time is not None:
            result['RecoveryEndTime'] = self.recovery_end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossBackupId') is not None:
            self.cross_backup_id = m.get('CrossBackupId')

        if m.get('RecoveryBeginTime') is not None:
            self.recovery_begin_time = m.get('RecoveryBeginTime')

        if m.get('RecoveryEndTime') is not None:
            self.recovery_end_time = m.get('RecoveryEndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

