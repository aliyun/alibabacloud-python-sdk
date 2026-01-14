# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBandwidthPackageAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        instance_id: str = None,
        renewal_status: str = None,
        request_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled.
        # 
        # *   **true**
        # *   **false** (default)
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: month. Valid values: **1** to **12**.
        # 
        # >  This parameter is returned only if the value of **AutoRenew** is **true**.
        self.auto_renew_duration = auto_renew_duration
        # The ID of the bandwidth plan.
        self.instance_id = instance_id
        # The auto-renewal status of the bandwidth plan.
        # 
        # *   **AutoRenewal**: The bandwidth plan is automatically renewed.
        # *   **Normal**: You must manually renew the bandwidth plan.
        # *   **NotRenewal**: The bandwidth plan is not renewed after it expires. The system sends a non-renewal reminder three days before the expiration date but no longer sends reminders to renew the bandwidth plan. You can change the auto-renewal status of a bandwidth plan from NotRenewal to **Normal** or **AutoRenewal**.
        # 
        # >  **RenewalStatus** takes precedence over **AutoRenew**. If you do not specify **RenewalStatus**, **AutoRenew** is automatically used.
        self.renewal_status = renewal_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

