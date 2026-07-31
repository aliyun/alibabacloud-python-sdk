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
        # Specifies whether to enable auto-renewal for the subscription dedicated host. Valid values:
        # 
        # - true: Enables auto-renewal for the subscription dedicated host.
        # 
        # - false: Disables auto-renewal for the subscription dedicated host.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # Specifies whether to enable auto-renewal for the dedicated host to follow the subscription ECS instances on the host.
        # 
        # If your dedicated host (DDH) uses the subscription billing method and the subscription ECS instances on the DDH have auto-renewal enabled, you can use this parameter to configure the DDH to automatically renew along with the ECS instances. When an ECS instance on the DDH is automatically renewed, if the DDH expires earlier than the new expiration time of the ECS instance, the DDH is also automatically renewed. The principle of DDH auto-renewal following ECS instances is as follows:
        # 
        # The DDH automatically determines the new expiration time of the corresponding ECS instance, and then selects the minimum renewal period that is greater than the ECS instance expiration time and meets the DDH renewal cycle. For details about the supported renewal cycles of DDHs, see the metric descriptions of the PeriodUnit and Duration parameters.
        # 
        # Example: A subscription DDH expires on January 15 of the current year. After a subscription ECS instance on the DDH is automatically renewed, the ECS instance expiration is extended to November 15 of the current year. The DDH lifecycle is 10 months shorter than the ECS instance lifecycle. In this case, the DDH selects the minimum renewal period that is greater than 10 months and meets the DDH renewal cycle, which is 12 months (PeriodUnit=Month and Duration=12).
        # 
        # Valid values:
        # 
        # - AutoRenewWithEcs: Enables auto-renewal following the subscription ECS instances on the dedicated host.
        # - StopRenewWithEcs: Disables auto-renewal following the subscription ECS instances on the dedicated host.
        # - NoOperation: Does not change the current settings of the dedicated host.
        # 
        # > If you set this parameter to AutoRenewWithEcs, make sure that auto-renewal is enabled for the dedicated host (AutoRenew=true). Otherwise, this parameter only changes the parameter value, and the actual auto-renewal feature following ECS instances does not take effect.
        # 
        # Default value: NoOperation.
        self.auto_renew_with_ecs = auto_renew_with_ecs
        # The IDs of dedicated hosts. You can specify up to 100 subscription dedicated host IDs. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.dedicated_host_ids = dedicated_host_ids
        # The renewal period. Valid values:
        # 
        # <props="china">
        # - If PeriodUnit is set to Week: 1, 2, 3, and 4.
        # - If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # - If PeriodUnit is set to Year: 1, 2, 3, 4, and 5.
        # 
        # 
        # 
        # <props="intl">
        # - If PeriodUnit is set to Month: 1 and 12.
        # - If PeriodUnit is set to Year: 1 and 12.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the renewal period. Valid values:
        # 
        # <props="china">
        # - Week
        # - Month
        # - Year
        # 
        # 
        # 
        # <props="intl">
        # - Month
        # - Year
        # 
        # 
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The region ID of the dedicated host.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable auto-renewal for the subscription dedicated host. The RenewalStatus parameter takes precedence over the AutoRenew parameter. Valid values:
        # 
        # - AutoRenewal: Enables auto-renewal.
        # 
        # - Normal: Disables auto-renewal but the system still sends expiration notifications.
        # 
        # - NotRenewal: Disables auto-renewal and the system does not send expiration notifications. Three days before expiration, the system automatically sends a non-renewal notification. You can change the value of this parameter to Normal for a dedicated host, and then manually renew the host by calling [RenewDedicatedHosts](https://help.aliyun.com/document_detail/134250.html) or set the value to AutoRenewal to enable auto-renewal.
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

