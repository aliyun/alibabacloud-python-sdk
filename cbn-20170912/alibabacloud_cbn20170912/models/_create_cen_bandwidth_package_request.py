# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateCenBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        bandwidth: int = None,
        bandwidth_package_charge_type: str = None,
        client_token: str = None,
        description: str = None,
        geographic_region_aid: str = None,
        geographic_region_bid: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        pricing_cycle: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateCenBandwidthPackageRequestTag] = None,
    ):
        # Specifies whether to automatically complete the payment of the bandwidth plan. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # If you set the parameter to false, go to Billing Management to complete the payment after you call this operation. The instance is created only after you complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable the auto-renewal feature. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false** (default): disables auto-renewal.
        # 
        # > Only subscription bandwidth plans support auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months. Valid values: **0** to **2147483647**. Default value: **1**.
        self.auto_renew_duration = auto_renew_duration
        # The maximum bandwidth value of the bandwidth plan. Unit: Mbit/s. Valid values: **2** to **10000**.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The billing method of the bandwidth plan. Set the value to **PREPAY**, which indicates that the billing method is pay-as-you-go.
        self.bandwidth_package_charge_type = bandwidth_package_charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the bandwidth plan.
        self.description = description
        # The area where the network instance is deployed. Valid values:
        # 
        # *   **China**: Chinese mainland
        # *   **North-America**: North America
        # *   **Asia-Pacific**: Asia Pacific
        # *   **Europe**: Europe
        # 
        # This parameter is required.
        self.geographic_region_aid = geographic_region_aid
        # The area where the other network instance is deployed. Valid values: Valid values:
        # 
        # *   **China**: Chinese mainland
        # *   **North-America**: North America
        # *   **Asia-Pacific**: Asia Pacific
        # *   **Europe**: Europe
        # 
        # This parameter is required.
        self.geographic_region_bid = geographic_region_bid
        # The name of the bandwidth plan.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The name must start with a letter and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the bandwidth plan. Default value: 1.
        # 
        # *   If **PricingCycle** is set to **Month**, set **Period** to a value from **1** to **3** or **6**.
        # *   If **PricingCycle** is set to **Year**, set **Period** to a value from **1** to **3**.
        # 
        # > This parameter is required when **BandwidthPackageChargeType** is set to **PREPAY**.
        self.period = period
        # The billing cycle of the bandwidth plan. Valid values:
        # 
        # *   **Month** (default): billed on a monthly basis.
        # *   **Year**: billed on an annual basis.
        self.pricing_cycle = pricing_cycle
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid

        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')

        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCenBandwidthPackageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateCenBandwidthPackageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag keys cannot be an empty string. The tag key can be up to 64 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # The tag value can be 0 to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # Each tag key must have a unique tag value. You can specify at most 20 tag values in each call.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

