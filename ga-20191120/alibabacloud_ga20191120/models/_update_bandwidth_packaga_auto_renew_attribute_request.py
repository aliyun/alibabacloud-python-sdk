# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBandwidthPackagaAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        client_token: str = None,
        instance_id: str = None,
        name: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # >  You must specify **AutoRenew** or **RenewalStatus**.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months. Valid values: **1** to **12**.
        # 
        # > This parameter takes effect only if **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The ID of the bandwidth plan.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the bandwidth plan.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The auto-renewal status of the bandwidth plan. Valid values:
        # 
        # *   **AutoRenewal**: The bandwidth plan is automatically renewed.
        # *   **Normal**: You must manually renew the bandwidth plan.
        # *   **NotRenewal**: The bandwidth plan is not renewed after it expires. The system sends only a non-renewal reminder three days before the expiration date. To renew a bandwidth plan for which you set RenewalStatus to NotRenewal, you can change the value of RenewalStatus from NotRenewal to Normal, and then manually renew the bandwidth plan. You can also set RenewalStatus to **AutoRenewal**.
        # > *   You must specify **AutoRenew** or **RenewalStatus**.
        # > *   **RenewalStatus** takes precedence over **AutoRenew**. If you do not specify **RenewalStatus**, **AutoRenew** is used.
        self.renewal_status = renewal_status

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

