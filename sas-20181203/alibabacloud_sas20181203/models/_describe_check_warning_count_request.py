# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckWarningCountRequest(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        check_id: int = None,
        risk_id: int = None,
        status: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The ID of the check item.
        # 
        # >  You can call the [ListCheckItemWarningSummary](~~ListCheckItemWarningSummary~~) operation to query the IDs of check items.
        self.check_id = check_id
        # The ID of the risk item.
        # 
        # >  You can call the [DescribeCheckWarningSummary](~~DescribeCheckWarningSummary~~) operation to query the IDs of risk items.
        self.risk_id = risk_id
        # The status of the check item. Valid values:
        # 
        # *   **1**: failed
        # *   **2**: verifying
        # *   **3**: passed
        # *   **6**: ignored
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

