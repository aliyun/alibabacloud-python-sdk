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
        # The timestamp of the most recent scan, in milliseconds.
        self.last_check_time = last_check_time
        # The request ID.
        self.request_id = request_id
        # The number of virus risks detected on the server.
        self.risk_num = risk_num
        # The asset information scanned by the virus scan node. This parameter is expressed as a character string converted from a JSON array. The following fields are included:
        # - **type**: The Asset Type on which the virus scan is executed. Valid values:
        #     - **groupId**: server group.
        #     - **uuid**: server.
        # - **name**: The name of the server group or server.
        # - **target**: The asset on which the virus scan is executed. The following describes the values of this field:
        #     - If **type** is set to **groupId**, this field specifies the server group ID.
        #     - If **type** is set to **uuid**, this field specifies the UUID of the server.
        self.target_info = target_info
        # The list of UUIDs of the assets.
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

