# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDedicatedHostAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_with_ecs: str = None,
        dedicated_host_ids: str = None,
        duration: int = None,
        owner_account: str = None,
        owner_id: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically renew the subscription. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false
        self.auto_renew = auto_renew
        # Specifies whether to automatically renew the subscription dedicated hosts along with the subscription ECS instances hosted on the dedicated hosts.
        # 
        # If auto-renewal is enabled for the subscription ECS instances hosted on the subscription dedicated hosts, you can specify this parameter to automatically renew the dedicated hosts along with the subscription ECS instances. When the subscription ECS instances hosted on your dedicated hosts are automatically renewed, the subscription dedicated hosts are also automatically renewed if the expiration time of the dedicated hosts is earlier than the expiration time of the renewed instances. Take note of the following items:
        # 
        # When the subscription dedicated hosts are configured to be automatically renewed along with the subscription ECS instances hosted on the dedicated hosts, the system checks the expiration time of the renewed instances and selects a minimum renewal duration for the dedicated hosts so that the dedicated hosts are renewed by a duration that ends later than the expiration time of the renewed instances. For more information about supported renewal durations, see the descriptions of the `PeriodUnit` and `Duration` parameters.
        # 
        # For example, assume that a dedicated host expires on January 15 of the current year. Subscription ECS instances hosted on the dedicated host are configured to be automatically renewed to November 15 of the same year. The expiration time of the dedicated host is earlier than the expiration time of the ECS instances by 10 months. In this case, the system selects a renewal duration of 12 months (a minimum duration calculated based on a `Duration` value of 12 and a `PeriodUnit` value of Month) for the dedicated host. This ensures that the dedicated host expires later than the ECS instances.
        # 
        # Valid values:
        # 
        # *   AutoRenewWithEcs: automatically renews the subscription dedicated hosts along with the subscription ECS instances hosted on the dedicated hosts.
        # *   StopRenewWithEcs: does not automatically renew the subscription dedicated hosts along with the subscription ECS instances hosted on the dedicated hosts.
        # *   NoOperation: does not change the current settings for the dedicated hosts.
        # 
        # > If you set this parameter to AutoRenewWithEcs, make sure that `AutoRenew` is set to true to enable auto-renewal for the dedicated hosts. Otherwise, the subscription dedicated hosts are not automatically renewed along with the subscription ECS instances hosted on the dedicated hosts.
        # 
        # Default value: NoOperation.
        self.auto_renew_with_ecs = auto_renew_with_ecs
        # The IDs of dedicated hosts. You can specify up to 100 subscription dedicated host IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.dedicated_host_ids = dedicated_host_ids
        # The renewal duration.
        # 
        # *   Valid values when PeriodUnit is set to Month: 1 and 12
        # *   Valid values when PeriodUnit is set to Year: 1 and 12
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the renewal period. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month
        self.period_unit = period_unit
        # The region ID of the dedicated host.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to automatically renew the subscription dedicated host. The `RenewalStatus` parameter takes precedence over the `AutoRenew` parameter. Valid values:
        # 
        # *   AutoRenewal: The dedicated hosts are automatically renewed.
        # *   Normal: The dedicated hosts are not automatically renewed, and renewal notifications are sent.
        # *   NotRenewal: The dedicated hosts are not automatically renewed, and no expiration notification is sent. A notification of no renewal is automatically sent three days before the end of the current subscription cycle. You can change the value of this parameter from NotRenewal to Normal and manually renew the dedicated hosts by calling the [RenewDedicatedHosts](https://help.aliyun.com/document_detail/134250.html) operation. Alternatively, you can renew the dedicated hosts by setting this parameter to AutoRenewal.
        self.renewal_status = renewal_status
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_with_ecs is not None:
            result['AutoRenewWithEcs'] = self.auto_renew_with_ecs

        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewWithEcs') is not None:
            self.auto_renew_with_ecs = m.get('AutoRenewWithEcs')

        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

