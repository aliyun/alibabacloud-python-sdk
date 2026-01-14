# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAcceleratorAutoRenewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        renewal_status: str = None,
        request_id: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # Indicates whether auto-renewal is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: month.
        self.auto_renew_duration = auto_renew_duration
        # Indicates how the GA instance is renewed. Valid values:
        # 
        # *   **AutoRenewal**: The GA instance is automatically renewed.
        # *   **Normal**: You must manually renew the GA instance.
        # *   **NotRenewal**: The GA instance is not renewed after it expires. The system sends only a non-renewal reminder three days before the expiration date. The system no longer sends notifications to remind you to renew the GA instance.
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
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

