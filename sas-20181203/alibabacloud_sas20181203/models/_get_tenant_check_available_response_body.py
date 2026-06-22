# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetTenantCheckAvailableResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetTenantCheckAvailableResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetTenantCheckAvailableResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTenantCheckAvailableResponseBodyData(DaraModel):
    def __init__(
        self,
        next_scan_time: int = None,
        status: int = None,
    ):
        # The timestamp of the next time when a one-click scan can be submitted.
        self.next_scan_time = next_scan_time
        # The current status of the one-click scan. Valid values:
        # 
        # - 0: The one-click scan can be submitted.
        # 
        # - 1: The current task is not complete. The scan cannot be submitted.
        # 
        # - 2: The free scan quota for this week has been used. Wait until the next free scan time.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_scan_time is not None:
            result['NextScanTime'] = self.next_scan_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextScanTime') is not None:
            self.next_scan_time = m.get('NextScanTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

