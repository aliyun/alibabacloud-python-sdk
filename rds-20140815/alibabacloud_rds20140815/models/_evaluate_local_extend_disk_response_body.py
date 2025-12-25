# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluateLocalExtendDiskResponseBody(DaraModel):
    def __init__(
        self,
        available: str = None,
        dbinstance_id: str = None,
        dbinstance_trans_type: str = None,
        local_upgrade_disk_limit: int = None,
        request_id: str = None,
    ):
        # Indicates whether the instance is available. Valid values: true and false.
        self.available = available
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The data transfer type supported by the instance.
        self.dbinstance_trans_type = dbinstance_trans_type
        # The maximum value of the local disk. Unit: GB.
        self.local_upgrade_disk_limit = local_upgrade_disk_limit
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_trans_type is not None:
            result['DBInstanceTransType'] = self.dbinstance_trans_type

        if self.local_upgrade_disk_limit is not None:
            result['LocalUpgradeDiskLimit'] = self.local_upgrade_disk_limit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceTransType') is not None:
            self.dbinstance_trans_type = m.get('DBInstanceTransType')

        if m.get('LocalUpgradeDiskLimit') is not None:
            self.local_upgrade_disk_limit = m.get('LocalUpgradeDiskLimit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

