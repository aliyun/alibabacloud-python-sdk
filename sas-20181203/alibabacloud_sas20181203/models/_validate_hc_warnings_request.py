# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateHcWarningsRequest(DaraModel):
    def __init__(
        self,
        check_ids: str = None,
        risk_ids: str = None,
        status: int = None,
        uuids: str = None,
    ):
        # The IDs of check items that you want to verify. Separate multiple IDs with commas (,).
        # > You can use [DescribeCheckWarningSummary](https://help.aliyun.com/document_detail/116179.html) to get IDs of check items.
        self.check_ids = check_ids
        # The IDs of risk items that you want to verify. Separate multiple IDs with commas (,).
        self.risk_ids = risk_ids
        # The status of the check item that you want to verify.
        # 
        # *   1: failed
        # *   3: passed
        # *   5: expired
        self.status = status
        # The UUIDs of the servers on which you want to verify the risk items. Separate multiple UUIDs with commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.risk_ids is not None:
            result['RiskIds'] = self.risk_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('RiskIds') is not None:
            self.risk_ids = m.get('RiskIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

