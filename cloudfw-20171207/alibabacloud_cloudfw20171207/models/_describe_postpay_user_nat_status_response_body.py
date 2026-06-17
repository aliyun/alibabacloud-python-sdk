# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePostpayUserNatStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
        unprotected_date: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The status of the NAT border firewall. Valid values:
        # 
        # - **open**: The feature is enabled.
        # 
        # - **init**: The feature is being enabled.
        # 
        # - **closed**: The feature is disabled.
        self.status = status
        # The number of days that protection was disabled. This parameter is returned only when the NAT border firewall is enabled.
        self.unprotected_date = unprotected_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.unprotected_date is not None:
            result['UnprotectedDate'] = self.unprotected_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnprotectedDate') is not None:
            self.unprotected_date = m.get('UnprotectedDate')

        return self

