# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically renew the instance before it expires.
        # 
        # - true: enables auto-renewal.
        # - false: disables auto-renewal.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal duration of the instance.
        # 
        # <props="china">
        # - When `PeriodUnit` is set to `Year`, the valid values of `Duration` are: {"1", "2", "3", "4", "5"}
        # - When `PeriodUnit` is set to `Month`, the valid values of `Duration` are: {"1", "2", "3", "6", "12", "24", "36", "48", "60"}
        # - When `PeriodUnit` is set to `Week`, the valid values of `Duration` are: {"1", "2", "3", "4"}
        # 
        # 
        # 
        # <props="intl">
        # - When `PeriodUnit` is set to `Year`, the valid values of `Duration` are: {"1", "2", "3", "4", "5"}
        # - When `PeriodUnit` is set to `Month`, the valid values of `Duration` are: {"1", "2", "3", "6", "12", "24", "36", "48", "60"}
        # 
        # 
        # 
        # <props="partner">
        # - When `PeriodUnit` is set to `Year`, the valid values of `Duration` are: {"1", "2", "3", "4", "5"}
        # - When `PeriodUnit` is set to `Month`, the valid values of `Duration` are: {"1", "2", "3", "6", "12", "24", "36", "48", "60"}
        self.duration = duration
        # Instance ID. You can specify up to 100 subscription instances at a time. Separate multiple instance IDs with commas (,).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the renewal duration, that is, the unit of the `Duration` parameter. Valid values:
        # 
        # <props="china">
        # - Week
        # - Month (default)
        # - Year
        # 
        # 
        # 
        # <props="intl">
        # - Month (default)
        # - Year
        # 
        # 
        # 
        # <props="partner">
        # - Month (default)
        # - Year
        self.period_unit = period_unit
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The auto-renewal status of the instance. Valid values:
        # 
        # - AutoRenewal: enables auto-renewal.
        # 
        # - Normal: disables auto-renewal.
        # 
        # - NotRenewal: does not renew the instance. After this value is set, the system no longer sends expiration reminders and only sends a non-renewal reminder three days before the instance expires. ECS instances that are set to not renew can be changed to pending renewal (`Normal`), and then manually renewed or set to auto-renewal.
        # 
        # > The `RenewalStatus` parameter takes precedence over the `AutoRenew` parameter. If the `RenewalStatus` parameter is not specified, the `AutoRenew` parameter takes effect by default.
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

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

