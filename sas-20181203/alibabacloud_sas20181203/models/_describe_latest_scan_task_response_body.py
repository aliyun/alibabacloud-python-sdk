# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLatestScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        last_check_time: int = None,
        request_id: str = None,
        risk_num: int = None,
        target_info: str = None,
        uuids: List[str] = None,
    ):
        # The timestamp when the last check was performed. Unit: milliseconds.
        self.last_check_time = last_check_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of virus detection risks on the server.
        self.risk_num = risk_num
        # The applicable scope of the whitelist. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: the type of the applicable scope. Valid values:
        # 
        #     *   **GroupId**: the ID of a server group
        #     *   **Uuid**: the UUID of a server
        # 
        # *   **uuids**: the UUIDs of servers
        # 
        # *   **groupIds**: the IDs of server groups
        # 
        # >  If you leave this parameter empty, all servers are added to the whitelist. If you set the **type** field to **GroupId**, you must also specify the **groupIds** field. If you set the **type** field to **Uuid**, you must also specify the **uuids** field.
        self.target_info = target_info
        # The UUIDs of the assets.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_num is not None:
            result['RiskNum'] = self.risk_num

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskNum') is not None:
            self.risk_num = m.get('RiskNum')

        if m.get('TargetInfo') is not None:
            self.target_info = m.get('TargetInfo')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

