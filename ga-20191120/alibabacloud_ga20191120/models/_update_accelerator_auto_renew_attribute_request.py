# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAcceleratorAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        client_token: str = None,
        name: str = None,
        region_id: str = None,
        renewal_status: str = None,
    ):
        # The ID of the Global Accelerator instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Auto-renewal is enabled.
        # 
        # - **false** (default): Auto-renewal is disabled.
        # 
        # > You must specify at least one of **AutoRenew** and **RenewalStatus**.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: month.
        # 
        # Valid values: **1** to **12**.
        # 
        # > This parameter takes effect only when **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** may be different for each request.
        self.client_token = client_token
        # The name of the Global Accelerator instance.
        # 
        # The name must be 1 to 128 characters in length, start with a letter or a Chinese character, and can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name
        # The region ID of the Global Accelerator instance. Set the value to **cn-hangzhou**.
        self.region_id = region_id
        # The auto-renewal status of the Global Accelerator instance. Valid values:
        # 
        # - **AutoRenewal**: The instance is configured for auto-renewal.
        # 
        # - **Normal**: The instance is configured for manual renewal.
        # 
        # - NotRenewal: The instance is not renewed. The system does not send expiration reminders, but sends a non-renewal reminder three days before the expiration date. You can change the renewal status from **NotRenewal** to **Normal** to manually renew the instance, or change the renewal status to **AutoRenewal**.
        # 
        # > * You must specify at least one of **AutoRenew** and **RenewalStatus**.
        # >
        # > * The **RenewalStatus** parameter takes precedence over the **AutoRenew** parameter. If you do not specify **RenewalStatus**, the value of **AutoRenew** is used.
        self.renewal_status = renewal_status

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        return self

