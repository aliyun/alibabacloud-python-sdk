# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class DescribeOpenBackupSetResponseBody(DaraModel):
    def __init__(
        self,
        data: Any = None,
        request_id: str = None,
    ):
        # The struct that contains instance topology information and backup set download links.
        # > The canBinlogRecoverToTimeUTC field indicates the point in time to which the backup set can be restored. This point in time is close to the RestoreTime input parameter. Because the latest local binlog of a DN may not have been uploaded, restoration to the desired point in time is not guaranteed.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

