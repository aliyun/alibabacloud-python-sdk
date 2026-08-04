# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateExcessiveDeviceRegistrationApplicationsStatusRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        status: str = None,
    ):
        # List of IDs for device registration applications that exceed your quota.
        # 
        # This parameter is required.
        self.application_ids = application_ids
        # Status of the device registration application. Valid values:
        # 
        # - **Approved**: Approve the application. You can approve only applications with a Pending status.
        # 
        # - **Rejected**: Reject the application. You can reject only applications with a Pending status.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

