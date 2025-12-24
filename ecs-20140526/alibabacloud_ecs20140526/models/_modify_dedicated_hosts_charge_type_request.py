# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDedicatedHostsChargeTypeRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        client_token: str = None,
        dedicated_host_charge_type: str = None,
        dedicated_host_ids: str = None,
        detail_fee: bool = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to automatically complete the payment. Valid value:
        # 
        # *   true: The payment is automatically completed. Ensure that your account balance is sufficient. Otherwise, your order becomes invalid and must be canceled.
        # *   false: An order is generated but no payment is made.
        # 
        # Default value: true.
        # 
        # >  If you do not have sufficient balance in your account, you can set `AutoPay` to `false` to generate an unpaid order. Then, you can pay for the order.
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The new billing method for the dedicated host. Valid value:
        # 
        # *   PrePaid: changes the billing method from pay-as-you-go to subscription.
        # *   PostPaid: changes the billing method from subscription to pay-as-you-go.
        # 
        # Default value: PrePaid.
        self.dedicated_host_charge_type = dedicated_host_charge_type
        # The IDs of the dedicated hosts. The value can be a JSON array that consists of up to 20 dedicated host IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.dedicated_host_ids = dedicated_host_ids
        # Specifies whether to return the billing details of the order when the billing method is changed from subscription to pay-as-you-go.
        # 
        # Indicates whether the nfs volume is set to the read-only mode. Default value: false.
        self.detail_fee = detail_fee
        # Specifies whether to perform only a dry run. Valid value:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized Resource Access Management (RAM) users, and missing parameter values. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        # 
        # Indicates whether the nfs volume is set to the read-only mode. Default value: false.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal duration of the subscription dedicated hosts. Valid values:
        # 
        # *   If you set `PeriodUnit` to Week, valid values of `Period` are 1, 2, 3, and 4.
        # *   If you set `PeriodUnit` to Month, valid values of `Period` are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The unit of the renewal duration specified by `Period`. Valid values:
        # 
        # *   Week
        # *   Month
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The region ID of the dedicated hosts. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dedicated_host_charge_type is not None:
            result['DedicatedHostChargeType'] = self.dedicated_host_charge_type

        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids

        if self.detail_fee is not None:
            result['DetailFee'] = self.detail_fee

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DedicatedHostChargeType') is not None:
            self.dedicated_host_charge_type = m.get('DedicatedHostChargeType')

        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')

        if m.get('DetailFee') is not None:
            self.detail_fee = m.get('DetailFee')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

